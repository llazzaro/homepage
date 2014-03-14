module.exports = App.IndexRoute = Ember.Route.extend
  model: ->
    this.store.find('post')

  actions: ->
    error: (reason) ->
      alert(reason)
