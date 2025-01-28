class TasyaSyafriza:
    def __init__(self):
        self.barang = []

    def pemasukanData(self, dataBarang):
        for kode, nama, jenis, stok in dataBarang:
            yield {
                'kode': kode,
                'nama': nama,
                'jenis': jenis,
                'stok': stok
            }

    def cariYangHampirHabis(self):
        barangHampirHabis = []
        for item in self.barang:
            if item['stok'] <= 5:
                barangHampirHabis.append(item)
        return barangHampirHabis

    def pengurutanJenis(self):
        n = len(self.barang)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.barang[j]['jenis'] > self.barang[j + 1]['jenis']:
                    self.barang[j], self.barang[j + 1] = self.barang[j + 1], self.barang[j]
        return self.barang

    def totalStok(self):
        total = sum(item['stok'] for item in self.barang)
        return total

    def tampilkanBarang(self):
        print("-" * 50)
        for item in self.barang:
            print(f"{item['kode']} | {item['nama']} \t| {item['jenis']} \t| {item['stok']}")

dataBarang = [
    ("001", "Hand Sanitizer", "Kesehatan", 3),
    ("002", "Ban Mobil", "Otomotif", 10),
    ("003", "Buah Apel", "Makanan", 2),
    ("004", "Botol Minum Bayi", "Alat Bayi", 6),
    ("005", "Mobil Mainan", "Mainan", 4)
]

kedai = TasyaSyafriza()
generator = kedai.pemasukanData(dataBarang)

for item in generator:
    kedai.barang.append(item)

print("\nData Barang Sebelum Pengurutan")
kedai.tampilkanBarang()

print("\nData Barang Setelah Pengurutan Berdasarkan Jenis")
urutBarang = kedai.pengurutanJenis()
kedai.tampilkanBarang()  

print("\nBarang yang Stoknya Hampir Habis")
barangHampirHabis = kedai.cariYangHampirHabis()
print("-" * 50)
for item in barangHampirHabis:
    print(f"{item['kode']} | {item['nama']} \t| {item['jenis']} \t| {item['stok']}")

print("\nTotal Stok Barang di Gudang")
print("-" * 50)
totalStokBarang = kedai.totalStok()
print(f"Total Stok: {totalStokBarang}")
