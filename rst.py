import os

from docutils.core import publish_parts
from google.appengine.ext import webapp


register = webapp.template.create_template_register()

@register.filter(name='rst2html')
def rst2html(s):
  settings = {'config': None}
  
  os.environ['DOCUTILSCONFIG'] = ""
  parts = publish_parts(source=s, writer_name='html4css',settings_overrides=settings)

  return parts['fragment']
