# first-class object / 일급객체란
# 1. 데이터처럼 사용가능
# 2. 매개변수에 넘겨줄수 있음
# 3. 리턴값으로 사용 가능


# 1.데이터처럼 사용가능

# 함수를 변수에 할당 가능

def func(x,y):
    return x+y

add = func

print(add(2,3))
print()


# 리스트, 튜플, 딕셔너리 등에 할당이 가능

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

calculator = [mul,div]
print(calculator[0](4,2),calculator[1](4,2), sep='\n')



#2. 매개변수로 넘겨줄수 있다.

def data_input():
    data = input('데이터입력 : ')
    return data

def redata(func):
    print(f'입력한 데이터 : ',func())

redata(data_input)


#3. 리턴값으로 사용가능

def plus_ten(a):
    return a + 10

def fx(x):
    return plus_ten(x)

print(fx(5))
