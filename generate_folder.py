import os 
def generate_folders(problems_str):
    '''generate_folder.py파일이 있는 위치에 백준코딩 문제 폴더 생성 함수 
    
    Args: 
        problems_str (str): whitespace로 구분된 백준 문제 번호 스트링
    Returns:
        None
    '''
    problems_list = problems_str.split()
    path_root = os.getcwd()
    for num in problems_list:
        os.mkdir(os.path.join(path_root, num))


if __name__ == '__main__':
    problems_str = '''2557
    10869
    2588
    9498
    2753
    1085
    2739
    10950
    2438
    10871
    2562
    8958
    4344
    2577
    15596
    11654
    2675
    1152
    2908
    2869
    1978
    9020
    1065
    2628
    10872
    1914
    9663
    1074
    2750
    2751
    10989
    1181
    2309
    10819
    10971
    2468'''
    generate_folders(problems_str)
