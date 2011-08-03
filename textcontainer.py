import cgi
import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db


class SaveTextHandler(webapp.RequestHandler):
    def post(self):
        #key = self.request.get("key")
        text = self.request.get("text")
        #property_name = self.request.get("property_name")
        #here something to get the model
        self.response.out.write("success%s" % (text))


def main():
    application = webapp.WSGIApplication([
            (r'/text-container/', SaveTextHandler),
            ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
