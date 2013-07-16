#coding:utf8
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
import tornadoredis
import tornado.web
import tornado.gen
import json
import redis


from video import app

class CheckHandler(RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        rid = self.get_argument('rid')
        self.client = tornadoredis.Client()
        self.client.connect()
        self.rid = rid

        #视频已经生成好了 直接获取
        rserver = redis.Redis('localhost')
        ret = rserver.get('video.%s.ok' % (rid))
        print "checkHandler", ret
        if ret != None:
            self.write('ok')
            self.finish()
        else:
            yield tornado.gen.Task(self.client.subscribe, 'saveVideo.%s'%(rid))
            ret = self.client.listen(self.on_message)
    def on_message(self, msg):
        print "on_message", msg
        if msg.kind == 'message':
            self.write(str(msg.body))
            self.finish()
            self.client.unsubscribe('saveVideo.%s'%(self.rid))
        elif msg.kind == 'disconnect':
            self.write('connection disconnect')
            self.finish()
            
        
        
tr = WSGIContainer(app)

application = Application([
(r'/checkVideo', CheckHandler),
(r'.*', FallbackHandler, dict(fallback=tr)),
])


"""
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
"""
if __name__ == '__main__':
    application.listen(5000)
    IOLoop.instance().start()
