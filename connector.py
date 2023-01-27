import time
import redis

import driver

cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


def start():
    hardware = driver()
    message = ''
    # result = hardware.read()
    # message = procesar(result)
    return {
        'status': True,
        'message': message
    }
