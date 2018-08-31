import threading

class Duck(threading.Thread):
    times = 1
    def __init__(self, n):
         threading.Thread.__init__(self)
         self.times = n

    def run(self):
        for i in range(self.times):
            print('quack quack')

def main():
    numDucks = 4
    ducks = []

    for i in range(numDucks):
        duck1 = Duck(3)
        ducks.append(duck1)

    print(f'we have {len(ducks)} ducks')
    
    for i in range(len(ducks)):
        ducks[i].start()
        ducks[i].join()


if __name__ == '__main__':
    main()
