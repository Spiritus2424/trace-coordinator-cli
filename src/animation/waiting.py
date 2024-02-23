from multiprocessing import Pool
from threading import Event, Thread
import sys
import time

def start_waiting_animation():
    should_stop = Event()
    thread = Thread(target=waiting_animation, args=[should_stop])
    thread.start()
    return should_stop

def stop_waiting_animation(animation_event: Event):
    animation_event.set()
    
def waiting_animation(stop_event: Event):
    n = 0
    while not stop_event.is_set():
        n = n % 3 + 1
        dots = n * '.' + (3 - n) * ' '
        sys.stdout.write(f"{dots}")
        # Move the cursor backward https://blog.finxter.com/how-to-overwrite-the-previous-print-to-stdout-in-python/
        sys.stdout.write("\033[3D") 
        sys.stdout.flush() 
        time.sleep(0.2)
