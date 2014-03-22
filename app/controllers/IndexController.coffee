App.IndexController = Ember.ArrayController.extend(
  sortProperties: ["date"]
  sortAscending: false
  contentWithIndexes: ( ->
    sortedContent = this.content.sortBy(this.sortProperties)
    indexedContent = sortedContent.map (item, index) ->
      item: item
      index: index
    indexedContent.reverseObjects()
  ).property('controller.@each')
)
