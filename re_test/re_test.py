import re

# re 모듈의 메서드

str = 'love people around you, love your work, love your self'

# match - 문자열 처음부터 검색, match 객체 1개 return
result_m = re.match('love',str)
print(result_m)

# search : 문자열의 전첼르 검색 , match 객체 1개 return
result_s = re.search('love',str)
print(result_s)

# findall - 문자열 전체 검색, 문자열 리스트 return
result_fa = re.findall('love',str)
print(result_fa)

#finditer - 문자열 전체 검색, match 객체 iterator return
result_fi = re.finditer('love',str)
for r in result_fa:
    print(r)

# fullmatch - 패턴과 문자열이 완벽하게 일치하는지 검사
str2 = 'Hey Guys, read a books'
result_fm = re.fullmatch('.*',str2)
print(result_fm)



# match 모듈의 메서드

# group() - 매칭된 문자열을 반환
print(result_s.group())

# start() - 매칭된 문자열의 시작점 반환
print(result_s.start())

# end() - 매칭된 문자열의 끝점 반환
print(result_s.end())

# span() - 매칭된 문자열의 시작과 끝 반환
print(result_s.span())


