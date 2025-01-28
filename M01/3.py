# Kelas Murid
class Murid:
    def __init__(self, nama, jenis_kelamin, tingkat):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.tingkat = tingkat
        self.jam_pengajaran = self.hitung_jam_pengajaran()
        self.biaya_les = self.hitung_biaya_les()
 
    # Metode untuk menghitung biaya les berdasarkan tingkatan
    def hitung_biaya_les(self):
        if self.tingkat == "TK":
            return 300000
        elif self.tingkat == "SD":
            return 500000
        elif self.tingkat == "SMP":
            return 700000
        elif self.tingkat == "SMA":
            return 1000000
        else:
            return 0
 
    # Metode untuk menghitung jam pengajaran berdasarkan tingkatan
    def hitung_jam_pengajaran(self):
        if self.tingkat == "TK" or self.tingkat == "SD":
            return 2
        elif self.tingkat == "SMP" or self.tingkat == "SMA":
            return 1
        else:
            return 0
 
    # Metode untuk mencetak kartu murid
    def cetak_kartu(self):
        print("\n--- Kartu Les Murid ---")
        print(f"Nama           : {self.nama}")
        print(f"Tingkat        : {self.tingkat}")
        print(f"Jam Pengajaran : {self.jam_pengajaran} jam")
        print(f"Biaya Les      : Rp {self.biaya_les:,.2f}")
        print("------------------------")
 
# Daftar murid yang terdaftar di les
murid1 = Murid("Andi Wijaya", "Laki-laki", "SMA")
murid2 = Murid("Siti Nurjanah", "Perempuan", "SD")
murid3 = Murid("Budi Santoso", "Laki-laki", "SMP")
murid4 = Murid("Rina Melati", "Perempuan", "TK")
 
# Cetak kartu masing-masing murid
murid1.cetak_kartu()
murid2.cetak_kartu()
murid3.cetak_kartu()
murid4.cetak_kartu()

