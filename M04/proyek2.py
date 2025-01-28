# kami membuat subclass dari Exception bawaan python agar bisa
# menampung berbagai jenis eror dan mengkustomnya secara manual.
class RumahEror(Exception):
    def __init__(self, pesanEror):
        super().__init__(pesanEror)
        self.pesanEror = pesanEror


# class Person sendiri adalah superclass untuk beberapa 
# atribut dan fungsi yang memiliki tujuan sama untuk 
# subclassnya nanti (dalam konteks ini subclass ada 2).
class Person:
    def __init__(self, nama, noHp):
        self.dataNama = nama
        self.dataNoHP = noHp

    def cekNama(self):
        if not all(karakter.isalpha() or karakter.isspace() for karakter in self.dataNama):
            raise RumahEror(f"Nama '{self.dataNama}' tidak valid. Pastikan dengan benar, nama hanya terdiri dari spasi dan huruf saja.")

    def cekNoHp(self):
        if len(self.dataNoHP) < 8 or len(self.dataNoHP) > 15:
            raise RumahEror(f"No HP '{self.dataNoHP}' tidak valid. Pastikan panjang harus 8 hingga 15 karakter.")
       
        if self.dataNoHP[0] != '+' and not self.dataNoHP[0].isdigit():
            raise RumahEror(f"No HP '{self.dataNoHP}' tidak valid. Pastikan harus diawali dengan '+' atau digit.")
       
        if not all(karakter.isdigit() for karakter in self.dataNoHP[1:] if karakter != '+'):
            raise RumahEror(f"No HP '{self.dataNoHP}' tidak valid. Hanya boleh berisi angka setelah tanda '+'.")

# subclass dari Person dan menambahkan satu fungsi untuk mengecek NIM.
class Mahasiswa(Person):
    def __init__(self, nim, nama, noHp):
        super().__init__(nama, noHp)
        self.nim = nim

    def cekNim(self):
        if len(self.nim) != 9 or not self.nim.isdigit():
            raise RumahEror(f"NIM '{self.nim}' tidak valid. Harus terdiri memiliki panjang 9 karakter.")

# subclass dari Person dan menambahkan satu fungsi untuk mengecek NIP.
class Dosen(Person):
    def __init__(self, nip, nama, noHp):
        super().__init__(nama, noHp)
        self.nip = nip

    def cekNip(self):
        if len(self.nip) != 9 or not self.nip.isdigit():
            raise RumahEror(f"NIP '{self.nip}' tidak valid. Harus terdiri memiliki panjang 9 karakter.")

# kami membuat try exceptnya ke masing-masing fungsi/method,
# agar kode program dalam dijalankan dan dicek hingga selesai/secara menyeluruh.
# karena jikat tidak, maka ketika program pertama kali menemukan eror 
# dengan "raise", data selanjutnya tidak akan dicek. 
def validasiData(person):
    # dikarenakan kami membuat try exceptnya ke masing-masing fungsi,
    # maka setiap baris program yang telah dilewati + mengalami eror,
    # akan kami simpan ke dalam sebuah wadah untuk menampung erornya 
    # dan menampilkan seluruh erornya di akhir program. 
    tampunganEror = []

    try:
        person.cekNama()
    except RumahEror as e:
        tampunganEror.append(e.pesanEror)

    try:
        person.cekNoHp()
    except RumahEror as e:
        tampunganEror.append(e.pesanEror)

    # kami menggunakan fungsi bawaan python yaitu isinstance
    if isinstance(person, Mahasiswa): # jika person = mahasiswa
        try:
            person.cekNim()
        except RumahEror as e:
            tampunganEror.append(e.pesanEror)
    elif isinstance(person, Dosen): # jika person = dosen
        try:
            person.cekNip()
        except RumahEror as e:
            tampunganEror.append(e.pesanEror)

    if tampunganEror:
        for error in tampunganEror:
            print(f"Error: {error}")
    else:
        print(f"Data {person.dataNama} valid, alias terverifikasi baik dan benar.")

# kami menggunakan inputan untuk mendapatkan data dari pengguna
def inputData():
    pilihanPengguna = input("Pilih (mahasiswa/dosen): ")

    if pilihanPengguna == "mahasiswa":
        namaMhs = input("Nama lengkap: ")
        noHPMhs = input("No HP: ")
        nim = input("NIM: ")
        mahasiswa = Mahasiswa(nim, namaMhs, noHPMhs)
        validasiData(mahasiswa)
    elif pilihanPengguna == "dosen":
        namaDosen = input("Nama lengkap: ")
        noHPDosen = input("No HP: ")
        nip = input("NIP: ")
        dosen = Dosen(nip, namaDosen, noHPDosen)
        validasiData(dosen)
    else:
        print("Pilihan tidak tersedia. Harap pilih mahasiswa/dosen.")
        inputData()


inputData()
