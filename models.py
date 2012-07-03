from google.appengine.ext import db


#
class Entry(db.Model):
    author = db.UserProperty()
    title = db.StringProperty(required=True)
    intro = db.TextProperty(required=True)
    photo = db.BlobProperty()
    slug = db.StringProperty(required=True)
    text = db.TextProperty(required=True)
    created_at = db.DateTimeProperty(auto_now=True)
    published_at = db.DateTimeProperty(auto_now=True)
    draft = db.BooleanProperty()

    def view_template(self):
        return 'post.html'

class FlickrEntry(db.Model):
    title = db.StringProperty(required=True)
    created_at = db.DateTimeProperty(auto_now=True)
    published_at = db.DateTimeProperty(auto_now=True)
    flickr_html = db.TextProperty(required=True)
    draft = db.BooleanProperty()
    
    def view_template(self):
        return 'flickr.html'

class Tag(db.Model):
    name = db.StringProperty()
    entry = db.ReferenceProperty(Entry, collection_name='tags')


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
    curriculum = db.ReferenceProperty(Curriculum, collection_name='lenguages')


class Technology(db.Model):
    name = db.StringProperty()
    link = db.StringProperty()
    curriculum = db.ReferenceProperty(Curriculum, collection_name='technology')


class Job(db.Model):
    name = db.StringProperty()
    description = db.TextProperty()
    start = db.DateProperty()
    end = db.DateProperty()
    curriculum = db.ReferenceProperty(Curriculum, collection_name='jobs')


class Interests(db.Model):
    name = db.StringProperty()
    curriculum = db.ReferenceProperty(Curriculum, collection_name='interests')


#
class Study(db.Model):
    name = db.StringProperty()
    name_universy = db.StringProperty()
    name_faculty = db.StringProperty()
    start = db.DateProperty()
    end = db.DateProperty()
    curriculum = db.ReferenceProperty(Curriculum, collection_name='estudies')


#
class Gallery(db.Model):
    name = db.StringProperty()
    draft = db.BooleanProperty()
    created_at = db.DateProperty()
    description = db.StringProperty()


class Photo(db.Model):
    name = db.StringProperty()
    description = db.StringProperty()
    link = db.StringProperty()
    gallery = db.ReferenceProperty(Gallery, collection_name='photos')


class Comment(db.Model):
    text = db.StringProperty()


class Network(db.Model):
    name = db.StringProperty()
    link = db.StringProperty()
    favicon = db.StringProperty()

class Location(db.Model):
    name = db.StringProperty()
    arrival = db.DateTimeProperty()
