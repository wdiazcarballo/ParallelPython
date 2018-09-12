import threading
from queue import Queue
import time
import shutil

print_lock = threading.Lock()

class IoThreading(threading.Thread):
    
    def __init__(self,NumberThread,compress_queue):
        threading.Thread.__init__(self)
        self.NumberThread = NumberThread
        self.compress_queue = compress_queue

    def copy_op(self,file_data):
        with print_lock:
            print("Starting thread : {}".format(threading.current_thread().name))

        mydata = threading.local()
        mydata.ip, mydata.op = next(iter(file_data.items()))

        shutil.copy(mydata.ip, mydata.op)

        with print_lock:
            print("Finished thread : {}".format(threading.current_thread().name))

    def run(self): #def process_queue():
        while True:
            file_data = self.compress_queue.get()
            print(f'self.compress_queue.get()  -> {file_data} With threading -> {self.NumberThread} ')
            self.copy_op(file_data)
            self.compress_queue.task_done()

def main():
        
    compress_queue = Queue()

    output_names = [{'clip1.mp4' : 'clip11.mp4'},{'clip2.mp4' : 'clip22.mp4'}]

    for i in range(2):
        # t = threading.Thread(target=process_queue)
        t = IoThreading(i,compress_queue)
        t.daemon = True
        t.start()

    start = time.time()

    for file_data in output_names:
        compress_queue.put(file_data)

    compress_queue.join()

    print("Execution time = {0:.5f}".format(time.time() - start))

if __name__ == '__main__' : main()
