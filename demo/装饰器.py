from functools import wraps


# 用装饰器声明一个单例
def singleton(cls, *args, **kw):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    ...


c1 = MyClass()
c2 = MyClass()

print(id(c1), id(c2))


# wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
def fun(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        print(1)
        fn()
        print("2")

    return decorator


@fun
def sayHi(name='bob'):
    print("hi", name)


def logit(logofile='out.log'):
    def login_decorator(fn):
        @wraps(fn)
        def wraps_function(*args, **kwargs):
            logstr = fn.__name__ + 'was called'
            print(logstr)
            with open(logofile, 'a') as openfile:
                openfile.write(logstr + '\n')
            return fn(*args, **kwargs)

        return wraps_function

    return login_decorator


@logit()
def testLog():
    pass


if __name__ == '__main__':
    # sayHi()
    # print(sayHi.__name__)
    testLog()
