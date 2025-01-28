from kalkulator import kalku

def test_tambah():
    assert kalku.tambah(10, -30) == -20

def test_kurang_benar():
    assert kalku.kurang(10, -30) == 40

def test_kurang_salah():
    assert kalku.kurang(10, -30) != -40

def test_kali():
    assert kalku.kali(10, -30) == -300

def test_bagi():
    assert kalku.bagi(10, -20) == -0.5

def test_bagi_dengan_nol():
    import pytest
    with pytest.raises(ValueError):
        kalku.bagi(10, 0)
