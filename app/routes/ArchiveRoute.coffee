module.exports = App.ArchiveRoute = Ember.Route.extend
  model: (params) ->
    App.TextPost.find({id: params.archive_id})
