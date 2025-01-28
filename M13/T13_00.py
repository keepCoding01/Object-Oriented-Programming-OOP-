def faktorial(n):
    total = 1
    for i in range(1, n+1):
        total*=i
    return total

class Barang:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama
        self.jumlah = 1
    def tambah(self, n):
        self.jumlah += n
    
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama