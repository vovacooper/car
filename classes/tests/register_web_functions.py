__author__ = 'lab_alglam'


class Ibs(object):
    web_func_dict = {}

    @classmethod
    def registerwebfunc(cls, *args):
        def decorator(fn):
            cls.web_func_dict[fn.__name__] = {'func': fn, 'args': args}
            return fn
        return decorator




'''
#Example
@Ibs.registerwebfunc("Asd", "asasasas")
def f():
    print("in f")

class v:
    @Ibs.registerwebfunc("Asd", "asasasas")
    def ff(self):
        print ("ff")


print(Ibs.web_func_dict)
'''