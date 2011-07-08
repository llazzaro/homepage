import cgi
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class saveText(webapp.RequestHandler):
        def post(self):
                #key = self.request.get("key")
                text = self.request.get("text")
                #property_name = self.request.get("property_name")
                #here something to get the model
                self.response.out.write("success"+text)

application = webapp.WSGIApplication([
        ('text-container',saveText)
        ])
                
def main():
        run_wsgi_app(application)

if __name__ == "__main__":
        main()
