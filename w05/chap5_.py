#filter 함수의 정체! / lambda랑 같이 많이 사용됨
def filter_func(x):
    if x > 10:
        return False
    return True

for i in range(10):
    if filter_func(i):
        print(i)

result = filter(filter_func, range(15)) # 0~10까지 나옴
print(f'result = {result}')
result1 = filter(lambda x: x<=10, range(15))
print(f'result1 = {result1}')

print('-'*30)

# all() any() 함수의 정체
lst = [True, False, True]

def all_func(lst):
    flag = True
    for i in lst:
        flag = flag and i
    return flag

print(all(lst))
print(all_func(lst))

print('-'*30)

# map()
lst = [[1,2], [3,4], [5,6]]
result2 = list(map(lambda x: x[0] + x[1], lst))

print(result2)

print('-'*30)

#random 함수 // start ~ stop 미만
import random

lst= []
for i in range(10):
    lst.append(random.randrange(10))

print(lst)
lst.sort()
print(lst, '이런 방식은 메모리 많이 잡아먹음.')
print('그래서 sorted를 사용해줌.')

so = sorted(lst)
print(type(so), so)


print('-'*30)

# zip 함수를 사용해보자. 함수랑도 묶을 수 있는게 신기해!
def a_func(a,b):
    print(a,b)

def b_func(a,b):
    print(a,b)

result = zip([a_func, b_func], range(3), range(10,20))
print(result)
result_lst = list(result)
print(result_lst)
print()
for f, p1, p2 in result_lst:
    a = f(p1, p2)
    print(a,'\n')



