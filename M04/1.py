class Person:
    def __init__(self, kode, nama, noHP):
        self.kode = kode
        self.nama = nama
        self.noHP = noHP

    def cekKode(self):
        try:
            if not self.kode.isdigit():
                raise ValueError("Kode harus terdiri dari angka saja.")
            if len(self.kode) != 9:
                raise ValueError("Kode harus memiliki panjang 9 karakter.")
        except ValueError as ve:
            print(f"Kesalahan pada kode: {ve}")
    
    def cekNama(self):
        
        try:
            if not all(char.isalpha() or char.isspace() for char in self.nama):
                raise ValueError("Nama hanya boleh terdiri dari huruf dan spasi.")
        except ValueError as ve:
            print(f"Kesalahan pada nama: {ve}")
    
    def cekNoTelp(self):
        try:
            if not (self.noHP.startswith('+') or self.noHP.isdigit()):
                raise ValueError("No HP harus dimulai dengan '+' atau angka.")
            if not self.noHP.replace('+', '').isdigit():
                raise ValueError("No HP hanya boleh terdiri dari angka dan '+' saja.")
            if not (8 <= len(self.noHP.replace('+', '')) <= 15):
                raise ValueError("No HP harus memiliki panjang antara 8 hingga 15 karakter.")
        except ValueError as ve:
            print(f"Kesalahan pada nomor HP: {ve}")
    
    def validasi(self):
        self.cekKode()
        self.cekNama()
        self.cekNoTelp()


class Mahasiswa(Person):
    def __init__(self, nim, nama, noHP):
        super().__init__(nim, nama, noHP)


class Dosen(Person):
    def __init__(self, nip, nama, noHP):
        super().__init__(nip, nama, noHP)


def cekDataMhs(person):
    print(f"\nMengecek data {type(person).__name__}:")
    person.validasi()



dosen = Dosen("987654321", "Dr. Andreas", "+621234567890")
mahasiswa = Mahasiswa("123", "Tasya123", "08123")


cekDataMhs(dosen)
cekDataMhs(mahasiswa)
