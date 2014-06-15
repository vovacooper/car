__author__ = 'vovacooper'

import redis

redis_kv = redis.StrictRedis(host='localhost', port=6379, db=0)


########################################################################################################################
if __name__ == "__main__":
    print(redis_kv.set('foo', 'bar'))
    print(redis_kv.get('foo'))
    print(redis_kv.get('bar'))


