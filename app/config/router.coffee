module.exports = App.Router.map ->
  @route "archives",
    path: "/archives"

  @route "archive",
    path: "/archive/:archive_id"

  @route "about",
    path: "/about"

  return
