#제너레이터 - 이터레이터를 만드는 함수

def season_generator(*args):
    for arg in args:
        yield arg               #처음 __next__ 호출시 첫번째 yield 값 반환 후 잠시 지연.
                                #반환할 것이 없을 경우 자동으로 stopiteration 에러 raise

g = season_generator('spring','summer','autumn','winter')

# print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


def func():

    print('1번 작업중')
    yield 1                 #return과 yield 다른점 - 작업중 return시 작업종료 / yield 는 일시 중지

    print('2번 작업중')
    yield 2
    
    print('3번 작업중')
    yield 3

    print('4번 작업중')
    yield 4

ge = func()
data = ge.__next__()
print(data)

data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)

