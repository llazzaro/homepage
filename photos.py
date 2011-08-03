import os
import functools
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from models import *
from decorators import templateSelector
import logging

#def templateSelector(func,template):
#  temp = os.path.join(os.path.dirname(__file__),template)
#  outstr = temp.render(temp,func)
#  self.response.out.write(outstr)


class MainHandler(webapp.RequestHandler):
    @templateSelector('templates/photos/photos.html')
    def get(self):
        path = self.request.path
        nombre_seccion = self.getSeccion(path)
        texto_seccion = "texto seccion"
        admin = users.is_current_user_admin()
        galleries = db.Query(Gallery).order('-created_at').fetch(limit=10)
        return self.response, {
                    'nombre_seccion': nombre_seccion,
                    'texto_seccion': texto_seccion,
                    'path': path,
                    'admin': admin,
                    'galleries': galleries}

    def getSeccion(self, path):
        return {
                '/index': 'Inicio',
                '/cv': 'Curriculum Vitae',
                '/about': 'Acerca de',
                '/projects': 'Proyectos',
                '/blog': 'Blog',
                '/photos': 'Fotos',
            }[path]

#class GalleryHandler(webapp.RequestHandler):
#  def get(self):
#    pass


class AdminHandler(webapp.RequestHandler):
    @templateSelector('templates/photos/admin.html')
    def get(self):
        galleries = db.Query(Gallery).order('-created_at').fetch(limit=10)
        return self.response, {'galleries': galleries}


class PhotoHandler(webapp.RequestHandler):
    @templateSelector('templates/photos/new_photo.html')
    def get(self):
        photo = None
        gallery = db.get(self.request.get('gallery'))
        if self.request.get('key'):
            photo = db.get(self.request.get('key'))

        return self.response, {'photo': photo, 'gallery': gallery}

    def post(self):
        gallery = db.get(self.request.get('gallery'))
        if self.request.get('key') is '':
            photo = Photo(
                name = self.request.get('name'),
                description = self.request.get('description'),
                link = self.request.get('link'),
                gallery = gallery,
            )
        else:
            photo = db.get(self.request.get('key'))
            photo.descripcion = self.request.get('descripcion')
            photo.nombre = self.request.get('nombre')
            photo.borrador = bool(self.request.get('borrador'))

        photo.put()
        self.redirect(
                '/photos/gallery?key=%s ' % (self.request.get('gallery')))


class GalleryHandler(webapp.RequestHandler):
    @templateSelector('templates/photos/new_gallery.html')
    def get(self):
        gallery = None
        if self.request.get('key'):
            gallery = db.get(self.request.get('key'))

        return self.response, {'gallery': gallery}

    def post(self):
        if self.request.get('key') is '':
            gallery = Gallery(
                nombre = self.request.get('nombre'),
                descripcion = self.request.get('descripcion'),
                borrador = bool(self.request.get('borrador'))
            )
        else:
            gallery = db.get(self.request.get('key'))
            gallery.descripcion = self.request.get('descripcion')
            gallery.nombre = self.request.get('nombre')
            gallery.borrador = bool(self.request.get('borrador'))

        gallery.put()
        self.redirect('/photos/admin')


class NotFoundHandler(webapp.RequestHandler):
    def get(self):
        temp = os.path.join(os.path.dirname(__file__), 'templates/404.html')
        outstr = template.render(temp, {})
        self.response.out.write(outstr)


class ViewGalleryHandler(webapp.RequestHandler):
    @templateSelector('templates/photos/gallery.html')
    def get(self):
        if self.request.get('key'):
            gallery = db.get(self.request.get('key'))
            #photos = db.Query(Foto).filter('gallery=',gallery)
            admin = users.is_current_user_admin()
        return self.response, {'gallery': gallery, 'admin': admin}


def main():
    application = webapp.WSGIApplication([
                    (r'/photos', MainHandler),
                    (r'/photos/gallery/?', ViewGalleryHandler),
                    (r'/photos/admin', AdminHandler),
                    (r'/photos/admin/new_gallery', GalleryHandler),
                    (r'/photos/admin/gallery/edit/?', GalleryHandler),
                    (r'/photos/admin/new_photo/?', PhotoHandler),
                    ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
