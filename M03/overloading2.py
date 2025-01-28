class Mahasiswa:
    def __init__(self, nim, nama="Null", kelas="Pagi", umur=20):
        self.nim = nim
        self.nama= nama
        self.kelas = kelas
        self.umur = umur
        #if(type(self.nim) == type.__str__)
    def detail(self):
        print("{0} {1} {2} {3}".format(self.nim, self.nama, self.kelas, self.umur))

ali = Mahasiswa("231119999", "Ali", "C_Pagi")
ali.detail()
adi = Mahasiswa("231119999", "Adi", "C_Pagi", 22)
adi.detail()
budi = Mahasiswa("231119998")
budi.detail()

