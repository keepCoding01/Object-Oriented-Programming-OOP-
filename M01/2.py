# Kelas Barang
class Barang:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
    # Fungsi untuk menjual barang (mengurangi stok)
    def jual(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        else:
            print(f"Stok {self.nama} tidak mencukupi!")
            return False
    # Mengecek apakah stok hampir habis
    def cek_stok_hampir_habis(self):
        return self.stok <= 1  # Jika stok <= 1 dianggap hampir habis
 
    # Mengembalikan harga total barang yang terjual
    def total_harga_terjual(self, jumlah):
        return self.harga * jumlah
 
 
# Kelas untuk mengelola laporan pengeluaran bulanan
class LaporanPengeluaran:
    def __init__(self):
        self.pengeluaran_bulanan = 0
        self.laporan_terjual = []
 
    # Tambahkan pengeluaran dan laporan barang yang terjual
    def tambah_pengeluaran(self, barang, jumlah):
        total = barang.total_harga_terjual(jumlah)
        self.pengeluaran_bulanan += total
        self.laporan_terjual.append((barang.nama, jumlah, total))
 
    # Cetak laporan pengeluaran bulanan
    def cetak_laporan(self):
        print("\nLaporan Pengeluaran Bulanan:")
        if not self.laporan_terjual:
            print("Tidak ada barang yang terjual bulan ini.")
        else:
            for barang, jumlah, total in self.laporan_terjual:
                print(f"{barang} - Jumlah Terjual: {jumlah}, Total Harga: Rp {total}")
        print(f"\nTotal Pengeluaran Bulanan: Rp {self.pengeluaran_bulanan}")
 
 
# Fungsi untuk memantau stok barang yang hampir habis
def pantau_stok(barang_list):
    print("\nBarang yang hampir habis:")
    stok_hampir_habis = False
    for barang in barang_list:
        if barang.cek_stok_hampir_habis():
            print(f"{barang.nama} (Stok: {barang.stok})")
            stok_hampir_habis = True
    if not stok_hampir_habis:
        print("Semua barang dalam stok aman.")
 
 
# Data barang yang tersedia di E-Commerce
barang1 = Barang("Hand Sanitizer", 20000, 2)
barang2 = Barang("Ban Mobil", 800000, 1)
barang3 = Barang("Buah-buahan", 50000, 10)
barang4 = Barang("Botol Minuman Bayi", 15000, 0)
 
# Daftar barang di toko
barang_list = [barang1, barang2, barang3, barang4]
 
# Buat objek laporan pengeluaran bulanan
laporan = LaporanPengeluaran()
 
# Simulasi penjualan barang
barang1.jual(1)  # Menjual 1 Hand Sanitizer
laporan.tambah_pengeluaran(barang1, 1)
 
barang2.jual(1)  # Menjual 1 Ban Mobil
laporan.tambah_pengeluaran(barang2, 1)
 
barang3.jual(5)  # Menjual 5 Buah-buahan
laporan.tambah_pengeluaran(barang3, 5)
 
# Pantau stok yang hampir habis
pantau_stok(barang_list)
 
# Cetak laporan pengeluaran bulanan
laporan.cetak_laporan()