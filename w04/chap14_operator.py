# 클래스 자체가 타입이 됨.
'''

class A:
    pass

a1 = A()
a2 = A()

# 객체를 생성하고 아래와 같은 계산을 하려고 하면 우리가 직접 정의를 해야 함.
# 오퍼레이트를 사용하는 이유가 아래와 같이 편하게 사용하기 위해서 임.
a3 = a1+ a2

'''

'''

class A:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        self.num += other.num
        return self #num 속성의 주소값이 넘어갈 수 있도록 self를 리턴해줌.

    def __sub__(self, other):
        self.num -= other.num
        return self

    def __eq__(self, other):
        return self.num == other.num

a1 = A(5)
a2 = A(7)

# a1 += a2
a3 = a1 + a2

# a1.__add__(a2)

print(a1.num)

# a3.__add__(a3, a1)

print(a1 == a2)

# 넌 뭐야.. 함수를 불러오지 않아도 되어서
a3 = A(8)
print(a1 == a3)

'''
class A:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        self.num += other.num
        return self #num 속성의 주소값이 넘어갈 수 있도록 self를 리턴해줌.

    def __sub__(self, other):
        self.num -= other.num
        return self

    def __eq__(self, other):
        return self.num == other.num

a1 = A(5)
a2 = A(7)

# a1 += a2
a3 = a1 + a2

# a1.__add__(a2)

print(a1.num)

# a3.__add__(a3, a1)

print(a1 == a2)

# 넌 뭐야.. 함수를 불러오지 않아도 되어서
a3 = A(8)
print(a1 == a3)
