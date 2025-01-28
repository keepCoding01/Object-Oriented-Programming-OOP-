from pathlib import Path

path = Path(__file__).parent.absolute()
try :
    f = open(f"{path}/db.txt","r")
    s = f.readlines()
    print("Isi Notepad sekarang : ", s)
except:
    pass

sNew = input("Masukkan nilai baru ke db.txt : ")
f = open(f"{path}/db.txt", "w")
f.write(sNew)
f.close()
print("Isi db.txt diperbaharui")

