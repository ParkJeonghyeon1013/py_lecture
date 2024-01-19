# ~/git_workspace/py_lecture/w05/import_test

import sys

sys.path.insert(
    0,
    '/home/rapa/git_workspace/py_lecture/w05/module_test'
)

print(sys.path) # 경로 확인

import module1 #module_test로가서 sys.path에 넣고 module1이 있으면 import 해줘라는 뜻

print(dir(module1))
print(module1.add(1,2))