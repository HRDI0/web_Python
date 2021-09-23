#미니 프로젝트 블로그 만들기.
import os
import csv
import menu
from post import Post

version = 1.0

file_path = "./requests_1/studing_web/miniproject_blog/data.csv"

post_list = []

#data.csv 파일이 있다면
if os.path.exists(file_path):
    #게시글 로드
    print("게시글 로딩중")
    f = open(file_path, 'r', encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]),data[1],data[2],int(data[3]))
        post_list.append(post)
else:
    #data.csv 파일이 없다면
    f = open(file_path,"w", encoding="utf8", newline='')
    f.close()

while True:
    print("\n\n - mini blog - ")
    print("메뉴")
    print("1. 게시글 작성")
    print("2. 게시글 목록")
    print("3. 블로그 나가기")
    try:
        commend = int(input('메뉴 번호 : '))
    except ValueError:
        print('올바른 메뉴 번호를 입력해주세요.')       #숫자이외 입력 예외처리
    else:
        if commend == 1:
            post_list.append(menu.post_write(post_list))
            input('\n엔터키를 눌러 다음으로 진행하세요...')    
        elif commend == 2:
            post_list = menu.post_load(post_list)
            input('\n엔터키를 눌러 다음으로 진행하세요...')
        elif commend == 3:
            print('이용해주셔서 감사합니다.')
            menu.save_data(file_path,post_list)
            exit()
        else:                                          #없는 카테고리 선택 예외처리
            print('정확한 카테고리 번호를 입력해주세요.')