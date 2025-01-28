class TasyaSyafriza: 
    def __init__(self, nama, nim=None, nip=None, jabatan=None, jenisKelamin=None, noHp=None):
        self.nama = nama
        self.nim = nim  
        self.nip = nip  
        self.jabatan = jabatan 
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp

    def cetakData(self):
        data = f"Nama: {self.nama}\n"
        if self.nim:
            data += f"NIM: {self.nim}\n"
        if self.nip:
            data += f"NIP: {self.nip}\nJabatan: {self.jabatan}\n"
        data += f"Jenis Kelamin: {self.jenisKelamin}\n"
        data += f"No HP: {self.noHp}\n"
        return data


class Absensi:  
    def __init__(self):
        self.pengunjung = []

    def tambahPengunjung(self, orang):
        self.pengunjung.append(orang)

    def cetakAbsensi(self):
        hasil = "Daftar Absensi:\n"
        for idx, orang in enumerate(self.pengunjung, 1):
            hasil += f"{idx}. {orang.nama} ({'Mahasiswa' if orang.nim else 'Dosen'})\n"
        return hasil

    def hitungPengunjung(self):
        return len(self.pengunjung)



class AbsensiDecorator:
    def __init__(self, absensi):
        self._absensi = absensi

    def cetak_dan_hitung(self):
        print(self._absensi.cetakAbsensi())
        print(f"Total Pengunjung: {self._absensi.hitungPengunjung()}")


mahasiswa1 = TasyaSyafriza("Ahmad", nim="21101234", jenisKelamin="Laki-laki", noHp="081234567890")
mahasiswa2 = TasyaSyafriza("Siti", nim="21105678", jenisKelamin="Perempuan", noHp="081987654321")
dosen1 = TasyaSyafriza("Dr. Rudi", nip="1980456", jabatan="Ketua Prodi", jenisKelamin="Laki-laki", noHp="081345678912")
dosen2 = TasyaSyafriza("Prof. Ani", nip="1980789", jabatan="Dekan", jenisKelamin="Perempuan", noHp="081876543219")

absensi = Absensi()
absensi.tambahPengunjung(mahasiswa1)
absensi.tambahPengunjung(mahasiswa2)
absensi.tambahPengunjung(dosen1)
absensi.tambahPengunjung(dosen2)

dekorator_absensi = AbsensiDecorator(absensi)
dekorator_absensi.cetak_dan_hitung()
