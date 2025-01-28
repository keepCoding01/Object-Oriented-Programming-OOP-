from abc import ABCMeta, abstractmethod
import os
 
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
 
class AbstractBarang(metaclass=ABCMeta):
    @abstractmethod
    def detail(self):
        pass
 
class AbstractTipeJenis(metaclass=ABCMeta):
    @abstractmethod
    def tambah(self, item):
        pass
 
    @abstractmethod
    def hapus(self, item):
        pass
 
class Gudang:
    def __init__(self):
        self.listBarang = []
 
    def tambahBarang(self, barang):
        self.listBarang.append(barang)
 
    def detail(self):
        if not self.listBarang:
            print("Tidak ada barang.")
        else:
            print("Daftar barang:")
            for barang in self.listBarang:
                barang.detail()
 
class JenisBarang(AbstractBarang, AbstractTipeJenis):
    def __init__(self, nama):
        self.nama = nama
        self.listTipe = []
 
    def tambah(self, item):
        self.listTipe.append(item)
 
    def hapus(self, item):
        self.listTipe.remove(item)
 
    def detail(self):
        print(self.nama)
        for tipe in self.listTipe:
            tipe.detail()
 
class TipeBarang(AbstractBarang, AbstractTipeJenis):
    def __init__(self, nama):
        self.nama = nama
        self.listSeri = []
 
    def tambah(self, item):
        self.listSeri.append(item)
 
    def hapus(self, item):
        self.listSeri.remove(item)
 
    def detail(self):
        print(f"  {self.nama}")
        for seri in self.listSeri:
            seri.detail()
 
class SeriBarang(AbstractBarang):
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
 
    def detail(self):
        print(f"    {self.nama} ({self.harga})")
 
clr()
gudang = Gudang()
 
while True:
    print("\nMenu (Abstract Factory & Composite):")
    print("1. Tambah Barang")
    print("2. Detail Barang")
    print("3. Keluar")
    pilihan = input("Pilihan: ")
 
    if pilihan == "1":
        print("Menu Tambah Barang")
        print("="*20)
        namaBarang = input("Jenis: ")
        jenis = input("Tipe: ")
        seri = input("Seri: ")
        harga = input("Harga: ")
 
        barang = next((b for b in gudang.listBarang if b.nama == namaBarang), None)
 
        if barang is None:
            barang = JenisBarang(namaBarang)
            gudang.tambahBarang(barang)
            print("Jenis barang baru!")
 
        tipe = next((t for t in barang.listTipe if t.nama == jenis), None)
        if tipe is None:
            tipe = TipeBarang(jenis)
            barang.tambah(tipe)
            print("Tipe baru ditambahkan!")
 
        tipe.tambah(SeriBarang(seri, harga))
        print("Seri barang baru ditambahkan!")
 
        totalJenisBarang = len(gudang.listBarang)
        print("Barang berhasil ditambahkan!")
        print(f"Jumlah jenis barang saat ini: {totalJenisBarang}")
 
        input("\nTekan enter untuk kembali ke menu!")
        clr()
 
    elif pilihan == "2":
        clr()
        gudang.detail()
        input("\nTekan enter untuk kembali ke menu!")
 
    elif pilihan == "3":
        print("Keluar dari program.")
        break
 
    else:
        print("Pilihan tidak valid.")
 
