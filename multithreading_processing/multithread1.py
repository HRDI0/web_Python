import threading

#멀티 스레딩이란.
#하나의 프로세스에서 다수의 스레드가 거의 동시처럼 번갈아가며 처리되는것 - 동시성

def work():
    print('[sub] start')
    keyword = input('[sub] 검색어 >>>')
    print(f'[sub] {keyword}로 검색합니다.')
    print('[sub] end')

print('[main] start')

worker = threading.Thread(target=work)
worker.daemon = True                #main 이 종료되면 같이 종료
worker.start()

print('[main] working') 
print('[main] end')