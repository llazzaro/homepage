import os,functools
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

    projects = db.Query(Project).get()
    
    temp = os.path.join(os.path.dirname(__file__),'templates/projects/projects.html')
    logging.info(temp)    

    outstr = template.render(temp,{'nombre_seccion':nombre_seccion,'texto_seccion':texto_seccion,'path':path,'projects':projects})
    self.response.out.write(outstr)

  def getSeccion(self,path):
    return { 
		'/index':  'Inicio',
		'/cv':'Curriculum Vitae',
		'/about':'Acerca de',
		'/projects':'Projects',
		'/blog':'Blog',
		'/fotos':'Fotos',
	}[path]

class NotFoundHandler(webapp.RequestHandler):
  def get(self):
    temp = os.path.join(os.path.dirname(__file__),'templates/404.html')
    outstr = template.render(temp,{})
    self.response.out.write(outstr)

class AdminHandler(webapp.RequestHandler):
  def get(self):
    pass

def main():
  application = webapp.WSGIApplication([
		(r'/projects',MainHandler),
		],debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
