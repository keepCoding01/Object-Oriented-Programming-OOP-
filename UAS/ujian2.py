from tabulate import tabulate

class Transaksi:
    def inputId(self, idBarang):
        return idBarang

    def inputNama(self, namaBarang):
        return namaBarang

    def inputJumlah(self, jumlahBarang):
        return jumlahBarang

    def inputKategori(self, kategoriBarang, subkategoriBarang):
        return {"kategori": kategoriBarang, "subkategori": subkategoriBarang}

    def tambahan(self, extraInfo):
        return extraInfo

    def mulai(self, idBarang, namaBarang, jumlahBarang, kategoriBarang, subkategoriBarang, extraInfo):
        idbrg = self.inputId(idBarang)
        namabrg = self.inputNama(namaBarang)
        jlhbrg = self.inputJumlah(jumlahBarang)
        kategoribrg = self.inputKategori(kategoriBarang, subkategoriBarang)
        tambahanbrg = self.tambahan(extraInfo)
        return idbrg, namabrg, jlhbrg, kategoribrg, tambahanbrg

class Masuk(Transaksi):
    def tambahan(self, extraInfo):
        return f"Barang masuk pada {extraInfo}"

class Keluar(Transaksi):
    def tambahan(self, extraInfo):
        return f"Barang keluar pada {extraInfo}"

def logDecorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

class Gudang:
    def __init__(self):
        self.listBarang = []

    @logDecorator
    def barangMasuk(self, idBarang, namaBarang, jumlahBarang, kategoriBarang, subkategoriBarang, waktu):
        transaksi = Masuk()
        dataBarang = transaksi.mulai(idBarang, namaBarang, jumlahBarang, kategoriBarang, subkategoriBarang, waktu)
        self.listBarang.append({
            "id": dataBarang[0], 
            "nama": dataBarang[1], 
            "jumlah": dataBarang[2], 
            "kategori": dataBarang[3]['kategori'], 
            "subkategori": dataBarang[3]['subkategori']
        })
        return f"Barang dengan ID {dataBarang[0]} telah masuk."

    @logDecorator
    def barangKeluar(self, idBarang, namaBarang, jumlahBarang, waktu):
        if not self.listBarang: 
            print("Gudang masih kosong, silakan tambah barang di menu 1.")
            return 

        transaksi = Keluar()
        dataBarang = transaksi.mulai(idBarang, namaBarang, jumlahBarang, '', '', waktu)  
        for barang in self.listBarang:
            if barang["id"] == dataBarang[0] and barang["nama"] == dataBarang[1]:
                if barang["jumlah"] >= dataBarang[2]:
                    barang["jumlah"] -= dataBarang[2]
                    if barang["jumlah"] == 0:
                        self.listBarang.remove(barang)
                    return f"Barang dengan ID {dataBarang[0]} telah keluar."
                else:
                    return "Jumlah barang tidak mencukupi."
        return "Barang tidak ditemukan di gudang."

    def detail(self):
        return self.listBarang

def tampilkanMenu():
    headers = ["No", "Menu", "Deskripsi"]
    data = [
        ["1", "Barang Masuk", "Menambahkan barang ke gudang"],
        ["2", "Barang Keluar", "Mengeluarkan barang dari gudang"],
        ["3", "Lihat Detail Barang", "Melihat daftar barang di gudang"],
        ["4", "Keluar", "Keluar dari program"]
    ]
    print(tabulate(data, headers, tablefmt="grid"))

gudang = Gudang()
while True:
    tampilkanMenu()  

    pilihan = input("\nPilih menu: ")

    if pilihan == "1":
        idBarang = int(input("Masukkan ID Barang: "))
        namaBarang = input("Masukkan Nama Barang: ")
        jumlahBarang = int(input("Masukkan Jumlah Barang: "))
        
        print("Pilih kategori barang:")
        print("1. Makanan")
        print("2. Kosmetik")
        print("3. Alat Tulis Kantor (ATK)")
        kategoriPilihan = input("Pilih kategori (1/2/3): ")

        if kategoriPilihan == "1":
            kategoriBarang = "Makanan"
            subkategoriBarang = input("Masukkan subkategori (misal: Cemilan, Minuman): ")
        elif kategoriPilihan == "2":
            kategoriBarang = "Kosmetik"
            subkategoriBarang = input("Masukkan subkategori (misal: Skincare, Makeup): ")
        elif kategoriPilihan == "3":
            kategoriBarang = "Alat Tulis Kantor (ATK)"
            subkategoriBarang = input("Masukkan subkategori (misal: Pensil, Kertas): ")
        else:
            print("Kategori tidak valid!")
            continue

        waktu = input("Masukkan Waktu (misal: 20 Januari 2025): ")
        print(gudang.barangMasuk(idBarang, namaBarang, jumlahBarang, kategoriBarang, subkategoriBarang, waktu))

    elif pilihan == "2":
        idBarang = int(input("Masukkan ID Barang: "))
        namaBarang = input("Masukkan Nama Barang: ")
        jumlahBarang = int(input("Masukkan Jumlah Barang: "))
        waktu = input("Masukkan Waktu (misal: 22 Januari 2025): ")
        result = gudang.barangKeluar(idBarang, namaBarang, jumlahBarang, waktu) 

        if result: 
            print(result)  

    elif pilihan == "3":
        detailBarang = gudang.detail()
        if detailBarang:
            detailBarangTabel = [
                [barang["id"], barang["nama"], barang["jumlah"], barang["kategori"], barang["subkategori"]] 
                for barang in detailBarang
            ]
            print(tabulate(detailBarangTabel, headers=["ID", "Nama Barang", "Jumlah", "Kategori", "Subkategori"], tablefmt="grid"))
        else:
            print("Gudang masih kosong.")

    elif pilihan == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan kamu tidak valid nihh. Silakan coba lagi yaaa.")
