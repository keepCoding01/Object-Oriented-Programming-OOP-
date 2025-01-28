import unittest
from kalkulator import kalku

class TestKalku(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(kalku.tambah(10, -30), -20)

    def test_kurang_benar(self):
        self.assertEqual(kalku.kurang(10, -30), 40)

    def test_kurang_salah(self):
        self.assertNotEqual(kalku.kurang(10, -30), -40)

    def test_kali(self):
        self.assertEqual(kalku.kali(10, -30), -300)

    def test_bagi(self):
        self.assertEqual(kalku.bagi(10, -20), -0.5)

    def test_bagi_dengan_nol(self):
        with self.assertRaises(ValueError):
            kalku.bagi(10, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
