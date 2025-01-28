class Kelas:
    def __init__(self, namaKelas, jenisRuangan, mataKuliah, proses):
        self.namaKelas = namaKelas
        self.jenisRuangan = jenisRuangan
        self.mataKuliah = mataKuliah
        self.proses = proses

    def rekapProses(self):
        return f"Kelas {self.namaKelas} di ruangan {self.jenisRuangan} mempelajari {self.mataKuliah} dengan proses: {self.proses}."


class KelasFacade:
    def __init__(self):
        self.kelasA = Kelas(
            namaKelas="A",
            jenisRuangan="T1/L2",
            mataKuliah="Kalkulus",
            proses="mengajarkan perhitungan kalkulus beserta prosesnya"
        )
        self.kelasB = Kelas(
            namaKelas="B",
            jenisRuangan="T3/L2",
            mataKuliah="Pemrograman",
            proses="mengajarkan pemrograman beserta proses-prosesnya"
        )
        self.kelasC = Kelas(
            namaKelas="C",
            jenisRuangan="T5/L2",
            mataKuliah="Bahasa Inggris",
            proses="mengajarkan formula-formula pembuatan kata-kata"
        )

    def rekapSemuaKelas(self):
        return "\n".join([
            self.kelasA.rekapProses(),
            self.kelasB.rekapProses(),
            self.kelasC.rekapProses()
        ])


if __name__ == "__main__":
    resepsionis = KelasFacade()
    print("\n")
    print("Rekap Absensi:")
    print(resepsionis.rekapSemuaKelas())
    print("\n")
