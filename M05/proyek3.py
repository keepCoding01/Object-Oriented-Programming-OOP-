from pathlib import Path

class Dagang:
    def __init__(self):
        self.barangDagang = {
            "f001": {"namaBarang": "Hand Sanitizer", "jumlahStok": 26},
            "f002": {"namaBarang": "Ban Mobil", "jumlahStok": 8},
            "f003": {"namaBarang": "Buah-buahan", "jumlahStok": 17},
            "f004": {"namaBarang": "Botol Minum Bayi", "jumlahStok": 14},
            "f005": {"namaBarang": "Televisi", "jumlahStok": 2}
        }

    def inputJumlahStok(self, prompt):
        while True:
            try:
                jumlahStok = int(input(prompt))
                return jumlahStok
            except ValueError:
                print("Aduhh inputan kamu tidak valid nih. Harap masukkan angka saja untuk jumlah stok ya.")

    def tulisKeFile(self, daftar):
        path = Path(__file__).parent.absolute()
        with open(f"{path}/db.txt", "w") as f:
            for item in daftar:
                f.write(item + "\n")

    def updateFile(self):
        path = Path(__file__).parent.absolute()
        with open(f"{path}/db.txt", "w") as f:
            for kodeBarang, dataBarang in self.barangDagang.items():
                f.write(f"{kodeBarang} | {dataBarang['namaBarang']} | {dataBarang['jumlahStok']}\n")

    def resetFile(self):
        path = Path(__file__).parent.absolute()
        with open(f"{path}/db.txt", "w") as f:
            pass

class TambahBarang(Dagang):
    def __init__(self, gudang):
        self.barangDagang = gudang.barangDagang
        
    def tambahBarang(self):
        kodeBarang = input("\nMasukkan kode barang yang baru: ")
        if kodeBarang in self.barangDagang:
            print(f"Ehh, barang dengan kode {kodeBarang} sudah ada di gudang ya.")
            print("Silakan gunakan menu 'Barang Masuk' untuk menambah stok (●'◡'●).")
        else:
            namaBarang = input("Masukkan nama barang yang baru: ")
            jumlahStok = self.inputJumlahStok("Masukkan jumlah stok awal: ")
            self.barangDagang[kodeBarang] = {"namaBarang": namaBarang, "jumlahStok": jumlahStok}
            print(f"Yeayyy, {namaBarang} berhasil ditambahkan ke db.txt dengan stok {jumlahStok} (*^_^*).")
            self.updateFile()

class DaftarBarang(Dagang):
    def __init__(self, gudang):
        self.barangDagang = gudang.barangDagang
    
    def daftarBarang(self):
        if not self.barangDagang:
            print("\nWaduh sepertinya gudangnya kosong deh, belum ada barang yang terdaftar >︿<.")
        else:
            print("\nDaftar barang telah ditulis ke db.txt yaaa, coba kamu cek deh.")
            print("Ini daftar barang yang ada di gudang:\n")
            iterator = iter(DaftarBarangIterator(self.barangDagang))
            daftar = []  
            while True:
                try:
                    item = next(iterator)
                    print(item)
                    daftar.append(item)
                except StopIteration:
                    break
            self.tulisKeFile(daftar)

class BarangMasuk(Dagang):
    def __init__(self, gudang):
        self.barangDagang = gudang.barangDagang
    
    def barangMasuk(self):
        kodeBarang = input("\nMasukkan kode barang: ")
        if kodeBarang in self.barangDagang:
            jumlahStok = self.inputJumlahStok(f"Masukkan jumlah stok yang akan ditambah untuk {self.barangDagang[kodeBarang]['namaBarang']}: ")
            self.barangDagang[kodeBarang]["jumlahStok"] += jumlahStok
            print(f"Yeayyy, stok {self.barangDagang[kodeBarang]['namaBarang']} berhasil ditambah ke db.txt. Total stok sekarang: {self.barangDagang[kodeBarang]['jumlahStok']} ^_^.")
            self.updateFile()
        else:
            print(f"Upsss, barang dengan kode {kodeBarang} tidak ditemukan. Silakan tambahkan barang baru terlebih dahulu.")

