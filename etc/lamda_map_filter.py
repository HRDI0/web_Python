#lamda

#lambda -> 아주 간단한 함수의 경우 
# (ex) def minus_one(num): 
#          return a - 1
#같은 경우      lambda a:a-1 로 대신할수 있다. - 가독성, 효율성

print((lambda a:a-1)(10))

#if문도 들어간다.       x가 만약 0보다 크다면 True 작다면 False
print((lambda x:True if x > 0 else False)(-1))

#map함수 와 lambda 활용 map은 순서가 있는 데이터를 순서대로 처리하여 map 객체로 리턴한다.
#ex)
a = [1,2,3,4]
ao = list(map(lambda x:x-1,a))      #a를 map으로 하나씩 lambda로 1 빼서 list로 만든다.
print(ao)

b = ['   A    ', '   B    ']
bo = list(map(lambda x:x.strip(),b))        #마찬가지로 문자열에서 공백을 제거하고 리스트로 만든다.
print(bo)

#filter 함수
#조건에 맞춰 순서가 있는 데이터를 필터링한다.

animals = ['Cat', 'Dog', 'Lion', 'Tiger', 'Monkey']
animalsO = list(filter(lambda x:len(x)<=3,animals))     
#리스트에서 문자열의 길이가 3이하인것만 필터링하여 리스트로 만든다.
print(animalsO)