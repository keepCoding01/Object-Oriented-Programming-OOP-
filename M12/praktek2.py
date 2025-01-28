# Composite Pattern

from abc import ABC, abstractmethod

class KomponenBiaya(ABC):
    @abstractmethod
    def ambilBiaya(self):
        pass

    @abstractmethod
    def tambah(self, komponen):
        pass

class BiayaSederhana(KomponenBiaya):
    def __init__(self, nama, biaya):
        self.nama = nama
        self.biaya = biaya

    def ambilBiaya(self):
        return self.biaya

    def tambah(self, komponen):
        raise NotImplementedError("Tidak bisa menambahkan ke daun")

    def __str__(self):
        return f"{self.nama}: Rp. {self.biaya:,.2f}"

class BiayaGabungan(KomponenBiaya):
    def __init__(self, nama):
        self.nama = nama
        self.komponen = []

    def tambah(self, komponen):
        self.komponen.append(komponen)

    def ambilBiaya(self):
        return sum(komp.ambilBiaya() for komp in self.komponen)

    def __str__(self):
        detail = "\n".join(str(komp) for komp in self.komponen)
        return f"{self.nama}:\n{detail}\nTotal: Rp. {self.ambilBiaya():,.2f}"

def main():
    biayaPendaftaran = BiayaSederhana("Biaya Pendaftaran", 200_000)
    biayaKuliahPertama = BiayaSederhana("Biaya Kuliah Pertama", 1_500_000)

    biayaMpt = BiayaGabungan("Biaya MPT")
    biayaMpt.tambah(BiayaSederhana("Biaya Training", 100_000))
    biayaMpt.tambah(BiayaSederhana("Biaya Penginapan", 200_000))
    biayaMpt.tambah(BiayaSederhana("Biaya Konsumsi", 150_000))

    totalBiaya = BiayaGabungan("Total Biaya Pendaftaran")
    totalBiaya.tambah(biayaPendaftaran)
    totalBiaya.tambah(biayaKuliahPertama)
    totalBiaya.tambah(biayaMpt)

    print(totalBiaya)

if __name__ == "__main__":
    main()
