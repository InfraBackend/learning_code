# -*- coding: utf-8 -*-
from kombu import Queue


# 定义任务队列
CELERY_QUEUES = (
    Queue('default', routing_key='task.#'),  # 路由键以task开头的都进入此队列
    Queue('web_tasks', routing_key='web.#')
)

CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'

CELERY_ROUTES = {
    'projq.tasks.add':{
        'queue': 'web_tasks',
        'routing_key': 'web.add',
    }
}

# 启动： celery -A projq worker -Q web_tasks -l info
# 只执行web_tasks 中的任务