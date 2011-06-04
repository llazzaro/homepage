import os,functools
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from models import *
import logging 
from decorators import templateSelector
import time, datetime

class MainHandler(webapp.RequestHandler):
  @templateSelector('templates/cv/cv.html')
  def get(self):
    path = self.request.path
    nombre_seccion = self.getSeccion(path)
    texto_seccion = "texto seccion"
    cv = db.Query(Curriculum).get()
    admin = users.is_current_user_admin()
    return self.response,{'nombre_seccion':nombre_seccion,'texto_seccion':texto_seccion,'path':path,'cv':cv,'admin':admin}

  def getSeccion(self,path):
    return { 
		'/index':  'Inicio',
		'/cv':'Curriculum Vitae',
		'/about':'Acerca de',
		'/projects':'Proyectos',
		'/blog':'Blog',
		'/fotos':'Fotos',
	}[path]

class EditarHandler(webapp.RequestHandler):
  @templateSelector('templates/cv/admin.html')
  def get(self):
#    if self.request.key('key') is '':
#      cv = Curriculum()
#:Q      cv.put()
    cv = db.get(self.request.get('key'))
    nombre_seccion = 'Edicion Curriculum Vitae'
    texto_seccion = 'bla blah'
    return self.response,{'nombre_seccion':nombre_seccion,'texto_seccion':texto_seccion,'cv':cv}

  def post(self):
    if self.request.get('key') is '':
      cv = Curriculum(
           nombres = self.request.get('nombres'),
           apellidos = self.request.get('apellidos'),
           nacionalidad = self.request.get('nacionalidad'),
           #fecha_nacimiento = self.request.get('fecha_nacimiento'),
           email = self.request.get('email')
           )
    else:
      cv = db.get(self.request.get('key'))
      cv.nombres = self.request.get('nombres')
      cv.apellidos = self.request.get('apellidos')
      cv.nacionalidad = self.request.get('nacionalidad')
      timestring = self.request.get('fecha_nacimiento')
      #time_format = "%Y-%m-%d %H:%M:%S"
      #fecha_nacimiento = datetime.datetime.fromtimestamp(time.mktime(time.strptime(mytime, time_format)))

      #cv.fecha_nacimiento = fecha_nacimiento
      cv.email = self.request.get('email')
    cv.put()
    self.redirect('/cv')

class NotFoundHandler(webapp.RequestHandler):
  def get(self):
    temp = os.path.join(os.path.dirname(__file__),'templates/404.html')
    outstr = template.render(temp,{})
    self.response.out.write(outstr)

def main():
  application = webapp.WSGIApplication([
		(r'/cv',MainHandler),
		(r'/cv/editar',EditarHandler),
		],debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
