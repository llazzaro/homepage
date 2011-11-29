import os
import functools
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from models import *
from decorators import templateSelector
import logging


class MainHandler(webapp.RequestHandler):

    @templateSelector('templates/index.html')
    def get(self):
        path = self.request.path
        networks = Network.all()
        current_location = db.Query(Location).order('-arrival').get()
        from_location = db.Query(Location).order('arrival').get()
        return self.response, {
                        'networks': networks,
                        'current_location': current_location,
                        'from_location': from_location,
                        'path': path}

    def post(self):
        pass


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
