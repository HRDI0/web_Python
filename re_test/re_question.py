import re

# 날짜 체크
# 날짜는 YYYY/MM/DD 형식이며 
# 연도는 1000 ~ 9999년 으로 4글자, 월은 01~12월로 2글자, 일은 01~31까지 2글자이다.
# 조건에 부합한 날짜 텍스트를 찾아 TRUE 출력하고 아닌것은 FALSE로 출력하라.

date_list = [
'2022/08/08','1000/01/01','9999/12/31',
'900/02/02','12000/10/26','2021/13/01',
'2023/2/02','2024/06/3','2023/06/35'
]

regex = re.compile('^([1-9][0-9]{3})\/(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])$')
# for i in date_list:
#     result = re.match(regex,i)
#     if result != None:
#         print(f"{i}  TRUE")
#     else:
#         print(f"{i}  FALSE")

for i in date_list:
    result = regex.match(i)
    out = (lambda x: True if x != None else False)(result)
    print(f"{i}  {out}")
print('\n')


# 이메일 검사
# 조건에 맞춰 이메일이 정확하게 입력되었는지 검사하라.
# 1. 이메일은 ID와 host 파트로 나뉘어 있다.(ID @ host)
# 2. ID는 영대소문자, 숫자, 특수문자(-_)가 들어갈 수 있다.
# 3. host는 영대소문자, 숫자, 특수문자(-)가 들어갈 수 있다.
# 4. host는 두 개 이상의 도메인으로 구성될 수 있다.(.com / .co.kr / .ag.kl 등)

email_list = [
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.co.kr',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver'
]

#내가 짠거(틀림 도메인 갯수가 두개이상일수도 있음.)
#regex2 = '^\b([a-zA-Z0-9-_]+)@([a-zA-Z0-9-]+)\.([a-z]+)(\.[a-z]+)?'
      
regex2 = re.compile('^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


for j in email_list:
    result2 = regex2.match(j)
    out = (lambda x: True if x != None else False)(result2)
    print(f"{j}  {out}")
print('\n')
