from abc import ABC, abstractmethod

class atasiEror(Exception):
    def __init__(self, pesan):
        self.pesan = pesan
        super().__init__(self.pesan)

class Murid(ABC):
    def __init__(self, nama, noHPOrtu, biayaLes, tingkatan, jamPengajaran):
        if not nama:
            raise atasiEror("Waduh, sepertinya NAMA MURID belum kamu isi deh...")
        if len(noHPOrtu) < 10:
            raise atasiEror("Ehhh, NO HP ORTU ga valid, masukin yang benar ya...")
        
        self.nama = nama
        self.noHPOrtu = noHPOrtu
        self.biayaLes = biayaLes
        self.tingkatan = tingkatan
        self.jamPengajaran = jamPengajaran
 
    @abstractmethod
    def infoKeterangan(self):
        pass

class MuridTK(Murid):
    def __init__(self, nama, noHPOrtu, jenisKelamin):
        super().__init__(nama, noHPOrtu, 300000, "TK", 2)
        self.jenisKelamin = jenisKelamin
 
    def infoKeterangan(self):
        return f"Nama: {self.nama}, Tingkatan: {self.tingkatan}, Jam Pengajaran: {self.jamPengajaran} jam, Biaya Les: Rp. {self.biayaLes:,}"

class MuridSD(Murid):
    def __init__(self, nama, noHPOrtu, jenisKelamin):
        super().__init__(nama, noHPOrtu, 500000, "SD", 2)
        self.jenisKelamin = jenisKelamin
 
    def infoKeterangan(self):
        return f"Nama: {self.nama}, Tingkatan: {self.tingkatan}, Jam Pengajaran: {self.jamPengajaran} jam, Biaya Les: Rp. {self.biayaLes:,}"

class MuridSMP(Murid):
    def __init__(self, nama, noHPOrtu, umur):
        super().__init__(nama, noHPOrtu, 700000, "SMP", 1)
        self.umur = umur
 
    def infoKeterangan(self):
        return f"Nama: {self.nama}, Tingkatan: {self.tingkatan}, Jam Pengajaran: {self.jamPengajaran} jam, Biaya Les: Rp. {self.biayaLes:,}"

class MuridSMA(Murid):
    def __init__(self, nama, noHPOrtu, jenisKelas):
        super().__init__(nama, noHPOrtu, 1000000, "SMA", 1)
        self.jenisKelas = jenisKelas
 
    def infoKeterangan(self):
        return f"Nama: {self.nama}, Tingkatan: {self.tingkatan}, Jam Pengajaran: {self.jamPengajaran} jam, Biaya Les: Rp. {self.biayaLes:,}"


try:
    print("-"*100)
    muridTK = MuridTK("Tasya", "08123456789", "Perempuan")
    muridSD = MuridSD("Budi", "084353345679", "Laki-laki")
    muridSMP = MuridSMP("Cici", "08345678901", 14)
    muridSMA = MuridSMA("Doni", "08345678901", "IPS")
    
    print(muridTK.infoKeterangan())
    print(muridSD.infoKeterangan())
    print(muridSMP.infoKeterangan())
    print(muridSMA.infoKeterangan())

except atasiEror as e:
    print(f"Eror : {e}")
