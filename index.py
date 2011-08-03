import os
import functools
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from models import *
import logging


class MainHandler(webapp.RequestHandler):
    def get(self):
        path = self.request.path
        nombre_seccion = self.getSeccion(path)
        texto_seccion = "texto seccion"
        template_filename = os.path.join(
                                os.path.dirname(__file__),
                                'templates/%s.html' % (path))
        if not os.path.isfile(template_filename):
            #aca deberia ser 404
            #raise self.error(404)
            template_filename = os.path.join(
                                    os.path.dirname(__file__),
                                    'templates/index.html')

        outstr = template.render(
                    template_filename, {
                        'nombre_seccion': nombre_seccion,
                        'texto_seccion': texto_seccion,
                        'path': path})
        self.response.out.write(outstr)

    def getSeccion(self, path):
        return {
                '/': 'Inicio',
                '/cv': 'Curriculum Vitae',
                '/about': 'Acerca de',
                '/projects': 'Proyectos',
                '/blog': 'Blog',
                '/fotos': 'Fotos',
                '/contact': 'Contact',
            }[path]


class NotFoundHandler(webapp.RequestHandler):
    def get(self):
        temp = os.path.join(
                    os.path.dirname(__file__),
                    'templates/404.html')
        outstr = template.render(temp, {})
        self.response.out.write(outstr)


def main():
    application = webapp.WSGIApplication([
                        (r'/', MainHandler),
                        (r'/index', MainHandler),
                        (r'/contact', MainHandler),
                        (r'/?', NotFoundHandler),
                        ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
