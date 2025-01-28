from abc import ABC, abstractmethod

class Murid(ABC):
    def __init__(self, nama, noHPOrtu, biayaLes):
        self.nama = nama
        self.noHPOrtu = noHPOrtu
        self.biayaLes = biayaLes
 
    @abstractmethod
    def infoTambahan(self):
        pass
 
class MuridSD(Murid):
    def __init__(self, nama, noHPOrtu, jenis_kelamin):
        super().__init__(nama, noHPOrtu, 500000)
        self.jenis_kelamin = jenis_kelamin
 
    def infoTambahan(self):
        return f"Nama: {self.nama}, No HP Ortu: {self.noHPOrtu}, Jenis Kelamin: {self.jenis_kelamin}, Biaya Les: Rp. {self.biayaLes:,}"
 
class MuridSMP(Murid):
    def __init__(self, nama, noHPOrtu, umur):
        super().__init__(nama, noHPOrtu, 800000)
        self.umur = umur
 
    def infoTambahan(self):
        return f"Nama: {self.nama}, No HP Ortu: {self.noHPOrtu}, Umur: {self.umur}, Biaya Les: Rp. {self.biayaLes:,}"
 
class MuridSMA(Murid):
    def __init__(self, nama, noHPOrtu, jenisKelas):
        super().__init__(nama, noHPOrtu, 1200000)
        self.jenisKelas = jenisKelas
 
    def infoTambahan(self):
        return f"Nama: {self.nama}, No HP Ortu: {self.noHPOrtu}, Jenis Kelas: {self.jenisKelas}, Biaya Les: Rp. {self.biayaLes:,}"
 
if __name__ == "__main__":
    murid_sd = MuridSD("Ani", "08123456789", "Perempuan")
    murid_smp = MuridSMP("Budi", "08234567890", 13)
    murid_sma = MuridSMA("Cici", "08345678901", "IPA")
 
    print(murid_sd.infoTambahan())
    print(murid_smp.infoTambahan())
    print(murid_sma.infoTambahan())