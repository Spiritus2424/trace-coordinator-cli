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
        sys.stdout.write('\r Waiting '+ dots)
        sys.stdout.flush()
        time.sleep(0.5)
