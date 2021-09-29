# 이터레이터 객체 - 리스트, 튜플, 문자열, 딕셔너리, range 객체

#__iter__ - iterator 메소드
#__next__ - iterator 동작 메소드

class season:
    def __init__(self):
        self.season_list = ['spring', 'summer', 'autumn', 'winter']
        self.idx = 0
        self.max_num = 4

    def __iter__(self):
        return self
    def __next__(self):
        if self.idx < self.max_num:
            curr_idx = self.idx
            self.idx += 1
            return self.season_list[curr_idx]
        else:
            raise StopIteration

# for i in season():
#     print(i)

season_obj = season().__iter__()        #iter 객체 생성
print(season_obj.__next__())            #iter 객체 하나 출력