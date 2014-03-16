App.PhotosView = Ember.View.extend
  template: Handlebars.compile('<div class="photos"></div>')
  didInsertElement: ->

    # This callback runs before lots_of_images has rendered.
    @scheduleMasonry()
    @scheduleFetchPhotosSizes()

    return

  # scheduleOnce debounces applyMasonry to only run once per
  # runloop. scheduleMasonry is called on didInsertElement, and
  # whenever controller.images changes.
  scheduleMasonry: (->
    Ember.run.scheduleOnce 'afterRender', this, @applyMasonry
    return
  ).observes('model.@each')

  applyMasonry: ->
    container = document.querySelector('.container')
    console.log('masonry')
    msnry = new Masonry(container,
      itemSelector: '.item',
      columnWidth: 150
    )
    return

  scheduleFetchPhotosSizes: ->
    _this = this
    _.each this.get('controller').content.content, (photo) ->
      photo.fetchSizes().then( (photo) ->
        _this.applyPhotoSources(photo)
      )
    return

  applyPhotoSources: (photo) ->
    console.log('Loading photo' + photo.sizes)
    container = document.querySelector('.photos')
    template = Handlebars.compile('<img src={{source}} >')
    html = template({source: photo.sizes[1].source})
    container.innerHTML = container.innerHTML.concat(html)
