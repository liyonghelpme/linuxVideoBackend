#coding:utf8
"""
检查是否有生成视频请求
如果有则执行程序生成视频
最后合并视频
将消息发送到publish 出去 但是如果用户没有在线监听则用户无法得到数据

视频的3个状态：在getVideo 接口

未请求过
已经请求正在生成
已经生成
"""
import redis
import json
import os
rserver = redis.Redis('localhost')
pubsub = rserver.pubsub()
pubsub.subscribe(['getVideo'])
for item in pubsub.listen():
    if item['type'] == 'message':
        print "read message", item
        data = json.loads(item['data'])
        uid = data[0]
        rid = data[1]
        #启动视频录制 启动cocos2d 程序 录制结束才能 开始下一个视频
        os.system('../cocos2dLibavLinux/proj.linux/bin/debug/HelloCpp')
        os.system('sh merge.sh %d' % (rid))
        #监听这个视频的对象得到通知 获取视频
        rserver.publish('saveVideo.%d'%(rid), json.dumps(rid))
        #标记视频已经生成了
        rserver.set("video.%d.ok" % (rid), 1)
        print "finish record video and audio"
    
    

    
