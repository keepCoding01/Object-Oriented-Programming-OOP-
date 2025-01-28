# --- Kelas Dasar ---
class Peserta:
    def cetakInfo(self):
        raise NotImplementedError("Metode ini harus diimplementasikan oleh subclass.")

# --- Kelas Mahasiswa ---
class Mahasiswa(Peserta):
    def __init__(self, nim, nama, prodi, jenisKelamin, noHp):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp

    def cetakInfo(self):
        return f"[Mahasiswa] NIM: {self.nim}, Nama: {self.nama}, Prodi: {self.prodi}, Jenis Kelamin: {self.jenisKelamin}, No HP: {self.noHp}"

# --- Kelas Dosen ---
class Dosen(Peserta):
    def __init__(self, nip, nama, jabatan, jenisKelamin, noHp):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp

    def cetakInfo(self):
        return f"[Dosen] NIP: {self.nip}, Nama: {self.nama}, Jabatan: {self.jabatan}, Jenis Kelamin: {self.jenisKelamin}, No HP: {self.noHp}"

# --- Kelas Absensi ---
class Absensi:
    def __init__(self):
        self.absensi = []

    def tambahPeserta(self, peserta):
        if not isinstance(peserta, Peserta):
            raise TypeError("Peserta harus merupakan instance dari kelas Peserta.")
        self.absensi.append(peserta)

    def cetakAbsensi(self):
        print("Daftar Absensi Acara:")
        for idx, peserta in enumerate(self.absensi, 1):
            print(f"{idx}. {peserta.cetakInfo()}")

    def hitungPeserta(self):
        return len(self.absensi)

# --- Data Input ---
mahasiswa1 = Mahasiswa("123456789", "Rina Andriana", "Sistem Informasi", "Perempuan", "081234567890")
mahasiswa2 = Mahasiswa("987654321", "Budi Santoso", "Teknik Informatika", "Laki-laki", "089876543210")
dosen1 = Dosen("1987654321", "Dr. Wahyu Saputra", "Dekan", "Laki-laki", "085678912345")

# --- Penggunaan ---
absensi = Absensi()
absensi.tambahPeserta(mahasiswa1)
absensi.tambahPeserta(mahasiswa2)
absensi.tambahPeserta(dosen1)

# Cetak Absensi
absensi.cetakAbsensi()

# Hitung Peserta
jumlahPeserta = absensi.hitungPeserta()
print(f"\nTotal Pengunjung pada Acara: {jumlahPeserta}")

# --- Unit Test ---
import unittest

class TestAbsensi(unittest.TestCase):
    def setUp(self):
        self.absensi = Absensi()
        self.mahasiswa1 = Mahasiswa("123456789", "Rina Andriana", "Sistem Informasi", "Perempuan", "081234567890")
        self.mahasiswa2 = Mahasiswa("987654321", "Budi Santoso", "Teknik Informatika", "Laki-laki", "089876543210")
        self.dosen1 = Dosen("1987654321", "Dr. Wahyu Saputra", "Dekan", "Laki-laki", "085678912345")

    def test_tambahPeserta(self):
        self.absensi.tambahPeserta(self.mahasiswa1)
        self.absensi.tambahPeserta(self.dosen1)
        self.assertEqual(len(self.absensi.absensi), 2)

    def test_hitungPeserta(self):
        self.absensi.tambahPeserta(self.mahasiswa1)
        self.absensi.tambahPeserta(self.mahasiswa2)
        self.absensi.tambahPeserta(self.dosen1)
        self.assertEqual(self.absensi.hitungPeserta(), 3)

if __name__ == "__main__":
    unittest.main()




# # pertanyaan 
# 1. Single Responsibility Principle (SRP)
# Prinsip: Setiap kelas harus memiliki satu tanggung jawab tunggal dan tidak menangani terlalu banyak tugas.

# Pelanggaran dalam Kode:
# Kelas Absensi:
# Selain menyimpan daftar peserta dan menghitung jumlah peserta, kelas ini juga bertanggung jawab untuk mencetak daftar absensi. Seharusnya, tugas mencetak bisa dipisahkan ke kelas atau fungsi lain untuk menjaga SRP.
# Solusi:
# Pisahkan tugas pencetakan ke kelas/fungsi khusus seperti AbsensiPrinter.
# 2. Open/Closed Principle (OCP)
# Prinsip: Kode harus terbuka untuk ekstensi, tetapi tertutup untuk modifikasi.

# Pelanggaran dalam Kode:
# Kelas Peserta:
# Jika nanti ingin menambahkan jenis peserta baru (misalnya, Alumni atau Tamu), kita harus memodifikasi kode di beberapa bagian. Hal ini melanggar OCP.
# Solusi:
# Pastikan abstraksi yang ada mendukung penambahan jenis peserta baru tanpa memodifikasi kode yang sudah ada. Misalnya, gunakan polimorfisme untuk menangani pencetakan info peserta.
# 3. Liskov Substitution Principle (LSP)
# Prinsip: Subkelas harus dapat menggantikan superclassnya tanpa mengubah perilaku program.

