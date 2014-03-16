App.Photo = DS.Model.extend(
  title: DS.attr('string'),
  source: DS.attr('string'),
  api_key: '428789fd4adda140b21ea2498ea5297d'
  flickr_user_id: '57745174@N02'
  flickr_url: 'https://api.flickr.com/services/rest/'
  flickr_photos_method: 'flickr.people.getPhotos'
  flickr_photo_method: 'flickr.photos.getSizes'
  attributesBindings: ['sizes']
  sizes: []
  fetchSizes: () ->
    console.log('Fetch Photo Sizes')
    _this = this
    return $.ajax(
      type: 'GET'
      url: _this.flickr_url + '?method=' + _this.flickr_photo_method + '&api_key=' + _this.api_key + '&user_id=' + _this.flickr_user_id + '&photo_id='+ _this.id + '&format=json&jsoncallback=?'
      contentType: 'text/javascript'
      dataType: 'jsonp'
      ).then((data) -> _this.set('sizes', data.sizes.size))
)

App.PhotoAdapter = DS.Adapter.extend(
  api_key: '428789fd4adda140b21ea2498ea5297d'
  flickr_user_id: '57745174@N02'
  flickr_url: 'https://api.flickr.com/services/rest/'
  flickr_photos_method: 'flickr.people.getPhotos'
  flickr_photo_method: 'flickr.photos.getSizes'

  findAll: (store, type) ->
    _this = this
    return $.ajax(
      type: 'GET'
      url: _this.flickr_url + '?method=' + _this.flickr_photos_method + '&api_key=' + _this.api_key + '&user_id=' + _this.flickr_user_id + '&format=json&jsoncallback=?'
      dataType: 'jsonp'
      ).then((data) ->
      _.map data.photos.photo, (photo) ->
        photo.sizes = photo.id
        return photo)
)
