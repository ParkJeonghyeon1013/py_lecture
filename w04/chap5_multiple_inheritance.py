# 죽음의 다이아몬드

class base_class:
    def __init__(self):
        print('BaseClass')


class a_class(base_class):
    def __init__(self):
        # base_class.__init__(self)
        super(a_class, self).__init__()
        print('a_Class')


class b_class(base_class):
    def __init__(self):
        # base_class.__init__(self)
        super(b_class, self).__init__()
        print('B_Class')


class Dervate_class(a_class, b_class):
    def __init__(self):
        # a_class.__init__(self)
        # b_class.__init__(self)
        super(Dervate_class, self).__init__()
        print('c_Class')

d = Dervate_class()