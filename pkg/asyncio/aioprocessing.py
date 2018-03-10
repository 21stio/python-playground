import asyncio
import datetime

import time

from beeprint import pp


def do():
    return get_abc()


def get_abc():
    time.sleep(1)
    return str(datetime.datetime.now())


loop = asyncio.get_event_loop()
tasks = [loop.run_in_executor(None, do), loop.run_in_executor(None, do), loop.run_in_executor(None, do)]

rs = loop.run_until_complete(asyncio.wait(tasks))
loop.close()


pp(list(rs[0]))
