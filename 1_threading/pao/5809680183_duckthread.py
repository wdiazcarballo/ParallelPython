import threading
import time

exit_Flag = 0

class duck (threading.Thread):
    times = 1
    def __init__(self, n):
        threading.Thread.__init__(self)
        self.times = n

    def run(self):
        for i in range(self.times):
            print('quack quack {} time(s)'.format(i+1))

def main():
    numDuck = 4
    ducks = []

    for i in range(numDuck):
        d = duck(3)
        ducks.append(d)
    
    print('we have {} ducks'.format(len(ducks)))

    for i in range(numDuck):
        print('duck{} says '.format(i+1))
        ducks[i].start()
        ducks[i].join()
if __name__ == '__main__': main()
