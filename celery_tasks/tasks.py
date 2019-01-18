from __future__ import absolute_import

import time

from circulation.celery import app


@app.task(name='test')
def test(num):
    for i in range(1000):
        time.sleep(1)
        print(num + i)
    return 'ok'
