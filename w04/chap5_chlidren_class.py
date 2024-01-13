import chap5_parent_class

class MoreFourCal(chap5_parent_class.FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

# is a 관계 : 자식이 특성을 물려받는 구조
class People(chap5_parent_class.Animal):
    def __init__(self):
        # super().__init__()
        chap5_parent_class.Animal.__init__(self)
        self.__cloth: bool = True

    def is_cloth(self) -> bool:
        if self.__cloth == True:
            return True

class Dog(chap5_parent_class.Animal):
    def __init__(self):
        # super().__init__()
        chap5_parent_class.Animal.__init__(self)
        self.__tail: bool = True
    def is_tail(self) -> bool:
        if self.__tail == True:
            return True
        return False



a = MoreFourCal(4,2)
print(a.pow())
print(a.add())

p = People()
dog = Dog()

print(p.is_move())
print(p.is_eat())
print(p.is_cloth())

print('-'*100)

print(dog.is_move())
print(dog.is_eat())
print(dog.is_tail())
