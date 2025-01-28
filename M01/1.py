class Mahasiswa:
    def __init__(self, nim, nama, prodi, jenis_kelamin, no_hp):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.jenis_kelamin = jenis_kelamin
        self.no_hp = no_hp
 
class Dosen:
    def __init__(self, nip, nama, jabatan, jenis_kelamin, no_hp):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.jenis_kelamin = jenis_kelamin
        self.no_hp = no_hp
 
def tambah_absensi(absensi, peserta):
    absensi.append(peserta)
 
def cetak_absensi(absensi):
    print("Daftar Absensi Acara:")
    for idx, peserta in enumerate(absensi, 1):
        if isinstance(peserta, Mahasiswa):
            print(f"{idx}. [Mahasiswa] NIM: {peserta.nim}, Nama: {peserta.nama}, Prodi: {peserta.prodi}, Jenis Kelamin: {peserta.jenis_kelamin}, No HP: {peserta.no_hp}")
        elif isinstance(peserta, Dosen):
            print(f"{idx}. [Dosen] NIP: {peserta.nip}, Nama: {peserta.nama}, Jabatan: {peserta.jabatan}, Jenis Kelamin: {peserta.jenis_kelamin}, No HP: {peserta.no_hp}")
 
def hitung_peserta(absensi):
    return len(absensi)
 
mahasiswa1 = Mahasiswa("123456789", "Rina Andriana", "Sistem Informasi", "Perempuan", "081234567890")
mahasiswa2 = Mahasiswa("987654321", "Budi Santoso", "Teknik Informatika", "Laki-laki", "089876543210")
dosen1 = Dosen("1987654321", "Dr. Wahyu Saputra", "Dekan", "Laki-laki", "085678912345")
 
absensi = []
 
tambah_absensi(absensi, mahasiswa1)
tambah_absensi(absensi, mahasiswa2)
tambah_absensi(absensi, dosen1)
 
cetak_absensi(absensi)
 
jumlah_peserta = hitung_peserta(absensi)
print(f"\nTotal Pengunjung pada Acara: {jumlah_peserta}")