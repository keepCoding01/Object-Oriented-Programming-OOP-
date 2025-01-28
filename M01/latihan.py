class Gudang:
    def __init__(self):
        self.data = []
        self.nomorToko = 1
    
    def cari(self, namaBarang):
        # Perulangan sejumlah barang di gudang
        for i in range(0, len(self.data)):
            if self.data[i].nama == namaBarang:  # Pengecekan nama barang
                print(f"Nama Barang: {self.data[i].nama}")
                print(f"Brand: {self.data[i].brand}")
                print(f"Jumlah: {self.data[i].jumlah}\n")

    def tambahBarang(self, barang):
        self.data.append(barang)  # Tambah barang baru ke gudang
    
    def barangKeluar(self, namaBarang, jumlah):
        for i in range(len(self.data)):
            if self.data[i].nama == namaBarang:  # Pengecekan nama barang
                if self.data[i].jumlah >= jumlah:  # Cek apakah jumlah cukup
                    self.data[i].jumlah -= jumlah   # Mengurangi jumlah barang
                    print(f"{jumlah} {namaBarang} berhasil dikeluarkan.")
                else:
                    print(f"Jumlah barang {namaBarang} tidak mencukupi. Tersedia: {self.data[i].jumlah}")
                return
        print(f"Barang dengan nama '{namaBarang}' tidak ditemukan.")


class Komputer:
    def __init__(self):
        self.nama = "Komputer"
        self.ram = 16
        self.storage = 1
        self.brand = "HP"
        self.jumlah = 10


class BarangLain:
    def __init__(self, nama, brand, jumlah):
        self.nama = nama
        self.brand = brand
        self.jumlah = jumlah


# Main Program
toko = Gudang()
objek1 = Komputer()
objek2 = Komputer()
objek2.brand = "Samsung"

# Menambah barang awal
toko.tambahBarang(objek1)
toko.tambahBarang(objek2)

status = True
while status:
    print("\nMenu Gudang PT.XYZ")
    print("1. Cari Barang")
    print("2. Simpan Barang")
    print("3. Keluarkan Barang")
    print("4. Keluar")
    print("Pilihan: ", end="")
    
    pil = input()
    
    if pil == "1":
        print("Cari Barang")
        nama = input("Nama Barang: ")
        toko.cari(nama)
        input("Tekan enter untuk kembali ke menu!")
    
    elif pil == "2":
        print("Simpan Barang")
        nama = input("Nama Barang: ")
        brand = input("Brand: ")
        jlh = int(input("Jumlah: "))  # Pastikan input jumlah adalah integer
        
        barangUser = BarangLain(nama, brand, jlh)
        toko.tambahBarang(barangUser)
        
        print(f"Barang '{nama}' berhasil ditambahkan.\n")
        input("Tekan enter untuk kembali ke menu!")
    
    elif pil == "3":
        print("Keluarkan Barang")
        nama = input("Nama Barang: ")
        jlh = int(input("Jumlah Barang: "))
        toko.barangKeluar(nama, jlh)
        input("Tekan enter untuk kembali ke menu!")
    
    elif pil == "4":
        status = False
        print("Program selesai.")
    
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
