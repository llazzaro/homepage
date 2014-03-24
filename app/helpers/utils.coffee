Ember.Handlebars.helper "if_even", (number) ->
  if (number % 2) is 0
    "even"
  else
    "odd"
