a = 1


def fun(a):
    print("func_in", id(a))  # func_in 41322472
    a = 2
    print("re-point", id(a), id(2))  # re-point 41322448 41322448


print("func_out", id(a), id(1))  # func_out 41322472 41322472
fun(a)
print(a)  # 1


# 单例
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1


# 2 共享属性
# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1
