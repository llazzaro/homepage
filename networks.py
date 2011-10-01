import re
import wsgiref.handlers
from google.appengine.ext import webapp
from models import *
from decorators import templateSelector

class NetworkHandler(webapp.RequestHandler):

    @templateSelector('templates/network/new_network.html')
    def get(self):
        entry = None
        if self.request.get('key'):
            entry = db.get(self.request.get('key'))

        return self.response, {'entry': entry}

    def post(self):
        #is this a new entry or edit entry?
        if self.request.get('key') is '':
            oNetwork = Network(
                link = self.request.get('link'),
                name = self.request.get('name'),
                )
        else:
            oNetwork = db.get(self.request.get('key'))
            oNetwork.name = self.request.get('name')
            oNetwork.link = self.request.get('link')

        pattern = r'(([a-z]+)\.)*([a-z]+)\.(com|org)'
        domain = re.search(pattern, oNetwork.link).group(0)
        oNetwork.favicon =  domain + '/favicon.ico'
        oNetwork.put()

        self.redirect('/networks/admin')

#Admin network begin here
class DeleteNetworkHandler(webapp.RequestHandler):
    def post(self):
        network = Network.get(self.request.get('key'))
        if network:
            network.delete()

        self.redirect('/networks/admin')


class AdminHandler(webapp.RequestHandler):
    @templateSelector('templates/network/admin.html')
    def get(self):
        networks = db.Query(Network).fetch(limit=10)
        return self.response, {'networks': networks}

def main():
    application = webapp.WSGIApplication([
                (r'/networks/admin/new', NetworkHandler),
                (r'/networks/admin/edit/?', NetworkHandler),
                (r'/networks/admin/delete/?', DeleteNetworkHandler),
                (r'/networks/admin', AdminHandler),
                ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
