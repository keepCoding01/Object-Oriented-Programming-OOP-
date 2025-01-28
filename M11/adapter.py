# menghubungkan dua kelas yang berbeda antarmukanya, sehingga mereka dapat bekerja sama tanpa harus mengubah kode asli.
# Contoh Sederhana: Bayangkan Anda memiliki charger ponsel lama (port micro-USB), tetapi sekarang Anda menggunakan ponsel dengan port USB-C. Anda membutuhkan adapter untuk menyambungkan charger lama ke ponsel baru.

class MyDatabase:
    def __init__(self, host, database, username, password):
        self.host = host
        self.database = database
        self.username = username
        self.password = password

    def koneksi(self):
        print("Berhasil terhubung ke server")
        print(f"Host : {self.host}")
        print(f"Database : {self.database}")
        print(f"Username : {self.username}")
        print(f"Password : {'*' * len(self.password)}")

    def executeQuery(self, perintah):
        print(f"Perintah yang dimasukkan adalah : {perintah}")

class AdapterDatabase:
    def __init__(self, stringKoneksi):
        tmp = stringKoneksi.split(" ")
        self.db = MyDatabase(tmp[0], tmp[1], tmp[2], tmp[3])
        self.db.koneksi()

    def selectTable(self, namaTable):
        perintah = f"Select * from {namaTable}"
        self.db.executeQuery(perintah)

if __name__ == "__main__":
    Host = "127.0.0.1"
    Database = "pelaporanUang"
    Username = "root"
    Password = "******"
    koneksi = f"{Host} {Database} {Username} {Password}"
    Tabel = "Pengeluaran"
    adapter = AdapterDatabase(koneksi)
    adapter.selectTable(Tabel)
