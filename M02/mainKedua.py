class Masyarakat:
    def __init__(self, nama):
        self.alamat = "Jl.M.H.Thamrin"
        self.berat = 60
        self.nama = nama
        self.umur = 21
    def perkenalan(self):
        print("Halo nama saya", self.nama)
    def ulangTahun(self):
        self.umur += 1
        print("Setelah ulang tahun umur saya menjadi", self.umur)

class Pemadam(Masyarakat):
    def __init__(self, nama, alat):
        super().__init__(nama)
        self.alat = alat
    def perkenalan(self):
        print("Halo, nama saya {0}, tinggal di {1} dan berat saya {2}".format(self.nama, self.alamat, self.berat))
        print("Saya menggunakan", self.alat, "sebagai perlengkapan saya.")
        super().ulangTahun()

class Polisi(Masyarakat):
    def __init__(self, nama, senjata):
        super().__init__(nama)
        self.alat = senjata
    def perkenalan(self):
        super().perkenalan()
        print("Saya menggunakan", self.alat, "sebagai senjata saya.")
