import threading 
import random

def f(d): 
    d.val = random.randint(1, 100) 
def keep_alive():
    d = threading.local()
    server = threading.Thread(target=f, args=(d,))
    server.start()
