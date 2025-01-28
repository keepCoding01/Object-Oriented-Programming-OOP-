class TasyaSyafriza:  
    def __init__(self, nama, jenisKelamin):
        self.nama = nama
        self.jenisKelamin = jenisKelamin


class Mahasiswa(TasyaSyafriza):  
    def __init__(self):
        self.nama = input("Masukkan nama mahasiswa: ")
        self.jenisKelamin = input("Masukkan jenis kelamin (L/P): ")
        self.nim = input("Masukkan NIM mahasiswa: ")
        self.programStudi = input("Masukkan program studi mahasiswa: ")
        super().__init__(self.nama, self.jenisKelamin)

    def __str__(self):
        return f"Mahasiswa: {self.nama}, NIM: {self.nim}, Prodi: {self.programStudi}, Jenis Kelamin: {self.jenisKelamin}"


class Dosen(TasyaSyafriza):  
    def __init__(self):
        self.nama = input("Masukkan nama dosen: ")
        self.jenisKelamin = input("Masukkan jenis kelamin (L/P): ")
        self.nip = input("Masukkan NIP dosen: ")
        self.jabatan = input("Masukkan jabatan dosen: ")
        self.noHp = input("Masukkan nomor HP dosen: ")
        super().__init__(self.nama, self.jenisKelamin)

    def __str__(self):
        return f"Dosen: {self.nama}, NIP: {self.nip}, Jabatan: {self.jabatan}, No HP: {self.noHp}, Jenis Kelamin: {self.jenisKelamin}"


class Absensi:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.daftarPengunjung = []  
        return cls._instance

    def tambahPengunjung(self, pengunjung):
        self.daftarPengunjung.append(pengunjung)

    def cetakDaftar(self):
        hasil = "=== Daftar Pengunjung ===\n"
        for idx, pengunjung in enumerate(self.daftarPengunjung, 1):
            hasil += f"{idx}. {pengunjung}\n"
        return hasil

    def hitungPengunjung(self):
        return len(self.daftarPengunjung)

    def cariPengunjung(self, nama):
        hasil = [str(p) for p in self.daftarPengunjung if p.nama.lower() == nama.lower()]
        return hasil if hasil else "Pengunjung tidak ditemukan."


class Main:
    def __init__(self):
        self.absensi = Absensi()

    def jalankan(self):
        print("=== Sistem Absensi ===")
        while True:
            print("\n1. Tambah Mahasiswa")
            print("2. Tambah Dosen")
            print("3. Cetak Daftar Pengunjung")
            print("4. Hitung Total Pengunjung")
            print("5. Cari Pengunjung")
            print("6. Keluar")
            pilihan = input("Pilih menu (1-6): ")

            if pilihan == "1":
                mahasiswa = Mahasiswa()  
                self.absensi.tambahPengunjung(mahasiswa)
                print(f"Mahasiswa {mahasiswa.nama} berhasil ditambahkan.")
            elif pilihan == "2":
                dosen = Dosen()
                self.absensi.tambahPengunjung(dosen)
                print(f"Dosen {dosen.nama} berhasil ditambahkan.")
            elif pilihan == "3":
                print(self.absensi.cetakDaftar())
            elif pilihan == "4":
                total = self.absensi.hitungPengunjung()
                print(f"Total pengunjung: {total}")
            elif pilihan == "5":
                nama = input("Masukkan nama pengunjung yang ingin dicari: ")
                hasil = self.absensi.cariPengunjung(nama)
                if isinstance(hasil, list):
                    print("\n".join(hasil))
                else:
                    print(hasil)
            elif pilihan == "6":
                print("Sistem absensi ditutup.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")


main = Main()
main.jalankan()
