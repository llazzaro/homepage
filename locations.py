import datetime
import time
import wsgiref.handlers
from google.appengine.ext import webapp
from decorators import templateSelector
from models import *

class LocationHandler(webapp.RequestHandler):

    @templateSelector('templates/location/new_location.html')
    def get(self):
        entry = None
        if self.request.get('key'):
            entry = db.get(self.request.get('key'))

        return self.response, {'entry': entry}

    def post(self):
        #is this a new entry or edit entry?
        arrival = datetime.datetime.fromtimestamp(
                time.mktime(
                    time.strptime(
                        self.request.get('arrival'),'%Y-%m-%d')
                    )
                )

        if self.request.get('key') is '':
            oLocation = Location(
                name = self.request.get('name'),
                arrival = arrival,
                )
        else:
            oLocation = db.get(self.request.get('key'))
            oLocation.name = self.request.get('name')
            oLocation.arrival = arrival

        oLocation.put()

        self.redirect('/locations/admin')

#Admin location begin here
class DeleteLocationHandler(webapp.RequestHandler):
    def post(self):
        location = Location.get(self.request.get('key'))
        if location:
            location.delete()

        self.redirect('/location/admin')


class AdminHandler(webapp.RequestHandler):
    @templateSelector('templates/location/admin.html')
    def get(self):
        locations = db.Query(Location).fetch(limit=10)
        return self.response, {'locations': locations}

def main():
    application = webapp.WSGIApplication([
                (r'/locations/admin/new', LocationHandler),
                (r'/locations/admin/edit/?', LocationHandler),
                (r'/locations/admin/delete/?', DeleteLocationHandler),
                (r'/locations/admin', AdminHandler),
                ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
