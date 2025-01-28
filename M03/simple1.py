class Murid:
    def __init__(self, nama, hpOrtu, tingkatan):
        self.nama = nama
        self.hpOrtu = hpOrtu
        self.tingkatan = tingkatan
 
    def biayaLes(self):
        pass 
 
class MuridLes(Murid):
    def __init__(self, nama, hpOrtu, tingkatan):
        super().__init__(nama, hpOrtu, tingkatan)
 
class MuridSD(MuridLes):
    def __init__(self, nama, hpOrtu, jenis_kelamin):
        super().__init__(nama, hpOrtu, "SD")
        self.jenis_kelamin = jenis_kelamin
 
    def biayaLes(self):
        return 500000
 
class MuridSMP(MuridLes):
    def __init__(self, nama, hpOrtu, umur):
        super().__init__(nama, hpOrtu, "SMP")
        self.umur = umur
 
    def biayaLes(self):
        return 800000
 
class MuridSMA(MuridLes):
    def __init__(self, nama, hpOrtu, jurusan):
        super().__init__(nama, hpOrtu, "SMA")
        self.jurusan = jurusan
 
    def biayaLes(self):
        return 1200000
 
murid_sd = MuridSD("Andi", "081234567890", "Laki-laki")
murid_smp = MuridSMP("Budi", "089876543210", 13)
murid_sma = MuridSMA("Cici", "085678901234", "IPA")
 
print(f"Nama: {murid_sd.nama}, Tingkatan: {murid_sd.tingkatan}, Biaya Les: Rp {murid_sd.biayaLes()}")
print(f"Nama: {murid_smp.nama}, Tingkatan: {murid_smp.tingkatan}, Biaya Les: Rp {murid_smp.biayaLes()}")
print(f"Nama: {murid_sma.nama}, Tingkatan: {murid_sma.tingkatan}, Biaya Les: Rp {murid_sma.biayaLes()}")