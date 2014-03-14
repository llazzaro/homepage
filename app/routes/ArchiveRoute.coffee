module.exports = App.ArchiveRoute = Ember.Route.extend
  model: (params) ->
    this.store.find('post',params.archive_id)

  actions: ->
    error: (reason) ->
      alert(reason)
