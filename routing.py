import re

var_regex = re.compile('\{(\w+)(?::([^}]+))?\}')


def template_to_regex(template):
        regex = ''
        last_pos = 0
        for match in var_regex.finditer(template):
                regex += re.escape(template[last_pos:match.start()])
                var_name = match.group(1)
                expr = match.group(2) or '[^/]+'
                expr = '(?P<%s>%s)' % (var_name, expr)
                regex += expr
                last_pos = match.end()
        regex += re.escape(template[last_pos:])
        regex = '^%s$' % regex
        return regex


class WSGIRouter(object):
        def __init__(self):
                self.routes = []

        def __call__(self, environ, start_response):
            for regex, handler, kwargs in self.routes:
                match = regex.match(environ['PATH_INFO'])
                if match:
                    environ['router.args'] = dict(kwargs)
                    environ['router.args'].update(match.groupdict())
                    return ['TEST']  # environ,start_response)

        def connect(self, template, handler, **kwargs):
                """ Connects URLs matching a template to a handler application.

                :param template:
                        A template string, consisting of literal text and
                        template expressions of the form {label[: regex ]},
                        where label is the mandatory name of the expression,
                        and regex is an optiones regular expression.

                :param handler:
                    A WSGI application to execute when the template is matched.
                """

                route_re = re.compile(template_to_regex(template))
                self.routes.append((route_re, handler, kwargs))
