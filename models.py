from google.appengine.ext import db

#
class Entry(db.Model):
  author = db.UserProperty()
  title = db.StringProperty(required=True)
  slug = db.StringProperty(required=True)
  text = db.TextProperty(required=True)
  created_at = db.DateTimeProperty(auto_now=True)
  published_at = db.DateTimeProperty(auto_now=True)
  draft = db.BooleanProperty()


class Tag(db.Model):
  name = db.StringProperty()
  entry = db.ReferenceProperty(Entry,collection_name='tags')

#
class Project(db.Model):
  name = db.StringProperty()
  slug = db.StringProperty()
  description = db.StringProperty()
  text = db.TextProperty()
  progress = db.IntegerProperty()

#
class Curriculum(db.Model):
  names = db.StringProperty()
  surnamess = db.StringProperty()
  nationality = db.StringProperty()
  date_birth = db.DateProperty()
  email = db.StringProperty()

class Lenguages(db.Model):
  name = db.StringProperty()
  curriculum = db.ReferenceProperty(Curriculum,collection_name='lenguages')

class Technology(db.Model):
  name = db.StringProperty()
  curriculum = db.ReferenceProperty(Curriculum,collection_name='technology')

class Jobs(db.Model):
  name = db.StringProperty()
  description = db.TextProperty()
  start = db.DateProperty()
  end = db.DateProperty()
  curriculum = db.ReferenceProperty(Curriculum,collection_name='jobs')
  
class Interests(db.Model):
  name = db.StringProperty()
  curriculum = db.ReferenceProperty(Curriculum,collection_name='interests')

#
class Study(db.Model):
  name = db.StringProperty()
  name_universy = db.StringProperty()
  name_faculty = db.StringProperty()
  start = db.DateProperty()
  end = db.DateProperty()
  curriculum = db.ReferenceProperty(Curriculum,collection_name='estudies')

#modelo para fotos
class Gallery(db.Model):
  name = db.StringProperty()
  draft = db.BooleanProperty()
  created_at = db.DateProperty()
  description = db.StringProperty()

class Photo(db.Model):
  name = db.StringProperty()
  description = db.StringProperty()
  link = db.StringProperty()
  gallery = db.ReferenceProperty(Gallery,collection_name='photos')

