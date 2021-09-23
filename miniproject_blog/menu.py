#메뉴 만들기
import csv
from post import Post

def post_write(post_list):
    print("\n")
    title = input('제목 : ')
    content = input('내용 : ')
    #post_list의 마지막 객체의 id +1 하여 id 번호 부여
    post = Post(int(post_list[-1].get_id()) + 1, title, content, 0) 
    return post

def post_load(post_list):
    print('\n\n게시글 로딩중...\n\n')

                            
    while True:
        id_list = []
        for pt in post_list:                #게시글 목록 확인
            print('글번호 : ',pt.get_id())
            print('제목 : ',pt.get_title())
            id_list.append(pt.get_id())
            print()
        try:                                #게시글 상세 확인
            id = int(input('원하는 글번호를 입력해주세요. (-1 입력시 종료)\n'))
        except ValueError:
            print('\n올바른 글번호를 입력해주세요.\n')    #숫자 이외 입력 예외처리
        else:
            if id == -1:
                break
            else:
                if id in id_list:
                    post_list = post_check(post_list,id)
                else:
                    print('\n정확한 글번호를 입력해주세요.\n')

        input('\n엔터키를 눌러 다음으로 진행하세요...\n')

    return post_list            #수정,삭제 되었거나 그대로인 게시물 리스트 반환

def post_check(post_list,id):
    for pt in post_list:
        if pt.get_id() == id:
            pt.add_view_count()
            post_list = post_change(pt,post_list)
    return post_list

def post_change(post,post_list):
    while True:
        print('\n글번호 : ',post.get_id())
        print('제목 : ',post.get_title())
        print('내용 : ',post.get_content())
        print('조회수 : ',post.get_view_count())
        print()
        try:
            commend = int(input('1. 수정  2. 삭제  (-1을 입력하면 메뉴로 돌아갑니다.)\n'))
        except ValueError:
            print('\n올바른 메뉴 번호를 입력해주세요.\n')   #예외처리
        else:
            if commend == 1:            #글수정
                title = input('제목 : ')
                content = input('내용 : ')
                post.set_post(post.get_id(),title,content,post.get_view_count())
            elif commend ==2:               #글삭제
                post_list.remove(post)
            elif commend == -1:
                print()
                return post_list
            else:
                print('\n정확한 메뉴 번호를 입력해주세요.\n')   #예외처리
    

def save_data(file_path,post_list):
    f = open(file_path,"w", encoding="utf8", newline='')
    writer = csv.writer(f)
    for pt in post_list:
        row = [pt.get_id(),pt.get_title(),pt.get_content(),pt.get_view_count()]
        writer.writerow(row)
    f.close()    