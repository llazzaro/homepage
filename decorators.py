from google.appengine.ext.webapp import template
import os
import yaml
import logging

# decorators
class templateSelector(object):
    def __init__(self, template):
        """
            If there are decorator arguments, the function
            to be decorated is not passed to the constructor!
        """
        self.template = template
        options_file = open('options.yml')
        self.options =  yaml.load(options_file)
        options_file.close()

    def __call__(self, f):
        """
            If there are decorator arguments, __call__() is only called
            once, as part of the decoration process! You can only give
            it a single argument, which is the function object.
        """
        def wrapped_f(*args, **kwargs):
            temp = os.path.join(os.path.dirname(__file__), self.template)
            response, template_data = f(*args)
            template_data['host'] = args[0].request.host_url
            template_data['disqus_shortname'] = self.options['disqus_shortname']
            outstr = template.render(temp, template_data)
            response.out.write(outstr)
        
        return wrapped_f

#def selectorTemplate(method,tempplate):
#  temp = os.path.join(os.path.dirname(__file__),template)
#  outstr = template.render(temp,{
#                   'nombre_seccion':nombre_seccion,
#                   'texto_seccion':texto_seccion,'path':path})
#  self.response.out.write(outstr)
