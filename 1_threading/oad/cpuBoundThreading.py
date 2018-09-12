#5809650541


import threading
from queue import Queue
import time

list_lock = threading.Lock()

class Cpu(threading.Thread):

    def __init__(self,min_nums,sum_primes_list):
        threading.Thread.__init__(self)
        self.min_nums = min_nums
        self.sum_primes_list = sum_primes_list
        
    def run(self):
       
        while True:
            
            rand_num = self.min_nums.get()
            self.find_rand(rand_num)
            self.min_nums.task_done()
    

    


    def find_rand(self,num):
        
        sum_of_primes = 0

        ix = 2

        while ix <= num:
            if self.is_prime(ix):
                sum_of_primes += ix
            ix += 1

        sum_primes_list.append(sum_of_primes)


    def is_prime(self,num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num%2 == 0 or num%3 == 0:
            return False
        i = 5
        while i*i <= num:
            if num%i == 0 or num%(i+2) == 0:
                return False
            i += 6
        return True
    
  


def main():

    min_nums = Queue()
    rand_list = [1000000,2000000,3000000]
    global sum_primes_list 
    sum_primes_list = list()
    
    for i in range(2):
        t = Cpu(min_nums,sum_primes_list)
        t.daemon = True
        t.start()

    start = time.time()

    for rand_num in rand_list:
        min_nums.put(rand_num)

    min_nums.join()

    end_time = time.time()

    sum_primes_list.sort()

    print(sum_primes_list)
    print("Execution time = {0:.5f}".format(end_time - start))


if __name__ == '__main__' : main()

 