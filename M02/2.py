class Delarosa:
    def __init__(self, nama_barang, brand, stok, harga):
        self.nama_barang = nama_barang
        self.brand = brand
        self.stok = stok
        self.harga = harga

    def info_barang(self):
        print(f"Barang: {self.nama_barang}")
        print(f"Brand: {self.brand}")
        print(f"Stok: {self.stok}")
        print(f"Harga: Rp {self.harga:,.2f}")

    def cek_stok(self):
        return self.stok <= 1

class HandSanitizer(Delarosa):
    def __init__(self, brand, stok, harga):
        super().__init__("Hand Sanitizer", brand, stok, harga)

class BanMobil(Delarosa):
    def __init__(self, brand, stok, harga):
        super().__init__("Ban Mobil", brand, stok, harga)

class BuahBuahan(Delarosa):
    def __init__(self, brand, stok, harga):
        super().__init__("Buah-buahan", brand, stok, harga)

class BotolMinumanBayi(Delarosa):
    def __init__(self, brand, stok, harga):
        super().__init__("Botol Minuman Bayi", brand, stok, harga)

class LaporanPengeluaran:
    def __init__(self):
        self.pengeluaran_bulanan = 0
        self.laporan_terjual = []

    def tambah_pengeluaran(self, barang, jumlah):
        total_harga = barang.harga * jumlah
        self.pengeluaran_bulanan += total_harga
        self.laporan_terjual.append((barang.nama_barang, barang.brand, jumlah, total_harga))

    def cetak_laporan(self):
        print("\nLaporan Pengeluaran Bulanan:")
        if not self.laporan_terjual:
            print("Tidak ada barang yang terjual bulan ini.")
        else:
            for nama, brand, jumlah, total in self.laporan_terjual:
                print(f"{nama} (Brand: {brand}) - Jumlah Terjual: {jumlah}, Total Harga: Rp {total:,.2f}")
        print(f"\nTotal Pengeluaran Bulanan: Rp {self.pengeluaran_bulanan:,.2f}")


def pantau_stok(barang_list):
    print("\nBarang yang hampir habis:")
    stok_hampir_habis = False
    for barang in barang_list:
        if barang.cek_stok():
            print(f"{barang.nama_barang} (Brand: {barang.brand}, Stok: {barang.stok}) hampir habis.")
            stok_hampir_habis = True
    if not stok_hampir_habis:
        print("Semua barang dalam stok aman.")

hand_sanitizer = HandSanitizer("Dettol", 2, 20000)
ban_mobil = BanMobil("Bridgestone", 1, 800000)
buah_buahan = BuahBuahan("Tropicana", 10, 50000)
botol_bayi = BotolMinumanBayi("Pigeon", 0, 15000)

barang_list = [hand_sanitizer, ban_mobil, buah_buahan, botol_bayi]

laporan = LaporanPengeluaran()

laporan.tambah_pengeluaran(hand_sanitizer, 1)
laporan.tambah_pengeluaran(ban_mobil, 1)
laporan.tambah_pengeluaran(buah_buahan, 5)

pantau_stok(barang_list)

laporan.cetak_laporan()
