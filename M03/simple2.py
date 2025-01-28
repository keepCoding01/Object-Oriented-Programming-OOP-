class Person:
    def __init__(self, nama, noIdentitas):
        self.nama = nama
        self.noIdentitas = noIdentitas
 
    # def absen(self):
    #     pass  
 
class AnggotaKelas(Person):
    def __init__(self, nama, noIdentitas):
        super().__init__(nama, noIdentitas)
 
class Dosen(AnggotaKelas):
    def absen(self):
        print("Silahkan mulai pelajaran.")
 
class Mahasiswa(AnggotaKelas):
    def absen(self):
        print("Terima kasih sudah hadir.")
 
dosen1 = Dosen("Andi", "231112518")
mahasiswa1 = Mahasiswa("Budi", "231115413")
 
dosen1.absen()  
mahasiswa1.absen()  