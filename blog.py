import os
import functools
import logging
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from models import *
from decorators import templateSelector
import rst


#this returns the entry list
class BlogHandler(webapp.RequestHandler):
    @templateSelector('templates/blog/blog.html')
    def get(self):
        entries = db.Query(Entry).filter(
                                    'draft =', False).order(
                                               '-published_at').fetch(limit=10)
        admin = users.is_current_user_admin()
        return self.response, {'admin': admin,
                                'entries': entries,
                                'nombre_seccion': 'Blog'}


#este devuelve la vista de una entry
class ViewEntryHandler(webapp.RequestHandler):
    @templateSelector('templates/blog/entry_view.html')
    def get(self, slug):
        entry = db.Query(Entry).filter("slug =", slug).get()
        entry.text = rst.rst2html(entry.text)
        return self.response, {'entry': entry, 'nombre_seccion': 'Blog'}


class EntryHandler(webapp.RequestHandler):
    @templateSelector('templates/blog/new_entry.html')
    def get(self):
        entry = None
        if self.request.get('key'):
            entry = db.get(self.request.get('key'))

        return self.response, {'entry': entry}

    def post(self):
        #is this a new entry or edit entry?
        if self.request.get('key') is '':
            oEntry = Entry(
                author = users.get_current_user(),
                title = self.request.get('title'),
                intro = self.request.get('intro'),
                photo = db.Blob(self.request.get('photo')),
                slug = self.request.get('slug'),
                text = self.request.get('text'),
                draft = bool(self.request.get('draft'))
            )
        else:
            oEntry = db.get(self.request.get('key'))
            oEntry.title = self.request.get('title')
            oEntry.intro = self.request.get('intro')
            oEntry.slug = self.request.get('slug')
            oEntry.text = self.request.get('text')
            oEntry.draft = bool(self.request.get('draft'))

        oEntry.put()

#    temp = os.path.join(os.path.dirname(__file__),'templates/blog.html')
#    outstr = template.render(temp,{})
#    self.response.out.write(outstr)
        self.redirect('/blog/admin')


class DeleteEntryHandler(webapp.RequestHandler):
    def post(self):
        entry = Entry.get(self.request.get('key'))
        if entry:
            article.delete()

        self.redirect('/blog/admin')


class AtomHandler(webapp.RequestHandler):
    @templateSelector('templates/blog/rss.xml')
    def get(self):
        entries = Entry.get_all()
        self.response.headers['Content-Type'] = 'text/xml'
        return self.response, {'entries': entries}


class RSSHandler(webapp.RequestHandler):
    @templateSelector('templates/blog/rss.xml')
    def get(self):
        entries = db.Query(Entry).order('-published_at').fetch(limit=10)
        self.response.headers['Content-Type'] = 'text/xml'
        return self.response, {'entries': entries}


class AdminHandler(webapp.RequestHandler):
    @templateSelector('templates/blog/admin.html')
    def get(self):
        entries = db.Query(Entry).order('-published_at').fetch(limit=10)
        return self.response, {'entries': entries}


class TagHandler(webapp.RequestHandler):
    @templateSelector('templates/blog/blog.html')
    def get(self, tag):
        entries = db.Query(Entry).filter(
                    'tags =', tag).order(
                            '-published_at').fetch(FETCH_THEM_ALL)
        return self.response, {'entries': entries}


class DateHandler(webapp.RequestHandler):
    pass


class GetImage(webapp.RequestHandler):
    def get(self):
        slug = self.request.get('slug')
        entry = db.Query(Entry).filter("slug = ", slug).get()
        if (entry and entry.photo):
            self.response.headers['Content-Type'] = 'image/jpeg'
            self.response.out.write(entry.photo)
        else:
            self.error(404)
            #self.redirect('/static/noimage.jpg')


def main():
    application = webapp.WSGIApplication([
                (r'/blog', BlogHandler),
                (r'/blog/atom', AtomHandler),
                (r'/blog/rss.xml', RSSHandler),
                (r'/blog/entry/([^/]+)', ViewEntryHandler),
                (r'/blog/admin/new', EntryHandler),
                (r'/blog/admin/edit/?', EntryHandler),
                (r'/blog/admin/delete/?', DeleteEntryHandler),
                (r'/blog/admin', AdminHandler),
                (r'/blog/tag/?', TagHandler),
                (r'/blog/date/?', DateHandler),
                (r'/blog/image', GetImage),
                ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
