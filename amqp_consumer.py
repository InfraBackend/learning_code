# -*- coding: utf-8 -*-
import pika


# 处理接收到消息的回调函数
def on_message(channel, method_frame, header_frame, body):
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    print(body)
parameters = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')
# 消息代理
connection = pika.BlockingConnection(parameters)
# 获得信道
channel = connection.channel()
# 声明交换机
channel.exchange_declare(exchange='web_develop', exchange_type='direct',
                         passive=False, durable=True, auto_delete=False)
# 声明队列
channel.queue_declare(queue='standard', auto_delete=True)
# 将队列和交换机绑定
channel.queue_bind(queue='standard', exchange='web_develop', routing_key='routing_key')
# 订阅队列
channel.basic_consume(on_message, 'standard')
# 开始消费
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()