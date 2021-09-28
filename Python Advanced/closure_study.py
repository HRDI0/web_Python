# 1. 클로저
# 함수가 종료되어도 자원을 사용할 수 있다.
# 조건
# 내부 함수여야한다. (내부함수 - 함수 안에 다른 함수를 정의할수 있다.)
# 외부 함수의 변수를 참조해야한다.
# 외부 함수는 내부 함수를 반환해야 한다.

def outer(name):
    def inner():            #__closure__
        print('Hello, ',name)       #외부 함수의 변후 name을 참조
    return inner                #외부 함수에서 내부 함수 inner 반환

func = outer('허성민')
#func()                  #함수가 종료되어도 자원을 사용하여 print문 출력


def greeting(name,age,gender):
    def inner():
        print(name, '님 안녕하세요.')
        print(age,'세',end=' ')
        print(gender)
    return inner

closure = greeting('허성민','25','male')
closure()

#closure객체, __closure__튜플[0],cell_contents데이터
#print(closure.__closure__[0].cell_contents)
for i in closure.__closure__:
    print(i.cell_contents)

#전역변수의 사용을 최소화 하기위한 방법