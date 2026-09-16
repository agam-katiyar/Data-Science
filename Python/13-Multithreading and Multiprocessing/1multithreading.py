## Multi threading
## When to use multithreading?
## -> I?O bound task: tasks that spends more time waiting for I/O operations
## -> Concurrent execution: improve throughput of your application by performing multiple operations concurrently.


import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2) ## it sleeps for mentioned time in seconds
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


## concurrent execution- one of these threads executes when other is in sleep mode
## create 2 thread
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
## start the thread
t1.start()
t2.start()

## wait for the execution to complete
t1.join()
t2.join()

# for normal execution
#print_numbers()
#print_letter()

finished_time = time.time()-t
print(finished_time)