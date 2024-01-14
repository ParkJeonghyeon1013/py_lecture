'''
import functools

def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)      # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b):
            r = func(a, b)

            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수이다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아니다.'.format(func.__name__, x))
            return r

        return wrapper
    return real_decorator

# 함수의 결과값이 5의 배수인지 알려줌
@is_multiple(5)
def add_func(a,b):
    return a+b

    # 함수의 결과값이 10의 배수인지 알려줌.
@is_multiple(10)
def mult_func(x,y):
    return x*y

add_func(2,6)
mult_func(2,5)

'''

'''
# 함수 이름을 불러올 때 잘 안불러지는 경우가 있음.
def deco_ss(func):
    def wrapper(a,b):
        res = func(a,b)
        print('func: {0}, result {1} '.format(func.__name__, res))
        return res
    return wrapper

# 함수 이름 불러올 때 내장함수인 __name__ 사용한다
@deco_ss
def testfunc(a,b):
    return a+b

testfunc(1,6)

'''



'''

# 클래스 기반의 데코레이터

import functools
def deco(func):
    @functools.wraps(func) # 함수 이름을 받아올때 써두면 좋다! 혹시 모르는 호환을 위해
    def wrapper(a,b):
        print(func.__name__, '[function]: func start')
        func()
        print(func.__name__, '[function]: func end')
    return wrapper

# deco를 매개변수를 받을 수 있도록 바꿔보자
def deco_2(x):
    def real_decorator(func):
        def wrapper(*args,**kwargs):

            print(func.__name__, '[function]: func start')
            func(x * 10)
            print(func.__name__, '[function]: func end')
        return wrapper
    return real_decorator

@deco_2(55)
def test_func(a):
    print('args: ', a)


test_func(1)
print('-'*100)


class Trace:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print(self.__func.__name__, '[class]: func start')
        self.__func()
        print(self.__func.__name__, '[class]: func end')

@Trace
def hello():
    print('hello')

@deco
def bye():
    print('bye')

@Trace
def use_Trace(a=5, b=10):
    return a + b

hello()
bye(2,6)
use_Trace()


'''

# 함수 기반 인자값 있는 데코레이터
def args_deco(x):
    def mult(func):
        def wrapper(a,b):
            res = func(a + b) * x
            return res
        return wrapper
    return mult

class Trace:
    def __init__(self, func):
        self.func = func
    def __call__(self, a,b):
        r = self.func(a,b)
        return r

@Trace
def add(a,b):
    return a+b

print(add(5,10))

class Trace2:
    def __init__(self, x):
        self.__x = x
    def __call__(self, func):
        def wrapper(a,b):
            r = func(a,b) * self.__x
            return r
        return wrapper

@Trace2(10)
def add2(a,b):
    return a+b
print(add2(5, 10))