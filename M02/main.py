from mainKedua import Masyarakat, Pemadam, Polisi
import os

status = True
tmp = 0
while(status):
    os.system("cls")
    print("Menu")
    print("1. Masyarakat")
    print("2. Pemadam")
    print("3. Polisi")
    print("0. Keluar")
    pilihan = input("Pilihan : ")
    if(pilihan =="1"):
        nama = input("Nama : ")
        tmp = Masyarakat(nama)
        tmp.perkenalan()
    elif(pilihan=="2"):
        nama = input("Nama : ")
        alat = input("Alat : ")
        tmp = Pemadam(nama, alat)
        tmp.perkenalan()
    elif(pilihan=="3"):
        nama = input("Nama : ")
        senjata = input("Senjata : ")
        tmp = Polisi(nama, senjata)
        tmp.perkenalan()
    elif(pilihan == "0"):
        status=False
    else:
        print("Pilihan tidak tersedia")
    input("Tekan enter untuk lanjut !")