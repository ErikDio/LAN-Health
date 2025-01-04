import speedtest
import os

def GetThreads():
    try:
        return os.cpu_count()
    except NotImplementedError:
        return 1
class Velocidade:
    threads = 1
    def __init__(self):
        self.threads = GetThreads()
        if(self.threads > 4):
            self.threads = 4
    def Teste(self, LOG):
        try:
            st = speedtest.Speedtest()
            vel_download = st.download(threads=self.threads)
            return vel_download
        except Exception as e:
            if(LOG == True):
                print("Exceção: '{e}' ao tentar testar a velocidade de download da rede.")
            return 0