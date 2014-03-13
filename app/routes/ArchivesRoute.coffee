module.exports = App.ArchivesRoute = Ember.Route.extend
  beforeModel: ->
    Ember.$('.recent_archives').append($('<div class="box"><div class="clock">'))

#  afterModel: ->
#    Ember.$('.recent_archives .box').remove()

  model: ->
    App.TextPost.findAll()

  actions: ->
    error: (reason) ->
      alert(reason)
