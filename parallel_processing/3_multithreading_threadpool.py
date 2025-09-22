import concurrent.futures
import time

counter = 0

def do_something(secs):
    global counter
    counter = counter + 1
    temp = counter
    print(f"Process: {counter},sleeping for {secs} seconds")
    time.sleep(secs)
    print(f"Task {temp} completed!")

threads = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5,4,3,2,1]
    results = [executor.submit(do_something,secs) for secs in seconds]
    
    # for f in concurrent.futures.as_completed(results): only needed if functions is returing something. 
    #     f.result()


# do_something(3)    
# do_something(2)
