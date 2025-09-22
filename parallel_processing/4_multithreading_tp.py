import concurrent.futures
import time


start = time.perf_counter()
counter = 0

def do_something(secs):
    global counter
    counter = counter + 1
    temp = counter
    print(f"Process: {counter},sleeping for {secs} seconds")
    time.sleep(secs)
    return f"Task {temp} completed in {secs} seconds"

threads = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    results = [executor.submit(do_something,secs) for secs in seconds]
    
    for f in concurrent.futures.as_completed(results): #only needed if functions is returing something. 
        print(f.result())


finish = time.perf_counter()

print(f"All tasks finished in {round(finish - start,2)} seconds")

print("Start of Second part of the code......\n")

with concurrent.futures.ThreadPoolExecutor() as executor2:
    seconds = [9,7,5,3,1]
    results = executor2.map(do_something,seconds) #map will return the result in order of starting the thread

    for result in results:
        print(result)