class BarangKeluar(Dagang):
    def __init__(self, gudang):
        self.barangDagang = gudang.barangDagang
    
    def barangKeluar(self):
        kodeBarang = input("\nMasukkan kode barang: ")
        if kodeBarang in self.barangDagang:
            jumlahStok = self.inputJumlahStok(f"Masukkan jumlah stok yang akan dikeluarkan: ")
            if self.barangDagang[kodeBarang]["jumlahStok"] >= jumlahStok:
                self.barangDagang[kodeBarang]["jumlahStok"] -= jumlahStok
                print(f"Stok barang {self.barangDagang[kodeBarang]['namaBarang']} berhasil dikurangi ya. Sisa stok sekarang: {self.barangDagang[kodeBarang]['jumlahStok']}.")
                print("\nEhh daftar barang telah diperbarui juga loh di db.txt, cek yah (●'◡'●).")
                self.updateFile()
            else:
                print(f"Maaf, stok barang tidak mencukupi. Stok saat ini hanya {self.barangDagang[kodeBarang]['jumlahStok']}. Silakan masukkan jumlah stok yang sesuai ya.")
        else:
            print(f"Barang dengan kode {kodeBarang} tidak ditemukan (~~>_<~~).")

class CekBarang(Dagang):
    def __init__(self, gudang):
        self.barangDagang = gudang.barangDagang
    
    def cekBarang(self):
        kodeBarang = input("\nMasukkan kode barang yang akan di cek: ")
        if kodeBarang in self.barangDagang:
            dataBarang = self.barangDagang[kodeBarang]
            # keys = kita ambil key dalam objek tersebut, yaitu kode barangnya.
            # list = karena barang berbentuk objek, maka kita jadikan list terlebih dahulu.
            # index = setelah berubah jadi list, kita cari kode barang dengan index agar tahu posisinya ada dimana.
            # karena index dimulai dari 0, dan kita maunya penomoran dimulai dari 1, maka tambah dengan 1.
            posisi = list(self.barangDagang.keys()).index(kodeBarang) + 1 
            print(f"Barang berada di posisi ke-{posisi}")  
            print(f"Detail Barang:")
            print(f"Kode Barang : {kodeBarang}")
            print(f"Nama Barang : {dataBarang['namaBarang']}")
            print(f"Jumlah Stok : {dataBarang['jumlahStok']}")
            if dataBarang["jumlahStok"] == 0:
                print("Peringatan (●__●)!!! Stok barang habis, harap segera menambah stok.")
            elif dataBarang["jumlahStok"] < 5:
                print("Peringatan (●__●)!!! Stok barang mau habis, harap segera menambah stok.")
        else:
            print(f"Barang dengan kode {kodeBarang} tidak ditemukan (~~>_<~~).")

class DaftarBarangIterator:
    def __init__(self, barangDagang):
        self.barangDagang = dict(sorted(barangDagang.items(), key=lambda item : item[1]['namaBarang']))
        self.keys = list(self.barangDagang.keys()) 
        self.index = 0

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration()
        kodeBarang = self.keys[self.index]
        data = self.barangDagang[kodeBarang]
        self.index += 1
        return f"{kodeBarang} | {data['namaBarang']} | {data['jumlahStok']}"

    def __iter__(self):
        return self

def menu():
    print("\nMenu Program Kelompok J&T Express=D (★‿★)")
    print("-"*40)
    print("1. Tambah Barang Baru")
    print("2. Daftar Barang")
    print("3. Barang Masuk")
    print("4. Barang Keluar")
    print("5. Cek Barang")
    print("0. Keluar")
    return input("Pilih menu sesuai nomor ya, mau nomor berapa nih(satu aja): ")

gudang = Dagang()

while True:
    pilihan = menu()

    if pilihan == "1":
        TambahBarang(gudang).tambahBarang()

    elif pilihan == "2":
        DaftarBarang(gudang).daftarBarang()

    elif pilihan == "3":
        BarangMasuk(gudang).barangMasuk()

    elif pilihan == "4":
        BarangKeluar(gudang).barangKeluar()

    elif pilihan == "5":
        CekBarang(gudang).cekBarang()

    elif pilihan == "0":
        gudang.resetFile() 
        print("-"*75) 
        print("File db.txt berhasil direset ulang! Program selesai, terima kasih ƪ(˘⌣˘)ʃ.\n")
        break

    else:
        print("Pilihan kamu ga valid deh, silakan coba lagi ya ヾ(＠⌒ー⌒＠).")
