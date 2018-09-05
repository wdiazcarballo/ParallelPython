import threading
import time



times = 1
lock = threading.Lock()

class Duck(threading.Thread):
    walking = 'Walks like a duck.'
    def __init__(self, quack , num):
        threading.Thread.__init__(self)
        self.quack = quack
        self.num = num
        print(f'Time to quack = {self.quack}')
    def run(self):
        global times
        for i in range(times):
            print(f'Duck : {self.num} Quaaaack Quaaaack!!')
        lock.acquire()
        times += 1
        lock.release()



def main():
    numDucks = 4
    Quaaaack = 3
    ducks = []
    for i in range(numDucks): 
        ducks.append(Duck(Quaaaack,i))
        # print(len(ducks))


    for i in range(len(ducks)):
        ducks[i].start()
        ducks[i].join()


if __name__ == '__main__' : main()

