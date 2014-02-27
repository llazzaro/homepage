App.Post = DS.Model.extend()
App.Post.reopenClass
  findAll: ->
    _this = this
    @array = Ember.ArrayProxy.extend({}).create()
    $.ajax(
      type: 'GET'
      url: 'http://api.tumblr.com/v2/blog/blog.lazzaroleonardo.com.ar/posts/' + _this.post_type + '?api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4'
      contentType: 'application/json'
      dataType: 'jsonp'
    ).then((data) ->
      _this.array.set('content', data.response.posts)
    )
    return @array
  find: (params) ->
    _this = this
    @post = Ember.ObjectProxy.extend({}).create()
    $.ajax(
      type: 'GET'
      url: 'http://api.tumblr.com/v2/blog/blog.lazzaroleonardo.com.ar/posts/text' + _this.post_type  + '?id=' + params.id + '&api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4'
      contentType: 'application/json'
      dataType: 'jsonp'
    ).then((data) ->
      _this.post.set('content', data.response.posts[0])
    )
    return @post

App.TextPost = App.Post.extend()
App.TextPost.reopenClass post_type: "text"

App.QuotePost = App.Post.extend()
App.QuotePost.reopenClass post_type: "quote"
