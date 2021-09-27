from multiprocessing import Process
import time

#multiprocessing to class

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
    p.join()
    print('[main] end')