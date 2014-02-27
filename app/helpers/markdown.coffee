Ember.Handlebars.helper "format-markdown", (body) ->
  converter = new Showdown.converter()
  new Handlebars.SafeString(converter.makeHtml(text))
