class Barang:
    def __init__(self, kodeBarang,namaBarang, jumlahBarang,):
        self.kodeBarang = kodeBarang
        self.namaBarang = namaBarang
        self.jumlahBarang = jumlahBarang
       
class PencarianBarang:
    def __init__(self, daftarBarang):
        self.daftarBarang = daftarBarang
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.daftarBarang):
            raise StopIteration
        barang = self.daftarBarang[self.index]
        self.index += 1
        return barang

    def cariBarangHabis(self):
        for barang in self:
            if barang.jumlahBarang <= 0:
                print(f"Barang {barang.namaBarang} sudah habis.")
            else:
                print(f"Barang {barang.namaBarang} masih ada stok: {barang.jumlahBarang} buah.")

def main():
    daftarBarang = [
        Barang("1AD","Hand Sanitizer", 0),
        Barang("1AY", "Mobil", 2),
        Barang("1AO","Buah-Buahan", 5),
        Barang("1BP","Botol Minuman", 1),
        Barang("1UE","Laptop", 0)
    ]

    pencarianBarang = PencarianBarang(daftarBarang)
    pencarianBarang.cariBarangHabis()


main()
