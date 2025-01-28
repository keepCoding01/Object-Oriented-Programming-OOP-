class TasyaSyafriza :
    def __init__(self,NIM,nama,jenisKelamin,noHP) :
        self.NIM = NIM
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.noHP = noHP

class Mahasiswa(TasyaSyafriza) :
    def __init__(self, NIM,nama,jenisKelamin,noHP):
        super().__init__(NIM,nama,jenisKelamin,noHP)
        

    def absensi(self):
        print(f'Ini adalah absensi Mahasiswa dengan NIM {self.NIM} - {self.nama}') 
        
        
class Dosen(TasyaSyafriza) :
    def __init__(self, NIM,nama,jenisKelamin,noHP,):
        super().__init__(NIM,nama,jenisKelamin,noHP)
        

    def perkenalan(self):
        print(f'Ini adalah absensi Dosen dengan NIP {self.nama} - {self.noHP}') 


mhs = Mahasiswa('231112518', 'Tiara Andini', "Perempuan", '085645332122')
dos = Dosen ("231116543", 'Andrian', "Laki", '08675543432')

mhs.absensi()
dos.perkenalan()

