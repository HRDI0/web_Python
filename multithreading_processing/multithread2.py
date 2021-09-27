import threading
import time

#주식 자동 매매 시뮬

#매수
def buyer():
    for i in range(5):
        print('[buyer] loading API...')
        time.sleep(1)
        print('[buyer] loading API...')
        time.sleep(1)
        print('[buyer] buy stanby')
        time.sleep(1)
        print('[buyer] buy success')
        time.sleep(1)

#매도
def seller():
    for i in range(5):
        print('[seller] loading API...')
        time.sleep(1)
        print('[seller] loading API...')
        time.sleep(1)
        print('[seller] sell stanby')
        time.sleep(1)
        print('[seller] sell success')
        time.sleep(1)

print('[main] start')
buyer_t = threading.Thread(target=buyer)
seller_t = threading.Thread(target=seller)
buyer_t.start()
seller_t.start()

buyer_t.join()                  #join() sub thread가 끝날때까지 main이 기다린다.
seller_t.join()
print('[main] end')