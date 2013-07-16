#coding:utf8
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack
import redis
import json

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

def getRedis():
    top = _app_ctx_stack.top
    if not hasattr(top, 'rserver'):
        rserver = redis.Redis("localhost")
        top.rserver = rserver
    return top.rserver
@app.teardown_appcontext
def closeRedis(exception):
    top = _app_ctx_stack

@app.route('/getVideo')
def getVideo():
    uid = request.args.get('uid', 0, type=int)
    rid = request.args.get('rid', 0, type=int)
    rserver = getRedis()

    #视频没有被请求生成过
    videoId = 'video.%d.gen' % (rid)
    ret = rserver.getset(videoId, 1)
    if ret == None:
        rserver.publish('getVideo', json.dumps([uid, rid]) )

    #视频已经生成成功了
    ret = rserver.get('video.%d.ok'%(rid))
    ok = False
    if ret != None:
        ok = True

    return json.dumps(dict(code=1, ok=ok))
        
"""
@app.route('/checkVideo')
def checkVideo():
    uid = request.args.get('uid', 0, type=int)
    rid = request.args.get('rid', 0, type=int)
    rserver = getRedis()
    sub = rserver.pubsub()
    sub.subscribe('saveVideo.%d'%(rid))
    data = None
    for item in sub.listen():
        print "item is", item
        if item['type'] == 'message':
            data = item['data']
            break
    print "checkVideo", data
    return data
"""

@app.route('/')
def index():
    return 'helloWorld'
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
