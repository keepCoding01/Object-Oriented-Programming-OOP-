import unittest

class Phone:
    def __init__(self, id, name, os, version):
        self.id = id
        self.name = name
        self.os = os
        self.version = float(version)
    
    def upgrade(self):
        self.version += 0.1
    
    def boot(self):
        return f"Power On {self.name}\n{self.os}\nVer.{self.version}"


class Test(unittest.TestCase):
    def setUp(self):
        self.phone = Phone(1, "Test", "TestOS", 1.0)
    
    def test_upgrade(self):
        """Upgrade berjalan sesuai"""
        versi = self.phone.version
        self.phone.upgrade()
        self.assertEqual(self.phone.version, versi + 0.1)

    def test_boot(self):
        """Boot mengembalikan nilai yang sesuai"""
        boot = "Power On Test\nTestOS\nVer.1.0"
        self.assertEqual(self.phone.boot(), boot)

    def test_version_attribute(self):
        """Objek yang di create dari kelas Phone memiliki atribut 'version'"""
        self.assertTrue(hasattr(self.phone, 'version'))


unittest.main()
