import threading
import time

def cook_biryani(flavor="Chicken"):
    print(f"Starting to cook {flavor} biryani...")
    # Simulate cooking time
    time.sleep(10)
    print(f"{flavor} biryani is ready!")


def do_dishes():
    print("Washing Dishes Start")
    time.sleep(3) 
    print("Dish washing done 60%")
    time.sleep(2)
    print("Dish washing done!")

def take_out_trash():
    print("Taking out trash") 
    time.sleep(2)
    print("Trash Cleaned...") 


job1 = threading.Thread(target=cook_biryani,args=("Mutton",))   
job2 = threading.Thread(target=do_dishes)   
job3 = threading.Thread(target=take_out_trash)   

job1.start()
job2.start()
job3.start()

job1.join() #join() will wait for this Thread to finish before printing ( "All Job Done!")
job2.join() #join() will wait for this Thread to finish before printing ( "All Job Done!")
job3.join() #join() will wait for this Thread to finish before printing ( "All Job Done!")

print("All Job Done!")

#### Daemon threads:  run in the background and are killed when the main program exits.

def daemon_thread():
    i=1
    while True:
        time.sleep(1)
        print(i)
        i +=1

job4_daemon=threading.Thread(target=daemon_thread,daemon=True)

job4_daemon.start()

print("Daemon Thread Started...")
time.sleep(6)
print("Daemon Thread Exited suddenly!")
