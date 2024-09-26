import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.en = 100  # Колличество врагов

    def run(self):
        n = 0
        print(f'{self.name}, на нас напали! ')
        while self.en > 0:
            time.sleep(1)
            self.en -= self.power
            n += 1
            print(f'{self.name} сражается {n} день(дня)..., осталось {self.en} воинов.')
        print(f'{self.name} одержал победу спустя {n} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

thread1 = first_knight
thread1.start()
thread2 = second_knight
time.sleep(1)
thread2.start()
thread1.join()
thread2.join()
print('Все битвы закончились!')
