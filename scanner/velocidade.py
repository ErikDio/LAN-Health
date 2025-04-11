import speedtest
import os
import log

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
    def teste(self):
        try:
            st = speedtest.Speedtest()
            vel_download = st.download(threads=self.threads)
            return vel_download
        except Exception as e:
            log.box_text_log(f"Exceção: '{e}' ao tentar testar a velocidade de download da rede.")