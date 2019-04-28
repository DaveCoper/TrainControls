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
    def __init__(self, train):
        self.train = train

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return "hello"

    def POST(self):
        return "hello"

    def PUT(self, data):
        pass

    def DELETE(self):
        self.train.Speed(0)


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
    webapp.train = TrainControler('train')
    cherrypy.quickstart(webapp, '/', conf)