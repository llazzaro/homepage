module.exports = App.ArchivesRoute = Ember.Route.extend
#beforeModel: ->
#  Ember.$('.recent_archives').append($('<div class="box"><div class="clock">'))

#  afterModel: ->
#    Ember.$('.recent_archives .box').remove()

  model: ->
    this.store.find('post')

  actions: ->
    error: (reason) ->
      alert(reason)
