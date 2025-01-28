from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    
    @abstractmethod
    def absensi(self):
        pass

class Dosen(Person):
    def absensi(self):
        return f"Silahkan mulai pelajaran, {self.name}."

class Mahasiswa(Person):
    def absensi(self):
        return f"Terima kasih sudah hadir, {self.name}."

if __name__ == "__main__":
    dosen = Dosen("Bapak Arif", "D12345")
    mahasiswa = Mahasiswa("Andi", "M54321")
    
    print(dosen.absensi())  
    print(mahasiswa.absensi()) 
