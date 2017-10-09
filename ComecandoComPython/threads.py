from threading import Thread
import time
import random


def my_func(i):
    print('Iniciando a thread {}'.format(i))
    time.sleep(random.random() + 1)
    print('Thread {} finalizada'.format(i))


for i in range(10):
    t = Thread(target=my_func, args=(i,))
    t.start()
