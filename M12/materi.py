from datetime import datetime
from abc import ABC, abstractmethod


class BUKU:
    def __init__(self, judul, tahun, stok):
        self.judul = judul
        self.tahun = tahun
        self.stok = stok

    def cetakBuku(self):
        return f"Judul: {self.judul}\nTahun: {self.tahun}\nStok: {self.stok}\n"


class KartuBuku(ABC):
    @abstractmethod
    def cetakKartu(self):
        pass


class KodeBuku(KartuBuku):
    def cetakKartu(self, buku):
        print(f"Kode Buku = {buku.judul[0:3].upper() + str(buku.tahun)}")


class DataBuku(KartuBuku):
    def cetakKartu(self, buku):
        print(f"Nama Buku = {buku.judul}")
        print(f"Jumlah Buku = {buku.stok}")


class FactoryKartuBuku(ABC):
    @abstractmethod
    def buatKodeBuku(self):
        pass

    @abstractmethod
    def buatDataBuku(self):
        pass


class AfdKartuBuku(FactoryKartuBuku):
    def buatKodeBuku(self):
        return KodeBuku()

    def buatDataBuku(self):
        return DataBuku()


class CekTahun:
    def __init__(self, proses):
        self._proses = proses

    def cetakBuku(self):
        return self._proses.cetakBuku()

    def get_asli(self):
        if isinstance(self._proses, CekTahun):
            return self._proses.get_asli()
        return self._proses


class CekTahunPemilik(CekTahun):
    def cetakBuku(self):
        hasil = self._proses.cetakBuku()
        thn_sekarang = datetime.now().year
        kategori = "Baru" if (thn_sekarang - self._proses.tahun) <= 5 else "Lama"
        hasil += f"Buku terbit pada tahun {self._proses.tahun}, sehingga termasuk buku {kategori}\n"
        return hasil


class CekTahunManajemen(CekTahun):
    def cetakBuku(self):
        hasil = self._proses.cetakBuku()
        thn_sekarang = datetime.now().year
        kategori = "Baru" if (thn_sekarang - self._proses.tahun) <= 3 else "Lama"
        hasil += f"Buku terbit pada tahun {self._proses.tahun}, sehingga termasuk buku {kategori}\n"
        return hasil


class CekStok(CekTahun):
    def cetakBuku(self):
        hasil = self._proses.cetakBuku()
        stok = self.get_asli().stok
        stok_status = "Tersedia" if stok > 0 else "Habis"
        hasil += f"Stok buku: {stok_status}\n"
        return hasil


class FacadeCekTahun:
    def __init__(self, buku):
        self.denganPemilik = CekTahunPemilik(buku)
        self.denganManajemen = CekTahunManajemen(buku)

    def proses(self):
        print("Saran dari \"Pemilik\" = ")
        print(self.denganPemilik.cetakBuku())
        print("\nSaran dari \"Manajemen\" = ")
        print(self.denganManajemen.cetakBuku())
        print()


if __name__ == '__main__':
    buku1 = BUKU("Pemrograman Python", 2019, 3)
    cekThn = FacadeCekTahun(buku1)
    denganCekJumlah = CekStok(buku1)
    denganPemilik = CekTahunPemilik(buku1)
    denganManajemen = CekTahunManajemen(buku1)
    denganCekSemua = CekStok(CekTahunPemilik(buku1))

    print("Awal : \n", buku1.cetakBuku())
    print()
    cekThn.proses()
    print("Dengan Cek Jumlah : \n", denganCekJumlah.cetakBuku())
    print("Dengan Cek Tahun Pemilik: \n", denganPemilik.cetakBuku())
    print("Dengan Cek Tahun Manajemen: \n", denganManajemen.cetakBuku())
    print("Dengan Cek Semua : \n", denganCekSemua.cetakBuku())

    ctkKrt = AfdKartuBuku()
    kdBuku = ctkKrt.buatKodeBuku()
    dataBuku = ctkKrt.buatDataBuku()
    print("\nKartu Buku")
    kdBuku.cetakKartu(buku1)
    dataBuku.cetakKartu(buku1)
