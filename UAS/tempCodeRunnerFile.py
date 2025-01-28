class Transaksi:
    def inputId(self, idBarang):
        return idBarang

    def inputNama(self, namaBarang):
        return namaBarang

    def inputJumlah(self, jumlahBarang):
        return jumlahBarang

    def tambahan(self, extraInfo):
        return extraInfo

    def mulai(self, idBarang, namaBarang, jumlahBarang, extraInfo):
        idResult = self.inputId(idBarang)
        namaResult = self.inputNama(namaBarang)
        jumlahResult = self.inputJumlah(jumlahBarang)
        tambahanResult = self.tambahan(extraInfo)
        return idResult, namaResult, jumlahResult, tambahanResult

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
    def barangMasuk(self, idBarang, namaBarang, jumlahBarang, waktu):
        transaksi = Masuk()
        dataBarang = transaksi.mulai(idBarang, namaBarang, jumlahBarang, waktu)
        self.listBarang.append({"id": dataBarang[0], "nama": dataBarang[1], "jumlah": dataBarang[2]})
        return f"Barang dengan ID {dataBarang[0]} telah masuk."
        

    @logDecorator
    def barangKeluar(self, idBarang, namaBarang, jumlahBarang, waktu):
        if not self.listBarang: 
            print("Gudang masih kosong, silakan tambah barang di menu 1.")
            return 

        transaksi = Keluar()
        dataBarang = transaksi.mulai(idBarang, namaBarang, jumlahBarang, waktu)
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


    gudang = Gudang()
    while True:
        print("\nMenu:")
        print("1. Barang Masuk")
        print("2. Barang Keluar")
        print("3. Lihat Detail Barang")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            idBarang = int(input("Masukkan ID Barang: "))
            namaBarang = input("Masukkan Nama Barang: ")
            jumlahBarang = int(input("Masukkan Jumlah Barang: "))
            waktu = input("Masukkan Waktu (misal: 20 Januari 2025): ")
            print(gudang.barangMasuk(idBarang, namaBarang, jumlahBarang, waktu))

        elif pilihan == "2":
            idBarang = int(input("Masukkan ID Barang: "))
            namaBarang = input("Masukkan Nama Barang: ")
            jumlahBarang = int(input("Masukkan Jumlah Barang: "))
            waktu = input("Masukkan Waktu (misal: 22 Januari 2025): ")
            result = gudang.barangKeluar(idBarang, namaBarang, jumlahBarang, waktu)  # Jangan langsung print di sini

            if result:  # Jika ada hasil, tampilkan
                print(result)  # Menampilkan hasil jika ada

        elif pilihan == "3":
            print("Detail Barang:", gudang.detail())

        elif pilihan == "4":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