# Sudah Dipenuhi:
# Kelas Mahasiswa dan Dosen adalah subkelas dari Peserta, dan keduanya dapat digunakan dengan cara yang sama seperti Peserta tanpa memengaruhi logika kelas Absensi.
# 4. Interface Segregation Principle (ISP)
# Prinsip: Kelas tidak boleh dipaksa untuk mengimplementasikan metode yang tidak relevan.

# Tidak Relevan untuk Kode Ini:
# Tidak ada masalah ISP karena setiap kelas hanya menggunakan metode yang relevan.
# 5. Dependency Inversion Principle (DIP)
# Prinsip: Modul tingkat tinggi tidak boleh bergantung langsung pada modul tingkat rendah; keduanya harus bergantung pada abstraksi.

# Pelanggaran dalam Kode:
# Kelas Absensi:
# Bergantung langsung pada implementasi kelas Mahasiswa dan Dosen karena memerlukan logika pencetakan spesifik. Jika format pencetakan diubah, ini dapat memengaruhi logika di Absensi.
# Solusi:
# Gunakan abstraksi (interface) untuk logika pencetakan peserta. Dengan cara ini, kelas Absensi tidak bergantung langsung pada kelas Mahasiswa atau Dosen.



# Perbaikan :

# # --- Kelas Dasar ---
# from abc import ABC, abstractmethod

# class Peserta(ABC):
#     @abstractmethod
#     def cetakInfo(self):
#         pass

# # --- Kelas Mahasiswa ---
# class Mahasiswa(Peserta):
#     def __init__(self, nim, nama, prodi, jenisKelamin, noHp):
#         self.nim = nim
#         self.nama = nama
#         self.prodi = prodi
#         self.jenisKelamin = jenisKelamin
#         self.noHp = noHp

#     def cetakInfo(self):
#         return f"[Mahasiswa] NIM: {self.nim}, Nama: {self.nama}, Prodi: {self.prodi}, Jenis Kelamin: {self.jenisKelamin}, No HP: {self.noHp}"

# # --- Kelas Dosen ---
# class Dosen(Peserta):
#     def __init__(self, nip, nama, jabatan, jenisKelamin, noHp):
#         self.nip = nip
#         self.nama = nama
#         self.jabatan = jabatan
#         self.jenisKelamin = jenisKelamin
#         self.noHp = noHp

#     def cetakInfo(self):
#         return f"[Dosen] NIP: {self.nip}, Nama: {self.nama}, Jabatan: {self.jabatan}, Jenis Kelamin: {self.jenisKelamin}, No HP: {self.noHp}"

# # --- Kelas Absensi ---
# class Absensi:
#     def __init__(self):
#         self.absensi = []

#     def tambahPeserta(self, peserta):
#         if not isinstance(peserta, Peserta):
#             raise TypeError("Peserta harus merupakan instance dari kelas Peserta.")
#         self.absensi.append(peserta)

#     def hitungPeserta(self):
#         return len(self.absensi)

# # --- Kelas Pencetak Absensi ---
# class AbsensiPrinter:
#     @staticmethod
#     def cetak(absensi):
#         print("Daftar Absensi Acara:")
#         for idx, peserta in enumerate(absensi, 1):
#             print(f"{idx}. {peserta.cetakInfo()}")

# # --- Penggunaan ---
# mahasiswa1 = Mahasiswa("123456789", "Rina Andriana", "Sistem Informasi", "Perempuan", "081234567890")
# mahasiswa2 = Mahasiswa("987654321", "Budi Santoso", "Teknik Informatika", "Laki-laki", "089876543210")
# dosen1 = Dosen("1987654321", "Dr. Wahyu Saputra", "Dekan", "Laki-laki", "085678912345")

# absensi = Absensi()
# absensi.tambahPeserta(mahasiswa1)
# absensi.tambahPeserta(mahasiswa2)
# absensi.tambahPeserta(dosen1)

# # Cetak Absensi
# AbsensiPrinter.cetak(absensi.absensi)

# # Hitung Peserta
# jumlahPeserta = absensi.hitungPeserta()
# print(f"\nTotal Pengunjung pada Acara: {jumlahPeserta}")



# Penerapan SOLID dalam Kode yang Diperbaiki
# SRP: Tugas pencetakan dipisahkan ke kelas AbsensiPrinter.
# OCP: Menambahkan jenis peserta baru tidak memengaruhi logika di Absensi.
# LSP: Subkelas (Mahasiswa dan Dosen) dapat menggantikan Peserta tanpa masalah.
# ISP: Tidak relevan karena antarmuka abstrak sudah cukup sederhana.
# DIP: Kelas Absensi bergantung pada abstraksi Peserta, bukan pada implementasi spesifik.