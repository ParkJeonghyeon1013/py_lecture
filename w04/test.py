import w04_setter_getter as w04

c1 = w04.Custom1()

print(c1.val)

c2 = w04.Custom2()

print(c2.val)

class People:
    def __init__(self):
        self.__name: str = ''
        self.__age :int = 0

    def get_name(self) ->str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age:int) -> None:
        self.__age = age