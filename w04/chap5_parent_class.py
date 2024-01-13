class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# is a 관계 : 자식이 특성을 물려받는 구조
class Animal:
    def __init__(self) -> None:
        self.__move: bool = True
        self.__eat: bool = False


    def is_move(self) -> bool:
        if self.__move == True:
            return True
        return False

    def is_eat(self) -> bool:
        if self.__eat == True:
            return True
        return False



# has a 관계 : 완제품 만들 때 부품 클래스를 포함하는 관계 / 클래스 안에 클래스 객체를 생성해서 사용하는 관계
class Bullet: #총알 관련 기능만 구현
    def __init__(self, count):
        self.__count = count

    def incre(self):
        self.__count += 1

    def decre(self):
        self.__count -= 1

    def rotate(self):
        print('회전한다.')

    def set_count(self, cnt):
        self.__count = cnt

    def get_count(self):
        return self.__count

# 총이 총알을 소비하는거니까. 총 안에 캡슐화 해준다!
class Gun: # 발사, 재장전
    def __init__(self):
        self.__bullet__ = Bullet(12)

    def reroad(self, count) -> None:
        self.__bullet__.set_count(count)

        # 아래와 같이 작성하면 객체가 하나 더 생성되는 것임. 따라서 set_count를 생성함!
        # self.__bullet__.__init__(12)

    def shot(self) -> None:
        self.__bullet__.decre()
        if self.__bullet__.get_count() < 0:
            return
        elif self.__bullet__.get_count() == 0:
            print('재장전 필요')
            return
        print('발사!')

class Food:
    def __init__(self):
        self.eating = ''







if __name__ == '__main__':
    gun = Gun()
    for i in range(13):
        gun.shot()


