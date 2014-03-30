App.Post = DS.Model.extend(
  date: DS.attr('date'),
  title: DS.attr('string'),
  body: DS.attr('string'),
  tags: DS.attr()
)

App.PostAdapter = DS.Adapter.extend(
  api_key: 'hSdfszPwGFt7wWTMnPmgsO8C4SHvWxnIHmX5VC0ujL9ZlEw5wb'
  tumblr_blog: 'llazzaro.tumblr.com'
  tumblr_url: 'http://api.tumblr.com/v2/blog/'
  post_type: 'text'

  findAll: (store, type)->
    _this = this
    return $.ajax(
      type: 'GET'
      url: _this.tumblr_url + _this.tumblr_blog + '/posts/' + _this.post_type + '?api_key=' + _this.api_key
      contentType: 'application/json'
      dataType: 'jsonp'
    ).then((data) ->
      data.response.posts
    )
  find: (store, type, id) ->
    _this = this
    return $.ajax(
      type: 'GET'
      url: _this.tumblr_url + _this.tumblr_blog + '/posts/text' + _this.post_type  + '?id=' + id + '&api_key=' + _this.api_key
      contentType: 'application/json'
      dataType: 'jsonp'
    ).then((data) ->
      data.response.posts[0]
    )
)
