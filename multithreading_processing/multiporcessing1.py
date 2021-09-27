import multiprocessing as mp

#멀티 프로세싱이란
#여러개의 스레드를 여러개의 프로세스에서 처리하는것 - 병렬성

def sub_process(name):
    print('[sub] start')
    print(name)
    cps = mp.current_process()
    print(f'[sub] pid : {cps.pid}')
    print('[sub] end')

if __name__ == '__main__':
    print('[main] start')
    p = mp.Process(target=sub_process,args=('start_coding',))
    p.start()
    cpm = mp.current_process()
    print(f'[mian] pid : {cpm.pid}')
    print('[main] end')
