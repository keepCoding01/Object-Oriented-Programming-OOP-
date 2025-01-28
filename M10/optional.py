from abc import ABC, abstractmethod

class TemplateProsesPakaianWanita(ABC):
    def membuatPakaian(self):
        self.step1PilihBahan()
        self.step2PotongBahan()
        self.step3Jahit()
        self.step4TambahManikManik()
        self.pakaianSelesai()

    def step1PilihBahan(self):
        pass

    @abstractmethod
    def step2PotongBahan(self):
        pass

    def step3Jahit(self):
        print("Menjahit pakaian sesuai pola.")

    def step4TambahManikManik(self):
        print("Menambahkan detail akhir seperti kancing atau renda.")

    def pakaianSelesai(self):
        print("Pakaian selesai dibuat dan siap untuk dijual.")


class CasualDress(TemplateProsesPakaianWanita):
    def step1PilihBahan(self):
        print("Memilih bahan kain katun atau denim untuk pakaian kasual.")

    def step2PotongBahan(self):
        print("Memotong pola pakaian kasual sederhana.")


class FormalDress(TemplateProsesPakaianWanita):
    def step2PotongBahan(self):
        print("Memotong pola pakaian kasual sederhana.")
    def step4TambahManikManik(self):
        print("Menambahkan bordir dan manik-manik untuk pakaian formal.")


if __name__ == "__main__":
    print("Membuat pakaian kasual:")
    casual = CasualDress()
    casual.membuatPakaian()

    print("\nMembuat pakaian formal:")
    formal = FormalDress()
    formal.membuatPakaian()
