class TasyaSyafriza:
    def __init__(self, nomor_induk, nama, jenis_kelamin, no_hp):
        self.nomor_induk = nomor_induk
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.no_hp = no_hp

class Mahasiswa(TasyaSyafriza):
    def __init__(self, nomor_induk, nama, jenis_kelamin, no_hp, prodi, semester):
        super().__init__(nomor_induk, nama, jenis_kelamin, no_hp)
        self.prodi = prodi
        self.semester = semester
    def absensi(self):
        print(f"Absensi Mahasiswa: {self.nomor_induk} - {self.nama}")
 
class Dosen(TasyaSyafriza):
    def __init__(self, nomor_induk, nama, jenis_kelamin, no_hp, mata_kuliah):
        super().__init__(nomor_induk, nama, jenis_kelamin, no_hp)
        self.mata_kuliah = mata_kuliah
    def perkenalan(self):
        print(f"Perkenalan Dosen: Nama saya {self.nama}, No HP saya {self.no_hp}.")
 
 
mahasiswa1 = Mahasiswa("M12345", "Andi Wijaya", "Laki-laki", "081234567890", "Teknik Informatika", 5)
mahasiswa2 = Mahasiswa("M67890", "Siti Nurjanah", "Perempuan", "089876543210", "Sistem Informasi", 3)
 
dosen1 = Dosen("D98765", "Dr. Felix", "Laki-laki", "085712345678", "Statistika Komputasi")
dosen2 = Dosen("D54321", "Dr. Nurhayati", "Perempuan", "087654321098", "Pemrograman Python")
 
mahasiswa1.absensi()  # Output: Absensi Mahasiswa: M12345 - Andi Wijaya
mahasiswa2.absensi()  # Output: Absensi Mahasiswa: M67890 - Siti Nurjanah
 
dosen1.perkenalan()  # Output: Perkenalan Dosen: Nama saya Dr. Felix, No HP saya 085712345678.
dosen2.perkenalan()  # Output: Perkenalan Dosen: Nama saya Dr. Nurhayati, No HP saya 087654321098.