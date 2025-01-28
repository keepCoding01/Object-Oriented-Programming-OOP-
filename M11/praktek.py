class Jam:
    def __init__(self, jam, menit):
        self.jam = jam
        self.menit = menit

    def selisih(self, cekOutj, cekOutm):
        jamMasuk = self.jam * 60 + self.menit
        jamKeluar = cekOutj * 60 + cekOutm
        if jamKeluar < jamMasuk: 
            jamKeluar += 24 * 60
        return jamKeluar - jamMasuk


class AdapterKendaraan:
    def __init__(self, id, nama):
        self.id = id
        self.nama = nama


class Mobil(AdapterKendaraan):
    def __init__(self):
        print("Tambah Mobil:")
        id = input("ID Mobil: ")
        nama = input("Nama Mobil: ")
        super().__init__(id, nama)
        self.transmisi = input("Transmisi (AT/MT): ")
        self.jumlahRoda = int(input("Jumlah Roda: "))


class Excavator(AdapterKendaraan):
    def __init__(self):
        print("Tambah Excavator:")
        id = input("ID Excavator: ")
        nama = input("Nama Excavator: ")
        super().__init__(id, nama)
        self.attachment = input("Jenis Attachment (Bucket/Grapple/Breaker): ")
        self.jenisRoda = input("Jenis Roda (Crawler/Wheeled): ")


class Petugas:
    def __init__(self):
        self.id = input("ID Petugas: ")
        self.nama = input("Nama Petugas: ")


class Parkir:
    def __init__(self, idKendaraan, jam, tarif):
        self.idKendaraan = idKendaraan
        self.jam = jam
        self.tarif = tarif

    def hitungBiaya(self, waktuKeluar):
        waktuParkir = self.jam.selisih(waktuKeluar.jam, waktuKeluar.menit)
        return self.tarif(waktuParkir)


def hitung(menit):
    tarifPertama = 5000
    tarifBerikutnya = 2000
    jam = menit // 60
    sisaMenit = menit % 60
    biaya = tarifPertama + max(0, jam - 1) * tarifBerikutnya
    if sisaMenit > 0:
        biaya += tarifBerikutnya
    return biaya


class Garasi:
    def __init__(self):
        self.petugas = []
        self.listKendaraan = []
        self.listParkir = {}

    def tambahPetugas(self):
        petugas = Petugas()
        self.petugas.append(petugas)
        print("Petugas berhasil ditambahkan.")

    def tambahKendaraan(self):
        print("1. Mobil\n2. Excavator")
        pilihan = input("Pilih jenis kendaraan: ")
        if pilihan == "1":
            kendaraan = Mobil()
        elif pilihan == "2":
            kendaraan = Excavator()
        else:
            print("Pilihan tidak valid!")
            return
        self.listKendaraan.append(kendaraan)
        print("Kendaraan berhasil ditambahkan.")

    def cekInParkir(self):
        if not self.petugas:
            print("Belum ada petugas yang ditambahkan! Tambahkan petugas terlebih dahulu.")
            return
        if not self.listKendaraan:
            print("Belum ada kendaraan yang ditambahkan! Tambahkan kendaraan terlebih dahulu.")
            return

        idKendaraan = input("ID Kendaraan: ")
        if idKendaraan in self.listParkir:
            print(f"Kendaraan {idKendaraan} sudah parkir.")
            return
        kendaraan = next((k for k in self.listKendaraan if k.id == idKendaraan), None)
        if kendaraan:
            waktu = input("Waktu Cek In (hh:mm): ")
            try:
                jam, menit = map(int, waktu.split(":"))
                self.listParkir[idKendaraan] = Parkir(idKendaraan, Jam(jam, menit), hitung)
                print("Parkir berhasil ditambahkan.")
            except ValueError:
                print("Format waktu tidak valid!")
        else:
            print("Kendaraan tidak ditemukan!")

    def cekOutParkir(self):
        idKendaraan = input("ID Kendaraan: ")
        if idKendaraan not in self.listParkir:
            print(f"Kendaraan {idKendaraan} belum cek in.")
            return
        waktu = input("Waktu Keluar (hh:mm): ")
        try:
            jam, menit = map(int, waktu.split(":"))
            parkir = self.listParkir.pop(idKendaraan)
            biaya = parkir.hitungBiaya(Jam(jam, menit))
            print(f"Kendaraan {idKendaraan} berhasil Cek Out dengan biaya: {biaya}")
        except ValueError:
            print("Format waktu tidak valid!")

    def mulai(self):
        print("\n== Menu Mulai ==")
        if self.petugas:
            print("\nPetugas terdaftar:")
            for petugas in self.petugas:
                print(f"ID: {petugas.id}, Nama: {petugas.nama}")
        else:
            print("Belum ada petugas. Tambahkan petugas terlebih dahulu.")
            self.tambahPetugas()

        if self.listKendaraan:
            print("\nKendaraan terdaftar:")
            for kendaraan in self.listKendaraan:
                print(f"ID: {kendaraan.id}, Nama: {kendaraan.nama}")
        else:
            print("Belum ada kendaraan. Tambahkan kendaraan terlebih dahulu.")
            self.tambahKendaraan()

        if not self.listParkir:
            print("\nTidak ada kendaraan yang sedang parkir.")
            self.cekInParkir()
        else:
            print("\nDaftar kendaraan yang sedang parkir:")
            for idKendaraan, parkir in self.listParkir.items():
                print(f"ID: {idKendaraan}, Waktu Cek In: {parkir.jam.jam}:{parkir.jam.menit}")

    def daftarKendaraan(self):
        if not self.listKendaraan:
            print("Tidak ada kendaraan terdaftar.")
        else:
            for k in self.listKendaraan:
                print(f"ID: {k.id}, Nama: {k.nama}")

    def daftarPetugas(self):
        if not self.petugas:
            print("Tidak ada petugas terdaftar.")
        else:
            for p in self.petugas:
                print(f"ID: {p.id}, Nama: {p.nama}")

    def daftarParkir(self):
        if not self.listParkir:
            print("Tidak ada kendaraan yang sedang parkir.")
        else:
            for idKendaraan, parkir in self.listParkir.items():
                print(f"ID: {idKendaraan}, Waktu Cek In: {parkir.jam.jam}:{parkir.jam.menit}")


def main():
    garasi = Garasi()
    while True:
        print("\nMenu:")
        print("1. Mulai (Menampilkan/mengatur petugas, kendaraan, atau parkir)")
        print("2. Tambah Petugas")
        print("3. Tambah Kendaraan")
        print("4. Cek In Kendaraan")
        print("5. Cek Out Kendaraan")
        print("6. Daftar Kendaraan")
        print("7. Daftar Petugas")
        print("8. Daftar Parkir")
        print("0. Keluar")

        pilihan = input("Pilihan: ")
        if pilihan == "0":
            break
        elif pilihan == "1":
            garasi.mulai()
        elif pilihan == "2":
            garasi.tambahPetugas()
        elif pilihan == "3":
            garasi.tambahKendaraan()
        elif pilihan == "4":
            garasi.cekInParkir()
        elif pilihan == "5":
            garasi.cekOutParkir()
        elif pilihan == "6":
            garasi.daftarKendaraan()
        elif pilihan == "7":
            garasi.daftarPetugas()
        elif pilihan == "8":
            garasi.daftarParkir()
        else:
            print("Pilihan tidak valid!")


main()
