Ember.Handlebars.helper "random-photo-size", (photo) ->
  sizes = [
      "square"
      "large_square"
      "small"
      "thumbnail"
#      "small_320"
#      "medium"
#      "medium_640"
#      "medium_800"
#      "large"
#      "large_1600"
#      "large_2048"
#      "original"
    ]
  size = sizes[Math.floor(Math.random() * sizes.length)]
  console.log(photo.sizes)
  new Handlebars.SafeString('<div class="item ' + size + '" ><img src="' + photo.source + '"></img></div>')
