class Mahasiswa:
    def __init__(self, nim, nama, noHp):
        self.nim = nim
        self.nama = nama
        self.noHp = noHp

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, NoHP: {self.noHp}"

class DaftarMahasiswa:
    def __init__(self, namaKelas):
        self.namaKelas = namaKelas
        self.daftarMahasiswa = []

    def tambahMahasiswa(self, mahasiswa):
        if len(self.daftarMahasiswa) < 5:  
            self.daftarMahasiswa.append(mahasiswa)
        else:
            print("Data mahasiswa sudah mencapai batas maksimal (5).")

    def cariMahasiswa(self, nim=None, nama=None, noHp=None):
        hasilPencarian = []
        for mahasiswa in self.daftarMahasiswa:
            if (nim and mahasiswa.nim == nim) or (nama and mahasiswa.nama == nama) or (noHp and mahasiswa.noHp == noHp):
                hasilPencarian.append(mahasiswa)
        return hasilPencarian

    def __iter__(self):
        return IteratorMahasiswa(self.daftarMahasiswa)

class IteratorMahasiswa:
    def __init__(self, daftarMahasiswa):
        self._daftarMahasiswa = daftarMahasiswa
        self._index = 0

    def __next__(self):
        if self._index < len(self._daftarMahasiswa):
            mahasiswa = self._daftarMahasiswa[self._index]
            self._index += 1
            return mahasiswa
        raise StopIteration

def main():
    kelasMikroskil = DaftarMahasiswa("Mikroskil 01")

    kelasMikroskil.tambahMahasiswa(Mahasiswa("123456789", "Budi", "08123456789"))
    kelasMikroskil.tambahMahasiswa(Mahasiswa("987654321", "Siti", "08123456788"))
    kelasMikroskil.tambahMahasiswa(Mahasiswa("456123789", "Andi", "08123456787"))
    kelasMikroskil.tambahMahasiswa(Mahasiswa("789456123", "Rina", "08123456786"))
    kelasMikroskil.tambahMahasiswa(Mahasiswa("321654987", "Tono", "08123456785"))

    hasilPencarian = kelasMikroskil.cariMahasiswa(nim="123456789")
    print("Hasil Pencarian Berdasarkan NIM:")
    for mahasiswa in hasilPencarian:
        print(mahasiswa)

    print("\nDaftar Mahasiswa di kelas Mikroskil:")
    for mahasiswa in kelasMikroskil:
        print(mahasiswa)


main()
