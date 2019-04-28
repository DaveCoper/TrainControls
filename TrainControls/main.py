import os, os.path
import string

import cherrypy

staticFilesDir = 'StaticFiles'

class RootControler(object):
    @cherrypy.expose
    def index(self):
        return open( os.path.join(staticFilesDir, 'Index.html'))


@cherrypy.expose
class TrainControler(object):    
    def __init__(self):
        self.text = 'hello'

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return self.text

    def POST(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        self.text = some_string
        return some_string

    def PUT(self, another_string):
        self.text = another_string

    def DELETE(self):
        self.text = 'hello'


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/train': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join( '.', staticFilesDir)
        }
    }

    webapp = RootControler()
    webapp.train = TrainControler()
    cherrypy.quickstart(webapp, '/', conf)