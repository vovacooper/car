__author__ = 'vovacooper'

import exceptions
from redis_kv import redis_kv
import json
import hashlib
########################################################################################################################

CASH_TTL = 1000

########################################################################################################################
'''
Usage:
@cash       #ttl is 1000 ms
@cash(ttl)  #ttl is an integer representing Time To Live in ms
'''


def cash(ttl):
    def cashed(func):
        def make_hash(d):
            str_key = json.dumps(d, sort_keys=True)
            md5 = hashlib.md5()
            md5.update(str_key)
            return md5.hexdigest()

        def is_cashed(self, key):
            """
            cash Decorator

            key - Dictionary

            if key is in cash then return from cash
            else return new val and add to cash
            """
            if type(key) is not dict:
                raise TypeError("the key must be a dict")

            hash_key = make_hash(key)

            if redis_kv.exists(hash_key):
                print("returning from cash")
                return redis_kv.get(hash_key)

            print("adding to cash")
            value = func(self, hash_key)
            redis_kv.set(hash_key, value, px=ttl)

            return value
        return is_cashed
    if callable(ttl):
        f = ttl
        ttl = CASH_TTL
        return cashed(f)
    return cashed

########################################################################################################################
#Example


class DecTest:
    def __init__(self):
        return

    @cash(10000)
    def get_val(self, key):
        return "value is " + key


class DecTestM(DecTest):
    #@cashed
    def get_val(self, key):
        return DecTest().get_val(key)

########################################################################################################################
if __name__ == "__main__":

    dec_test = DecTest()
    for x in range(0, 2):
        print(dec_test.get_val({"b": x}))
    for x in range(0, 2):
        print(dec_test.get_val({"b": x}))

    dec_test = DecTestM()
    for x in range(0, 2):
        print(dec_test.get_val({"b": x}))
    for x in range(0, 2):
        print(dec_test.get_val({"b": x}))




