import threading

times = 1
lock = threading.Lock()

class Duck(threading.Thread):
    def __init__(self, name):
         threading.Thread.__init__(self)
         self.name = name

    def run(self):
        global times
        for i in range(times):
            lock.acquire()
          #  print(f'{self.name}: quack quack')
            print('{}: quack quack'.format(self.name))
            times+=1
            lock.release()

def main():
    numDucks = 4
    numQuacks = 3
    ducks = []

    for i in range(numDucks):
        duck1 = Duck('Duck {}'.format(i))
        ducks.append(duck1)

    #print(f'we have {len(ducks)} ducks')
    print('we have {}'.format(len(ducks)))

    
    for i in range(len(ducks)):
        ducks[i].start()
        ducks[i].join()


if __name__ == '__main__':
    main()
