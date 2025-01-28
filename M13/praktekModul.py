class Mahasiswa:
    def __init__(self, nim, nama, prodi, jenisKelamin, noHp):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp

class Dosen:
    def __init__(self, nip, nama, jabatan, jenisKelamin, noHp):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp

def tambahAbsensi(absensi, peserta):
    absensi.append(peserta)

def cetakAbsensi(absensi):
    print("Daftar Absensi Acara:")
    for idx, peserta in enumerate(absensi, 1):
        if isinstance(peserta, Mahasiswa):
            print(f"{idx}. [Mahasiswa] NIM: {peserta.nim}, Nama: {peserta.nama}, Prodi: {peserta.prodi}, Jenis Kelamin: {peserta.jenisKelamin}, No HP: {peserta.noHp}")
        elif isinstance(peserta, Dosen):
            print(f"{idx}. [Dosen] NIP: {peserta.nip}, Nama: {peserta.nama}, Jabatan: {peserta.jabatan}, Jenis Kelamin: {peserta.jenisKelamin}, No HP: {peserta.noHp}")

def hitungPeserta(absensi):
    return len(absensi)

# --- Data Input ---
mahasiswa1 = Mahasiswa("123456789", "Rina Andriana", "Sistem Informasi", "Perempuan", "081234567890")
mahasiswa2 = Mahasiswa("987654321", "Budi Santoso", "Teknik Informatika", "Laki-laki", "089876543210")
dosen1 = Dosen("1987654321", "Dr. Wahyu Saputra", "Dekan", "Laki-laki", "085678912345")

absensi = []

# Tambahkan ke absensi
tambahAbsensi(absensi, mahasiswa1)
tambahAbsensi(absensi, mahasiswa2)
tambahAbsensi(absensi, dosen1)

# Cetak absensi
cetakAbsensi(absensi)

# Hitung jumlah peserta
jumlahPeserta = hitungPeserta(absensi)
print(f"\nTotal Pengunjung pada Acara: {jumlahPeserta}")

# --- Unit Test ---
import unittest

class TestAbsensi(unittest.TestCase):
    def setUp(self):
        self.absensi = []
        self.mahasiswa1 = Mahasiswa("123456789", "Rina Andriana", "Sistem Informasi", "Perempuan", "081234567890")
        self.mahasiswa2 = Mahasiswa("987654321", "Budi Santoso", "Teknik Informatika", "Laki-laki", "089876543210")
        self.dosen1 = Dosen("1987654321", "Dr. Wahyu Saputra", "Dekan", "Laki-laki", "085678912345")

    def test_tambahAbsensi(self):
        tambahAbsensi(self.absensi, self.mahasiswa1)
        tambahAbsensi(self.absensi, self.dosen1)
        self.assertEqual(len(self.absensi), 2)
        self.assertIsInstance(self.absensi[0], Mahasiswa)
        self.assertIsInstance(self.absensi[1], Dosen)

    def test_hitungPeserta(self):
        tambahAbsensi(self.absensi, self.mahasiswa1)
        tambahAbsensi(self.absensi, self.mahasiswa2)
        tambahAbsensi(self.absensi, self.dosen1)
        self.assertEqual(hitungPeserta(self.absensi), 3)

if __name__ == "__main__":
    unittest.main()
