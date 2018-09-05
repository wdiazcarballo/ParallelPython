import threading
import time

class Duck(threading.Thread):
    walking = 'Walks like a duck.'
    def __init__(self, quack , num):
        threading.Thread.__init__(self)
        self.quack = quack
        self.num = num
        print(f'Time to quack = {self.quack}')
    def run(self):
        for i in range(self.quack):
            print(f'Duck Number : {self.num} Quaaaack Quaaaack!!')



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

