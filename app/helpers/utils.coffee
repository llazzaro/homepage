Ember.Handlebars.helper "if_even", (number) ->
  console.log('even helper')
  console.log(number)
  console.log('dsadas')
  if (number % 2) is 0
    "even"
  else
    "odd"
