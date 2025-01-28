from datetime import datetime

class BUKU:
    def __init__(self, judul, tahun, stok):
        self.judul = judul
        self.tahun = tahun
        self.stok = stok

    def cetakBuku(self):
        return f"Judul: {self.judul}\nTahun: {self.tahun}\nStok: {self.stok}\n"


class cekTahun:
    def __init__(self, proses):
        self._proses = proses

    def cetakBuku(self):
        return self._proses.cetakBuku()

    def get_asli(self):
        # Kembalikan objek asli dengan rekursif
        if isinstance(self._proses, cekTahun):
            return self._proses.get_asli()
        return self._proses


class cekTahunPemilik(cekTahun):
    def cetakBuku(self):
        hasil = self._proses.cetakBuku()
        thn_sekarang = datetime.now().year
        kategori = "Baru" if (thn_sekarang - self._proses.tahun) <= 5 else "Lama"
        hasil += f"Buku terbit pada tahun {self._proses.tahun}, sehingga termasuk buku {kategori}\n"
        return hasil


class cekTahunManajemen(cekTahun):
    def cetakBuku(self):
        hasil = self._proses.cetakBuku()
        thn_sekarang = datetime.now().year
        kategori = "Baru" if (thn_sekarang - self._proses.tahun) <= 3 else "Lama"
        hasil += f"Buku terbit pada tahun {self._proses.tahun}, sehingga termasuk buku {kategori}\n"
        return hasil


class cekStok(cekTahun):
    def cetakBuku(self):
        hasil = self._proses.cetakBuku()
        stok = self.get_asli().stok  # Ambil stok dari objek asli
        stok_status = "Tersedia" if stok > 0 else "Habis"
        hasil += f"Stok buku: {stok_status}\n"
        return hasil


class facadeCekTahun:
    def __init__(self, buku):
        self.denganPemilik = cekTahunPemilik(buku)
        self.denganManajemen = cekTahunManajemen(buku)

    def proses(self):
        print("Saran dari \"Pemilik\" = ")
        print(self.denganPemilik.cetakBuku())
        print("\nSaran dari \"Manajemen\" = ")
        print(self.denganManajemen.cetakBuku())
        print()


if __name__ == '__main__':
    buku1 = BUKU("Pemrograman Python", 2019, 3)
    cekThn = facadeCekTahun(buku1)
    denganCekJumlah = cekStok(buku1)
    denganPemilik = cekTahunPemilik(buku1)
    denganManajemen = cekTahunManajemen(buku1)
    denganCekSemua = cekStok(cekTahunPemilik(buku1))

    print("Awal : \n", buku1.cetakBuku())
    print()
    cekThn.proses()
    print("Dengan Cek Jumlah : \n", denganCekJumlah.cetakBuku())
    print("Dengan Cek Tahun Pemilik: \n", denganPemilik.cetakBuku())
    print("Dengan Cek Tahun Manajemen: \n", denganManajemen.cetakBuku())
    print("Dengan Cek Semua : \n", denganCekSemua.cetakBuku())
