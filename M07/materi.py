class BUKU:
    perpus = []

    def inputBuku(self):
        while True:
            kodeBuku = yield "Kode buku" 
            for buku in self.perpus:
                if buku['kode'] == kodeBuku:
                    print("Kode Buku sudah terdaftar....!!!")
                    continue
            namaBuku = yield "Nama buku"  
            jenisBuku = yield "Jenis buku"  
            tmp = {"kode": kodeBuku, "nama": namaBuku, "jenis": jenisBuku}
            self.perpus.append(tmp)

    def cetakBuku(self):
        for i, buku in enumerate(self.perpus, start=1):
            print(f"Buku ke-{i}:")
            print(f"Kode Buku = {buku['kode']}")
            print(f"Nama Buku = {buku['nama']}")
            print(f"Jenis Buku = {buku['jenis']}")
            print()

a = BUKU()
b = a.inputBuku()
next(b) 
b.send('IF001')  
b.send('Pemrograman Python')  
b.send('Pemrograman')  
a.cetakBuku()  


b = a.inputBuku()
print(b)
next(b)
# b.send("IF001")
b.send("IF002")
b.send("Bahasa C")
b.send("Pemrograman")
a.cetakBuku() 


# hlib = BUKU()
# hlib.inputBuku("P023", "Pemrograman C", "Pembelajaran")
# hlib.inputBuku("K030", "Doraemon", "Komik")
# hlib.inputBuku("D067", "Asal Mula Air Hujan", "Dongeng")
# hlib.inputBuku("P001", "Pemrograman Python", "Pembelajaran")

# print("Sebelum diurutkan")
# hlib.cetakBuku()

# print("\n\nSetelah diurutkan")
# hlib.urutBuku()
# hlib.cetakBuku()