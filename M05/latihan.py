buku = []
buku += ["Pemrograman dengan Python"]
buku += ["Struktur data"]
buku += ["Data Mining"]
buku += ["Visualisasi Data"]
buku += ["Pengolahan Citra"]
buku += ["Kecerdasan Buatan"]
buku += ["Pemrograman Web"]

# Melakukan pencarian buku dalam array bukus
def cariBuku(bukus,buku) :
    items = iter(bukus)
    i = 0
    while True:
        try:
            if (next(items) == buku):
                print(f"Buku\"{buku}\" ditemukan pada tumpukan ke-{i+1}...!!!")
                break
            i += 1
        except StopIteration:
            print(f"Buku\"{buku}\" tidak ditemukan...!!!")
            break

cariBuku(buku, "Database")
cariBuku(buku, "Struktur data")
cariBuku(buku, "Pemrograman C")
