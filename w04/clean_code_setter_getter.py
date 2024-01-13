class People:
    def __init__(self):
        self.__name: str = ''
        self.__age: int = 0

    @property
    def info(self) -> tuple:
        return (self.__name, self.__age)

    @info.setter
    def info(self, info: tuple) -> None:
        # 제대로 된 은닉을 위해 값을 확인하는 과정 거침.
        # name : 최대 8
        # age 1~80

        if len(tuple[0]) > 8:
            print('이름은 8자리를 초과할 수 없습니다.')
            return
        if info[1] < 1 or info[1] > 80:
            print('나이는 1~80')
            return

        self.__name = tuple[0]
        self.__age = tuple[1]

p = People()
# p.info = (이름, 나이)

p.set_info('name', 22)

