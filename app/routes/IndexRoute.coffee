module.exports = App.IndexRoute = Ember.Route.extend
  model: ->
    App.TextPost.findAll()
