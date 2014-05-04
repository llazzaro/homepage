Ember.Handlebars.helper "if_even", (number) ->
  if (number % 2) is 0
    "even"
  else
    "odd"

Ember.Handlebars.helper "trim", (body) ->
  trimmedBody = body.substring(0, 500)
  new Handlebars.SafeString(trimmedBody)
