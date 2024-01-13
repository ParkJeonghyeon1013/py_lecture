#!/usr/bin/python
#encoding=utf-8


'''
r: read
w: write
a: append
'''

# 경로를 입력 해당 파일 리스트를 보여주는 스크립트
# 1. 스탠다드 모듈
# 2. 써드파티 모듈
# 3. 본인이 작성한 모듈

import re
import sys
import pathlib

# ok 라는 단어가 있는 파일의 내용을 본인 홈 디렉토리의
# result.txt라는 파일 이름으로 해당 내용을 write
#
# open('path', 'w')
# pathlib.Path.home()
#   : 본인의 홈디렉토리 경로 반환하는 함수
#       ex) home = pathlib.Path.home()
#           home.as_posix()
#
def get_path():
    home = pathlib.Path.home()
    home_path = '{0}/{1}'.format(home.as_posix(), 'result.txt')
    count = 0
    try:
        s_path = pathlib.Path(sys.argv[1])
        for i in s_path.glob('**/*.txt'):
            print(i)
            if count > 5:
                break
            with open(i.as_posix(), 'r') as fp:
                # fp.readlines() --> list
                try:
                    for rl in fp.readlines():
                        res = re.search(r'\s?(ok)\s+', rl)
                        # ok 단어를 못찾았다면,
                        if res is None:
                            continue
                        with open(home_path, 'a') as fp2:
                            fp2.write('{0}: {1}'.format(i.as_posix(), rl))
                except UnicodeDecodeError as err:
                    pass
    except IndexError as err:
        sys.stderr.write('index가 잘못됨')


get_path()
