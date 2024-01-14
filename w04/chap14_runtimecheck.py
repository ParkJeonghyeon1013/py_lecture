from functools import wraps
from time import time, gmtime


def runtime_check(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        start_time = time()
        s_time = gmtime(start_time)
        print('( {0} ) Start Time: {1}/{2} - {3}:{4}:{5}'.format(
            func.__name__, s_time.tm_mon, s_time.tm_mday, s_time.tm_hour + 9, s_time.tm_min, s_time.tm_sec))
        func_result = func(*args, **kwargs)
        end_time = time()
        e_time = gmtime(end_time)
        print('( {0} ) End Time: {1}/{2} - {3}:{4}:{5}'.format(
            func.__name__, e_time.tm_mon, e_time.tm_mday, e_time.tm_hour + 9, e_time.tm_min, e_time.tm_sec))
        run_time = end_time - start_time
        print('( {0} ) Running Time: {1}m {2}s'.format(
            func.__name__, int(run_time // 60), int(run_time % 60)))
        return func_result

    return __wrapper


def runtime_check_with_param(param):
    def wrapper(func):
        @wraps(func)
        def __wrapper(*args, **kwargs):
            start_time = time()
            s_time = gmtime(start_time)
            print('( {0} ) Start Time: {1}/{2} - {3}:{4}:{5}'.format(
                param, s_time.tm_mon, s_time.tm_mday, s_time.tm_hour + 9, s_time.tm_min, s_time.tm_sec))
            func_result = func(*args, **kwargs)
            end_time = time()
            e_time = gmtime(end_time)
            print('( {0} ) End Time: {1}/{2} - {3}:{4}:{5}'.format(
                param, e_time.tm_mon, e_time.tm_mday, e_time.tm_hour + 9, e_time.tm_min, e_time.tm_sec))
            run_time = end_time - start_time
            print('( {0} ) Running Time: {1}m {2}s'.format(
                param, int(run_time // 60), int(run_time % 60)))
            return func_result

        return __wrapper

    return wrapper

num = 100000000

@runtime_check((num,))
def func1():
    res = ''
    for i in range(num):
        res += str(i)
    return res

print('-'*100)

@runtime_check((num,))
def func2():
    lst = []
    for i in range(num):
        lst.append(str(i))
    return ''.join(lst) #join 을 통한 문자열 더하기는 속도가 더 빠르다

f1 = func1()
f2 = func2()

# print(f1)
# print(f2)

