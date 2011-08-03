from google.appengine.ext.webapp.util import run_wsgi_app

from routing import WSGIRouter
from blog import BlogHandler
from index import MainHandler

router = WSGIRouter()

router.connect("/", MainHandler)
router.connect("/blog", BlogHandler)


def main():
        run_wsgi_app(router)

if __name__ == '__main__':
        main()
