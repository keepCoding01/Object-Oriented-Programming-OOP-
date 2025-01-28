import pytest

class BUKU:
    def __init__(self, nama, tahun, jlh):
        self.nama = nama
        self.tahun = tahun
        self.jlh = jlh

class fiturBaru:
    data = []

    def tambahBuku(self, buku):
        self.data.append(buku)

    def pencarianBuku(self, cari):
        for buku in self.data:
            if buku.nama == cari:
                return [buku.nama, buku.tahun]
        return [0, 0]

@pytest.fixture
def data():
    buku1 = BUKU("Pemrograman C", 2021, 3)
    buku2 = BUKU("Pemrograman C#", 2022, 10)
    fb = fiturBaru()
    fb.tambahBuku(buku1)
    fb.tambahBuku(buku2)
    return fb

def test_pencarianBenar(data):
    assert data.pencarianBuku("Pemrograman C") == ["Pemrograman C", 2021]

def test_pencarianSalah(data):
    assert data.pencarianBuku("Tidak Ada Buku") == [0, 0]
