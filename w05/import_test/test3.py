
import site
site.addsitedir('/home/rapa/git_workspace/py_lecture/w05')

from module_test import *
# * 사용해서 import 할 때 init 파일안에 __all__ 안에 리스트로 사용할 모듈 적어줄것!

print('@@@ name: ', __name__)


# 하위 디렉토리를 가져올때는 아래와 같은 두 가지 방식이 가능함.
from module_test.games import item
import module_test.games.item as games

item.testfunc()

