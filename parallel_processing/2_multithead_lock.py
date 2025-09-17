import threading

counter = 0 #global variable

#Creation: A Lock object is initialized in the unlocked state:
lock = threading.Lock()

def increment_count():
    #global counter #To modify a global variable inside a function, you must use the global keyword.
    global counter

    for _ in range(100_100):
        lock.acquire() # Here each thread acquires the lock before incrementing counter and releases it afterward, 
                       # guaranteeing that only one thread modifies counter at any given moment, thus preventing race 
                       # conditions and ensuring the correct final value.
        counter = counter + 1
        lock.release() # Release the lock


threads = []

for _ in range(3):
    thread =threading.Thread(target=increment_count)
    threads.append(thread)
    

for th in threads:
    th.start()
    th.join()

print("Final Value of Counter: ",counter)        



