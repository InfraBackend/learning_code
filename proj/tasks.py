# -*- coding: utf-8 -*-
# 消息代理
BROKER_URL = ''
#任务结果
CELERY_RESULT_BACKEND = ''
# 序列化
CELERY_TASK_SERIALIZER = 'msgpack'   # msgpack是一个二进制的类json的序列化方案
CELERY_RESULT_SERIALIZER = 'json'
# 指定接收内容类型
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']






# 启动： celery -A proj worker -l info
