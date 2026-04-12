import threading
import time

def fucn(seconds):
    print(f'sleeping for {seconds}')
    time.sleep(seconds)



# t1 = time.perf_counter()
# fucn(1)
# fucn(5)
# fucn(2)
# t2 = time.perf_counter()
# print(t2 - t1)

t1 = time.perf_counter()

tt1 =  threading.Thread(target=fucn, args=[1])
tt2 =  threading.Thread(target=fucn, args=[5])
tt3 =  threading.Thread(target=fucn, args=[2])

tt1.start()
tt2.start()
tt3.start()


tt1.join()
tt2.join()
tt3.join()

t2 = time.perf_counter()
print(t2 - t1)