module.exports = App.Router.map ->
  @route "archives",
    path: "/archives"

  @route "archive",
    path: "/archive/:archive_id"

  @route "about",
    path: "/about"

  @route "photos",
    path: "/photos"

  return
