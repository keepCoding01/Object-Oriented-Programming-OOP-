class TasyaSyafriza:
    def __init__(self):
        self.barang = []
 
    def pemasukanData(self, kode, nama, jenis, stok):
        self.barang.append({
            'kode': kode,
            'nama': nama,
            'jenis': jenis,
            'stok': stok
        })
 
    def cariYangHampirHabis(self):
        barangHampirHabis = []
        iterator = iter(self.barang)
        while True:
            try:
                i = next(iterator)
                if i['stok'] <= 5:  
                    barangHampirHabis.append(i)
            except StopIteration:
                break
        return barangHampirHabis
 
    def pengurutanJenis(self):
        n = len(self.barang)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.barang[j]['jenis'] > self.barang[j + 1]['jenis']:
                    self.barang[j], self.barang[j + 1] = self.barang[j + 1], self.barang[j]
        return self.barang
 
    def tampilkanBarang(self):
        iterator = iter(self.barang) 
        while True:
            try:
                i = next(iterator)
                print(f"{i['kode']} | {i['nama']} \t| {i['jenis']} \t| {i['stok']}")
            except StopIteration:
                break
 
kedai = TasyaSyafriza()
 
kedai.pemasukanData("001", "Hand Sanitizer", "Kesehatan", 3)
kedai.pemasukanData("002", "Ban Mobil", "Otomotif", 10)
kedai.pemasukanData("003", "Buah Apel", "Makanan", 2)
kedai.pemasukanData("004", "Botol Minum Bayi", "Alat Bayi", 6)
kedai.pemasukanData("005", "Mobil Mainan", "Mainan", 4)
 
print("\nData Barang Sebelum Pengurutan")
print("-"*50)
kedai.tampilkanBarang()
 
print("\nData Barang Setelah Pengurutan Berdasarkan Jenis")
print("-"*50)
urutBarang = kedai.pengurutanJenis()
for i in urutBarang:
    print(f"{i['kode']} | {i['nama']} \t| {i['jenis']} \t| {i['stok']}")
 
print("\nBarang yang Stoknya Hampir Habis")
print("-"*50)
barangHampirHabis = kedai.cariYangHampirHabis()
for i in barangHampirHabis:
    print(f"{i['kode']} | {i['nama']} \t| {i['jenis']} \t| {i['stok']}")

print("\n")
