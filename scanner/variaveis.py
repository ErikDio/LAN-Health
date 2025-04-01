import threading

DEBUG:bool = False
LOG:bool = False
RUNNING = False
FINISHING:threading.Event = threading.Event()
ABORTED:threading.Event = threading.Event()