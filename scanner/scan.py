import threading
import variaveis
import time
import nmap

class Scan():
    def __init__(self, delay:int, gateway, prefix:int, speed:int, config):
        self.delay:int = delay
        self.gateway:str = gateway
        self.prefix:int = prefix
        self.speed:int = speed
        self.config:str = config
        self.mapa:nmap.nmap.PortScanner
    def run(self):
        while True:
            print(f"Delay: {self.delay}, Gateway: {self.gateway}, Prefix: {self.prefix}, Speed: {self.speed}, Config: {self.config}")
            time.sleep(3)
            if (variaveis.FINISHING.is_set() == True):
                variaveis.ABORTED.set()
                return
            threading.Event.wait(variaveis.FINISHING, self.delay*60)