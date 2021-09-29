#generator 만들기
# [i * 2 for i in range(1,10)] ->  (i * 2 for i in range(1,10))
double_generator =  (i * 2 for i in range(1,10))

for i in double_generator:
    print(i)

#list 와 generator 차지하는 메모리의 크기
import sys

list_data = [i * 3 for i in range(1,10000+1)]
generator_data = (i * 3 for i in range(1,10000+1))

print('list_data size : ',sys.getsizeof(list_data))     #85176byte
print('generator_data size : ',sys.getsizeof(generator_data))   #112byte
#이유는 list는 데이터를 미리 연산해서 저장해놓는 반면, generator는 연산 식만 저장하고 불러낼때마다
#연산한다. 그러므로 빅데이터를 처리할때는 필수적으로 generator가 사용된다.
