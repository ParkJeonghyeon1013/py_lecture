#!/usr/bin/python
#encoding=utf-8

import re
import sys
import pathlib

'''
--- method (기능)
* 홈 디렉토리 경로 반환하는 멤버 함수
* re 모듈 이용해 문자열 검색 멤버 함수 -> 특정 문자열이 있는지 없는지 판별
* 인자로 들어오는 경로와 데이터를 파일로 저장하는 멤버 함수

pep8: 클래스의 첫 글자는 대문자
이름 짓는 규칙 : 동사 + 명사
    ex) run_xxx
    ex) run_houdddi, run_maya
'''

class FileIO:
    def __init__(self, s_path: str) -> None:
        self.__s_path = pathlib.Path(s_path)
        # 컴파일 과정
        self.__pattern = re.compile(r'\s?(ok)\s+')


    def __del__(self) -> None:
        print('FileIO 객체가 메모리에서 제거되었습니다.')
        pass

    # 정적 멤버 함수 : 클래스 안에 속해 있지만 클래스 내부 함수와 큰 상호작용을 하지 않아 편의를 위해 들어간 함수.
    @staticmethod
    def get_home_path() -> pathlib.Path:
        """

        :return: home 디렉토리 경로 반환
        """
        return pathlib.Path.home()

    # TODO: gettter
    @property
    def s_path(self) -> pathlib.Path:
        return self.__s_path

    # TODO: setter
    @s_path.setter
    def s_path(self, s_path: pathlib.Path) -> None:
        """

        :param s_path: source path
        :return: None
        """

        # s_path 인자의 타입이 pahtlib.Path 인가
        # release 모드에서는 assert 키워드 무시되고 프로그램이 만들어짐
        assert isinstance(s_path, pathlib.Path)
        self.__s_path = s_path



    def is_found_str(self, s_str: str) -> bool:
        """

        :param f_str: found string, 찾을 문자열
        :return: 찾았으면 True
        """
        res = self.__pattern.search(s_str)
        return res is not None

    @staticmethod
    def save_file(dst_fpath: pathlib.Path, data: list) -> bool:
        """
        해당 파일이 없을 때에만
        :param dst_fpath: 최종으로 만들어질 파일 경로
        :param data: 파일에 저장할 리스트 데이터
        :return: boolean
        """

        # 속도 면에서 join 을 사용하는 것이 더 빠름
        # res = ''
        # for i in data:
        #     res += (i + '\n')


        if dst_fpath.exists():
            dst_fpath.unlink()
            return False
        with open(dst_fpath.as_posix(), 'a') as fp:
            fp.write('\n'.join(data))
        return True

    @property
    def get_lst_py(self) -> list[pathlib.Path]:
        """

        :return: source path의 모든 하위 디렉토리 검색 후
        확장자가 .py인 파일 경로를 반환
        """

        return list(self.__s_path.glob('**/*.py'))

    # def get_lst_py(self) -> list:
    #     chk_list = list(self.__s_path.glob('**/*.py'))
    #     if itme in chk_list: return list(self.__s_path.glob('**/*.py'))

    # __name__ == '__main__'
    # 파일 임포트할 때는 실행되지 않도록 하기 위함. 파일 실행 시 __main__ 이라고 바뀜. 그거 이용해서 실행.

    def get_found_str(self, lines: list) -> list[str]:
        """

        해당 메소드는 파일의 문자열들을 리스트로 받아서
        매칭되는 해당 라인의 문자열을 반환.
        :param lines:
        :param fstr:
        :return:
        """
        lst = []
        for rl in lines:
            if not self.is_found_str(rl):
                continue
            lst.append(rl)
        return lst

    # todo:
    def handler(self):
        found_lst = list()
        home_path = fio.get_home_path()
        for i in self.get_lst_py():
            with open(i.as_posix(), 'r') as fp:
                tmp = self.get_found_str(fp.readlines())
                if not len(tmp):
                    continue
                tmp = map(lambda x: '{0}: {1}'.format(i.as_posix(), x), tmp)
                tmp = list(tmp)
                found_lst.extend(tmp)

        FileIO.save_file(
            pathlib.Path('{0}/class_result.txt'.format(home_path.as_posix())),
            found_lst
        )



if __name__ =='__main__':
    fio = FileIO('/')

    fio.handler()

    # print(FileIO.get_home_path())
    # print()
    # print(fio.get_s_path())
    # print()

    print(fio.get_lst_py())

    # 한줄 길어지면 이와같은 방식으로 사용          / as_posix으로 string으로 바꿔줌.

    tmp = '{0}/file_io.txt'.format(FileIO.get_home_path().as_posix())

