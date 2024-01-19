# error custome 가능하닷!

class MyError(Exception):
    def __init__(self):
        print('my error class')

def raise_func():
    print('aaaaaaaa')
    raise MyError()
    print('bbbbbbb')

try:
    raise_func()
except MyError as err:
    print(err)