class TasyaSyafriza:
    def __init__(self):
        self.daftarMhs = [] 

    def pemasukanData(self):
        dataMhs = [
            {"nim": "123456789", "nama": "Budi", "noHp": "08123456789"},
            {"nim": "987654321", "nama": "Siti", "noHp": "08123456788"},
            {"nim": "456123789", "nama": "Andi", "noHp": "08123456787"},
            {"nim": "789456123", "nama": "Rina", "noHp": "08123456786"},
            {"nim": "321654987", "nama": "Tono", "noHp": "08123456785"}
        ]
        for data in dataMhs:
            self.daftarMhs.append(data)

    def absensi(self, cariNama):
        ditemukan = []
        tidakDitemukan = []

        for mahasiswa in self.daftarMhs:
            if mahasiswa["nama"] == cariNama:
                ditemukan.append(mahasiswa)
            else:
                tidakDitemukan.append(mahasiswa)
        
        return ditemukan, tidakDitemukan


def main():
    kelasTasya = TasyaSyafriza()
    kelasTasya.pemasukanData()

    cariNama = "Aca"
    ditemukan, tidakDitemukan = kelasTasya.absensi(cariNama)

    print(f"Hasil Pencarian untuk nama: {cariNama}")
    if ditemukan:
        print(f"1. Data yang ada di kelas Mikroskil:")
        for data in ditemukan:
            print(f"- NIM: {data['nim']}, Nama: {data['nama']}, No HP: {data['noHp']}")
    else:
        print("Tidak ditemukan data yang sesuai.")

    print("\n2. Data Mahasiswa lain yang ada di kelas Mikroskil:")
    for data in tidakDitemukan:  
        print(f"- NIM: {data['nim']}, Nama: {data['nama']}, No HP: {data['noHp']}")

main()
