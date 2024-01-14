'''

# trace의 func에는 데코레이터로 감싼 함수의 이름이 들어감.
def trace(func):
    print(func)
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 종료\n')
    return wrapper

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

hello()
world()

'''




'''

def cus_deco(func):
    print('연산시작')
    func(2,3)
    print('연산종료\n')

def cus_func(a,b):
    print('result:', a+b)


def cus_func2(a, b):
    print('result:', a - b)


cus_deco(cus_func) # 얘네는 동작 되고
cus_deco(cus_func2)

cus_deco(cus_func()) # 얘는 안됨. 괄호 여부 차이에 따라서 뭐가 다른거지?
# 변수처럼 사용하기 위해서 데코레이터를 사용하는것인가?

'''




'''

# cus_deco는 데코레이터에 의해서 아래의 함수를 전달받는다
def cus_deco(func):
    def wrapper(a,b):
        print('연산시작')
        func(a,b)
        print('연산종료\n')
    return wrapper

@cus_deco
def cus_func(a,b):
    print('result:', a + b)

@cus_deco
def cus_func2(a, b):
    print('result:', a - b)

cus_func(7, 5)
cus_func2(7, 5)



'''



'''
# 가변인수함수 데코레이터
def cus_deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print('result : ', res)
        return res
    return wrapper # return 시 wrapper 함수가 실행되는 것!!!!!!!! 결과적으로 wrapper의 결화값이 들어감.

@cus_deco
def cus_func(*args: tuple):
    result = 0
    for i in args:
        result += i
    return result

@cus_deco
def cus_func2(**kwargs: dict):
    x_val = kwargs['x']
    y_val = kwargs['y']
    return x_val + y_val


final_res = cus_func(7, 5)
final_res2 = cus_func2(x=7, y=5)

print(final_res)
print(final_res2)
'''

'''

# 매개변수 있는 데코레이터
# 결과값에 5가 곱해지는 매개 변수가 있는 데코레이
def cus_deco(x):
    def mult_val(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs) * x
            print('result : ', res)
            return res
        return wrapper
    return mult_val # return 시 wrapper 함수가 실행되는 것!!!!!!!! 결과적으로 wrapper의 결화값이 들어감.

@cus_deco(5)
def cus_func(*args: tuple):
    result = 0
    for i in args:
        result += i
    return result

@cus_deco(5)
def cus_func2(**kwargs: dict):
    x_val = kwargs['x']
    y_val = kwargs['y']
    return x_val + y_val


final_res = cus_func(7, 5)
final_res2 = cus_func2(x=7, y=5)

print(final_res)
print(final_res2)
'''



# 여러개 데코레이터가 있는 데코레이터

def deco_dual(func):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        return wrapper
    return deco_dual

def cus_deco(x):
    def mult_val(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs) * x
            print('result : ', res)
            return res
        return wrapper
    return mult_val # return 시 wrapper 함수가 실행되는 것!!!!!!!! 결과적으로 wrapper의 결화값이 들어감.

@deco_dual
@cus_deco(5)
def cus_func(*args: tuple):
    result = 0
    for i in args:
        result += i
    return result

@deco_dual
@cus_deco(5)
def cus_func2(**kwargs: dict):
    x_val = kwargs['x']
    y_val = kwargs['y']
    return x_val + y_val


final_res = cus_func(7, 5)
final_res2 = cus_func2(x=7, y=5)

print(final_res)
print(final_res2)