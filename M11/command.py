# memisahkan perintah (command) dari objek yang melaksanakan perintah. Berguna untuk membuat sistem undo/redo atau batch execution.
# Contoh Sederhana: Bayangkan Anda memiliki remote kontrol yang bisa menghidupkan dan mematikan lampu.

from abc import ABC, abstractmethod

class proses(ABC):
    @abstractmethod
    def execute (): pass

class switchOn(proses):
    def execute(self):
        print("Lampu nyala")

class switchOff(proses):
    def execute(self):
        print("Lampu mati")


class switch:
    def __init__ (self, cmd):
        self.cmd = cmd
    def Proses(self):
        self.cmd.execute()

if __name__ == "__main__":
    on = switchOn()
    sw = switch(on)
    sw.Proses()

    print('\n')

    off = switchOff()
    sw = switch(off)
    sw.Proses()