import os,functools
import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
from models import *
from decoradores import selectorTemplate
import logging

#def selectorTemplate(func,template):
#  temp = os.path.join(os.path.dirname(__file__),template)
#  outstr = temp.render(temp,func)
#  self.response.out.write(outstr)


class MainHandler(webapp.RequestHandler):
 
  @selectorTemplate('templates/fotos/fotos.html')
  def get(self):
    path = self.request.path
    nombre_seccion = self.getSeccion(path)
    texto_seccion = "texto seccion"
    admin = users.is_current_user_admin()
    galerias = db.Query(Galeria).order('-creada').fetch(limit=10)
    return self.response,{'nombre_seccion':nombre_seccion,'texto_seccion':texto_seccion,'path':path,'admin':admin,'galerias':galerias}

  def getSeccion(self,path):
    return { 
		'/index':  'Inicio',
		'/cv':'Curriculum Vitae',
		'/about':'Acerca de',
		'/projects':'Proyectos',
		'/blog':'Blog',
		'/fotos':'Fotos',
	}[path]

#class GaleriaHandler(webapp.RequestHandler):
#  def get(self):
#    pass

class AdminHandler(webapp.RequestHandler):
  @selectorTemplate('templates/fotos/admin.html')
  def get(self):
    galerias = db.Query(Galeria).order('-creada').fetch(limit=10)
    return self.response,{'galerias':galerias}

class FotoHandler(webapp.RequestHandler):
  @selectorTemplate('templates/fotos/nueva_foto.html')
  def get(self):

    foto = None
    galeria = db.get(self.request.get('galeria'))
    if self.request.get('key'):
      foto = db.get(self.request.get('key'))

    return self.response,{'foto':foto,'galeria':galeria}

  def post(self):
    galeria = db.get(self.request.get('galeria'))
    if self.request.get('key') is '':
      foto = Foto(
                nombre = self.request.get('nombre'),
                descripcion = self.request.get('descripcion'),
                link = self.request.get('link'),
		galeria = galeria,
            )
    else:
      foto = db.get(self.request.get('key'))
      foto.descripcion = self.request.get('descripcion')
      foto.nombre = self.request.get('nombre')
      foto.borrador = bool(self.request.get('borrador'))

    foto.put()
    self.redirect('/fotos/galeria?key='+self.request.get('galeria'))

class GaleriaHandler(webapp.RequestHandler):
  @selectorTemplate('templates/fotos/nueva_galeria.html')
  def get(self):

    galeria = None
    if self.request.get('key'):
      galeria = db.get(self.request.get('key'))

    return self.response,{'galeria':galeria}

  def post(self):
    if self.request.get('key') is '':
      galeria = Galeria(
                nombre = self.request.get('nombre'),
                descripcion = self.request.get('descripcion'),
                borrador = bool(self.request.get('borrador'))
            )
    else:
      galeria = db.get(self.request.get('key'))
      galeria.descripcion = self.request.get('descripcion')
      galeria.nombre = self.request.get('nombre')
      galeria.borrador = bool(self.request.get('borrador'))

    galeria.put()
    self.redirect('/fotos/admin')


class NotFoundHandler(webapp.RequestHandler):
  def get(self):
    temp = os.path.join(os.path.dirname(__file__),'templates/404.html')
    outstr = template.render(temp,{})
    self.response.out.write(outstr)

class VistaGaleriaHandler(webapp.RequestHandler):
  @selectorTemplate('templates/fotos/galeria.html')
  def get(self):
    if self.request.get('key'):
      galeria = db.get(self.request.get('key'))
      #fotos = db.Query(Foto).filter('galeria=',galeria)
      admin = users.is_current_user_admin()
    return self.response,{'galeria':galeria,'admin':admin}

def main():
  application = webapp.WSGIApplication([
		(r'/fotos',MainHandler),
		(r'/fotos/galeria/?',VistaGaleriaHandler),
		(r'/fotos/admin',AdminHandler),
		(r'/fotos/admin/galeria_nueva',GaleriaHandler),
		(r'/fotos/admin/editar/galeria/editar/?',GaleriaHandler),
                (r'/fotos/admin/foto_nueva/?',FotoHandler),
		],debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
