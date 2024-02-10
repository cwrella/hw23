import multiprocessing as mp
import time
import random

def number():
    n = random.randint(1, 100)
    file = open("number.txt", "w")
    file.write(str(n))
    file.close()
    time.sleep(1)

if __name__ == "__main__":
    start = time.time()
    processes = []
    for i in range(1000):
        process = mp.Process(target=number)
        process.start()
        processes.append(process)

    for i in processes:
        i.join()
    print(time.time() - start)
