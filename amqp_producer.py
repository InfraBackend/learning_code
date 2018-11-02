# -*- coding: utf-8 -*-
import sys
import pika


parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
# 消息代理
connection = pika.BlockingConnection(parameters)
# 获得信道
channel = connection.channel()
# 声明交换机
channel.exchange_declare(exchange='web_develop', exchange_type='direct',
                         passive=False, durable=True, auto_delete=False)
if len(sys.argv) != 1:
    msg = sys.argv[1]
else:
    msg = 'haha'

# 创建一个消息
props = pika.BasicProperties(content_type='text_plain')
# 发送给交换机
channel.basic_publish('web_develop', 'routing_key', msg, properties=props)
connection.close()
