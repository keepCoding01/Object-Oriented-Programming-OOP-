class BUKU :
    perpus = []
    def inputBuku(self, kodeBuku, namaBuku, jenisBuku):
        tmp = {"kode" : kodeBuku, "nama" : namaBuku, "jenis":jenisBuku}
        self.perpus.append(tmp)

    def cetakBuku(self):
        for i in range(len(self.perpus)):
            print(f"Buku ke-{i+1}:")
            print(f"Kode Buku = {self.perpus[i]['kode']}")
            print(f"Nama Buku = {self.perpus[i]['nama']}")
            print(f"Jenis Buku = {self.perpus[i]['jenis']}")
            print()

    def urutBuku(self):
        self.perpus = sorted(self.perpus, key = lambda d : d['kode'])
    

hlib = BUKU()
hlib.inputBuku("P023", "Pemrograman C", "Pembelajaran")
hlib.inputBuku("K030", "Doraemon", "Komik")
hlib.inputBuku("D067", "Asal Mula Air Hujan", "Dongeng")
hlib.inputBuku("P001", "Pemrograman Python", "Pembelajaran")

print("Sebelum diurutkan")
hlib.cetakBuku()

print("\n\nSetelah diurutkan")
hlib.urutBuku()
hlib.cetakBuku()