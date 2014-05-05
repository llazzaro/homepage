App.DisqusCommentsComponent = Ember.Component.extend(
  elementId: "disqus_thread"
  tagName: "div"
  didInsertElement: ->
    if window.DISQUS # Simply reload disqus
      id = @get("model.id")
      title = @get("model.title")
      DISQUS.reset
        reload: true
        config: ->
          @page.identifier = id
          @page.title = title
          @page.url = window.location.toString().replace('#', '#!')
          return

    else
      window.disqus_shortname = "llazzaro"
      window.disqus_identifier = @get("model.id")
      window.disqus_url = window.location.toString().replace('#', '#!')
      window.disqus_title = @get("model.title")
      dsq = document.createElement("script")
      dsq.type = "text/javascript"
      dsq.async = true
      dsq.src = "//" + disqus_shortname + ".disqus.com/embed.js"
      (document.getElementsByTagName("head")[0] or document.getElementsByTagName("body")[0]).appendChild dsq
    return

  willDestroyElement: ->
    Em.$("#" + @get("window.discus_url")).remove()
    return
)
