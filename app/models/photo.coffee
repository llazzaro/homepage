App.Photo = DS.Model.extend()

App.Photo.reopenClass
  api_key: '428789fd4adda140b21ea2498ea5297d'
  flickr_user_id: '57745174@N02'
  flickr_url: 'https://api.flickr.com/services/rest/'
  flickr_photos_method: 'flickr.people.getPhotos'
  flickr_photo_method: 'flickr.photos.getSizes'
  findAll: ->
    _this = this
    @array = Ember.ArrayProxy.extend({}).create()
    $.ajax(
      type: 'GET'
      url: _this.flickr_url + '?method=' + _this.flickr_photos_method + '&api_key=' + _this.api_key + '&user_id=' + _this.flickr_user_id + '&format=json&jsoncallback=?'
      dataType: 'jsonp'
    ).then((data) ->
      _this.array.set('content', data.photos.photo)
    )
    return @array

  find: (params) ->
    _this = this
    @photo = Ember.ArrayProxy.extend({}).create()
    $.ajax(
      type: 'GET'
      url: _this.flickr_url + '?method=' + _this.flickr_photo_method + '&api_key=' + _this.api_key + '&user_id=' + _this.flickr_user_id + '&photo_id='+ params.id + '&format=json&jsoncallback=?'
      contentType: 'text/javascript'
      dataType: 'jsonp'
    ).then((data) ->
      _this.photo.set('content', data.sizes.size)
    )
    return @photo
