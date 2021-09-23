won = input()
dollar = input()

try:
    print(int(won)/int(dollar))
except ValueError as e:
    print('error',e)
except ZeroDivisionError as e:
    print('error',e)
except:
    print('fatal error')
else:
    print('예외가 발생하지 않았을 경우 출력')
finally:
    print('예외가 발생하던 발생하지 않던 출력')

class PositivenumError (Exception):
    def __init__(self):
        super().__init__('Please input num < 0')

try:
    num = input()
    if int(num) >= 0:
        raise PositivenumError
except Exception as e:
    print(e)