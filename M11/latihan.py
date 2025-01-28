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


# -------------------------------------------------
# Kelas asli dengan format yang berbeda
# class KelasA:
#     def __init__(self):
#         self.namaKelas = "A"
#         self.ruangan = "T1/L2"
#         self.pelajaran = "Kalkulus"
#         self.keterangan = "mengajarkan perhitungan kalkulus beserta prosesnya"

#     def detail(self):
#         return f"{self.namaKelas}: {self.keterangan}"

# class KelasB:
#     def __init__(self):
#         self.nama = "B"
#         self.jenis = "T3/L2"
#         self.subjek = "Pemrograman"
#         self.deskripsi = "mengajarkan pemrograman beserta proses-prosesnya"

#     def info(self):
#         return f"{self.nama}: {self.deskripsi}"

# class KelasC:
#     def __init__(self):
#         self.kelas = "C"
#         self.lokasi = "T5/L2"
#         self.matkul = "Bahasa Inggris"
#         self.proses = "mengajarkan formula-formula pembuatan kata-kata"

#     def data(self):
#         return f"{self.kelas}: {self.proses}"

# # Adapter untuk menyelaraskan antarmuka
# class AdapterKelas:
#     def __init__(self, kelas, method):
#         self.kelas = kelas
#         self.method = method

#     def rekapProses(self):
#         return self.method()

# # Penggunaan Adapter
# if __name__ == "__main__":
#     kelasA = KelasA()
#     kelasB = KelasB()
#     kelasC = KelasC()

#     adapterA = AdapterKelas(kelasA, kelasA.detail)
#     adapterB = AdapterKelas(kelasB, kelasB.info)
#     adapterC = AdapterKelas(kelasC, kelasC.data)

#     print("Rekap Absensi:")
#     print(adapterA.rekapProses())
#     print(adapterB.rekapProses())
#     print(adapterC.rekapProses())

# =====================================================
# Command interface
# class Command:
#     def execute(self):
#         raise NotImplementedError("Subclasses harus mengimplementasikan metode execute")

# # Kelas Aksi
# class Kelas:
#     def __init__(self, namaKelas, jenisRuangan, mataKuliah, proses):
#         self.namaKelas = namaKelas
#         self.jenisRuangan = jenisRuangan
#         self.mataKuliah = mataKuliah
#         self.proses = proses

#     def rekapProses(self):
#         return f"Kelas {self.namaKelas} di ruangan {self.jenisRuangan} mempelajari {self.mataKuliah} dengan proses: {self.proses}."

# # Command untuk rekap kelas
# class RekapKelasCommand(Command):
#     def __init__(self, kelas):
#         self.kelas = kelas

#     def execute(self):
#         return self.kelas.rekapProses()

# # Invoker untuk menjalankan semua perintah
# class Resepsionis:
#     def __init__(self):
#         self.commands = []

#     def tambahCommand(self, command):
#         self.commands.append(command)

#     def prosesSemua(self):
#         hasil = []
#         for command in self.commands:
#             hasil.append(command.execute())
#         return "\n".join(hasil)

# # Main Program
# if __name__ == "__main__":
#     # Membuat objek kelas
#     kelasA = Kelas(
#         namaKelas="A",
#         jenisRuangan="T1/L2",
#         mataKuliah="Kalkulus",
#         proses="mengajarkan perhitungan kalkulus beserta prosesnya"
#     )
#     kelasB = Kelas(
#         namaKelas="B",
#         jenisRuangan="T3/L2",
#         mataKuliah="Pemrograman",
#         proses="mengajarkan pemrograman beserta proses-prosesnya"
#     )
#     kelasC = Kelas(
#         namaKelas="C",
#         jenisRuangan="T5/L2",
#         mataKuliah="Bahasa Inggris",
#         proses="mengajarkan formula-formula pembuatan kata-kata"
#     )

#     # Membuat objek command
#     commandA = RekapKelasCommand(kelasA)
#     commandB = RekapKelasCommand(kelasB)
#     commandC = RekapKelasCommand(kelasC)

#     # Invoker
#     resepsionis = Resepsionis()
#     resepsionis.tambahCommand(commandA)
#     resepsionis.tambahCommand(commandB)
#     resepsionis.tambahCommand(commandC)

#     # Eksekusi
#     print("Rekap Absensi:")
#     print(resepsionis.prosesSemua())
