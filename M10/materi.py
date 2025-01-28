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

    def get_attribute(self, attr):
        # Rekursif untuk mencari atribut pada objek asli
        if hasattr(self._proses, attr):
            return getattr(self._proses, attr)
        elif isinstance(self._proses, cekTahun):
            return self._proses.get_attribute(attr)
        else:
            raise AttributeError(f"Atribut '{attr}' tidak ditemukan.")

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
        stok = self.get_attribute("stok")
        stok_status = "Tersedia" if stok > 0 else "Habis"
        hasil += f"Stok buku: {stok_status}\n"
        return hasil

if __name__ == '__main__':
    buku1 = BUKU("Pemrograman Python", 2019, 3)

    denganPemilik = cekTahunPemilik(buku1)
    denganManajemen = cekTahunManajemen(buku1)
    denganCekJumlah = cekStok(buku1)
    denganCekSemua = cekStok(cekTahunPemilik(buku1))

    print("Awal : \n", buku1.cetakBuku())
    print("Dengan Cek Tahun Pemilik: \n", denganPemilik.cetakBuku())
    print("Dengan Cek Tahun Manajemen: \n", denganManajemen.cetakBuku())
    print("Dengan Cek Jumlah : \n", denganCekJumlah.cetakBuku())
    print("Dengan Cek Semua : \n", denganCekSemua.cetakBuku())
