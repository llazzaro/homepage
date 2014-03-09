Ember.Handlebars.helper "date-start-of", (date) ->
  moment(date).fromNow()

Ember.Handlebars.helper "date-with-month", (date) ->
  moment().format('LL')

Ember.Handlebars.helper "date-on-days", (date) ->
  moment().add('days', 10).calendar()
