import unittest
from T13_00 import faktorial
from T13_00 import Barang
from T13_00 import Mahasiswa

class Pengujian(unittest.TestCase):
    def test_faktorial(self):
        self.assertEqual(faktorial(3), 6)
    def test_faktorial0(self):
        self.assertEqual(faktorial(0), 0)
    def test_kelasBarang(self):
        obj1 = Barang("01", "Garpu")
        self.assertIsInstance(obj1, Barang)
    def test_kelasBarang2(self):
        obj1 = Mahasiswa("Garpu")
        self.assertIsInstance(obj1, Barang)
    def test_tambahBarang(self):
        obj1 = Barang("01", "Garpu")
        jlhAwal = obj1.jumlah
        n=5
        obj1.tambah(n)
        self.assertEqual(obj1.jumlah, jlhAwal+n)
unittest.main()