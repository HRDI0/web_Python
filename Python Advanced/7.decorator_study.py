# decorator - 함수의 앞뒤에 부가적인 기능을 넣어주고 싶을때 사용. (로깅, 권한 등.)
# 클로저를 사용해야함. 기능 위에 @decorator 기입 (@abstractmethod, @staticmethod 등)

def logger(func):        #decorator 생성
    def wrapper(arg):              #함수의 시작과 끝을 로깅
        print('func_start')
        func(arg)
        print('func_end')
    return wrapper

@logger                 #decorator 작동
def print_hello(name):
    print('hello',name)
@logger
def print_bye(name):
    print('bye',name)


print_hello('world')
print_bye('world')