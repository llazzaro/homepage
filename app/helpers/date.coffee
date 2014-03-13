Ember.Handlebars.helper "date-start-of", (date) ->
  date = date.replace(' GMT','')
  moment(date).fromNow()

Ember.Handlebars.helper "date-with-month", (date) ->
  date = date.replace(' GMT','')
  moment(date).format('LL')

Ember.Handlebars.helper "date-on-days", (date) ->
  date = date.replace(' GMT','')
  moment(date).add('days', 10).calendar()
