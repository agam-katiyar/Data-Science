## Multiprocessing

## allows you to create that runs in parallel
# WHen to use?
##-> CPU bound tasks that are heavy on CPU usage(Mathematical operations, etc)
# -> Parallel exection- Multiple cores of CPU

import multiprocessing

import time
## Independent processes with indepent memory and all
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")


if __name__ =="__main__":
    ## Create 2 processses
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()


    ## start the provceess
    p1.start()
    p2.start()

    ## Wait for the process to complete
    p1.join()
    p2.join()

    finished_time= time.time() -t
    print(finished_time)