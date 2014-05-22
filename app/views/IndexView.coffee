App.IndexView = Ember.View.extend
  didInsertElement: ->
    hljs.initHighlightingOnLoad()
