# Abstract Factory

from abc import ABC, abstractmethod

class Biaya(ABC):
    @abstractmethod
    def ambilBiaya(self):
        pass

class BiayaPendaftaran(Biaya):
    def ambilBiaya(self):
        return 200_000

class BiayaKuliahPertama(Biaya):
    def ambilBiaya(self):
        return 1_500_000

class BiayaMpt(ABC):
    @abstractmethod
    def ambilBiaya(self):
        pass

class BiayaTraining(BiayaMpt):
    def ambilBiaya(self):
        return 100_000

class BiayaPenginapan(BiayaMpt):
    def ambilBiaya(self):
        return 200_000

class BiayaKonsumsi(BiayaMpt):
    def ambilBiaya(self):
        return 150_000

class PabrikBiaya(ABC):
    @abstractmethod
    def buatBiayaPendaftaran(self):
        pass

    @abstractmethod
    def buatBiayaMpt(self):
        pass

class PabrikBiayaKonkret(PabrikBiaya):
    def buatBiayaPendaftaran(self):
        return BiayaPendaftaran()

    def buatBiayaMpt(self):
        return [BiayaTraining(), BiayaPenginapan(), BiayaKonsumsi()]

def main():
    pabrik = PabrikBiayaKonkret()

    biayaPendaftaran = pabrik.buatBiayaPendaftaran()
    biayaKuliah = BiayaKuliahPertama()

    biayaMpt = pabrik.buatBiayaMpt()

    totalBiayaMpt = sum(b.ambilBiaya() for b in biayaMpt)
    totalKeseluruhan = biayaPendaftaran.ambilBiaya() + biayaKuliah.ambilBiaya() + totalBiayaMpt

    print(f"Biaya Pendaftaran: Rp. {biayaPendaftaran.ambilBiaya():,.2f}")
    print(f"Biaya Kuliah Pertama: Rp. {biayaKuliah.ambilBiaya():,.2f}")
    print("Biaya MPT:")
    for biaya in biayaMpt:
        print(f"- Rp. {biaya.ambilBiaya():,.2f}")
    print(f"Total Biaya: Rp. {totalKeseluruhan:,.2f}")

if __name__ == "__main__":
    main()
