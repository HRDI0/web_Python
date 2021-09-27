from multiprocessing import Process
import time

class Sub(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f'[sub] {self.name} start')
        time.sleep(2)
        print(f'[sub] {self.name} end')

if __name__ == '__main__':
    print('[main] start')
    p = Sub(name='start_coding')
    p.start()
  
    #프로세스가 살아있는지 검사
    if p.is_alive():
        p.terminate()   #강제 종료
    print('[main] end')


# 추가적인 학습
# 스레드간 데이터 처리 (lock)
# 프로세스간 데이터 전송 (queue, pipe)
# 속도비교
# 운영체제와 메모리