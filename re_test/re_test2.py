import re


# group

str = "010-1234-4567"
str2 = '02-512-3232,010-2343-3333,1-32-321,aaa-bbb-cccc,010-23435-5555,010-2343-5555'
result = re.match('(\d{2,3})-(\d{3,4})-(\d{4})$',str)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))
print('\n')

# ,로 나눠진 문자열에서 형식에 맞는 전화번호들의 뒷자리 4자리만 출력
result2 = re.finditer('(\d{2,3})-(\d{3,4})-(\d{4})(?=,|$)',str2)

for idx,r in enumerate(result2,1):
    print(f"{idx}. {r.group(3)}")
print('\n')

# substitution
str3 = '02-512-3232,010-2343-3333,010-2343-5555'
result3 = re.sub('(\d{4})(?=,|$)','****' ,str3)
result4 = re.sub('(?<=\d{3}-\d{4}-)(\d{4})(?=,|$)','****',str)
#전방 탐색 ?= 과 후방탐색 ?<= 
#전방 탐색은 결과물의 뒷부분이 필요 없을 때 사용. 범위가 유동적이어도 가능
#후방 탐색은 결과물의 앞부분의 팔요 없을 때 사용. 범위가 고정적이여야함.
print(result3)
print(result4)