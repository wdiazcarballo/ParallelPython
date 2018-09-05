import threading


times = 1
lock = threading.Lock()

class Duck(threading.Thread):
  
    def __init__(self, name, n):
         threading.Thread.__init__(self)
         self.name = name
        #  self.times = n

    def run(self):
        global times
        for i in range(times):
            print(f'{self.name}: quack quack')
        lock.acquire()
        times += 1
        lock.release()

def main():
    numDucks = 4
    numQuacks = 3
    ducks = []

    for i in range(numDucks):
        duck1 = Duck(f'Duck {i}', numQuacks)
        ducks.append(duck1)

    print(f'we have {len(ducks)} ducks')
    
    for i in range(len(ducks)):
        ducks[i].start()
        ducks[i].join()


if __name__ == '__main__':
    main()
