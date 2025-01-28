class CapitalIterable:
    def __init__(self, string):
        self.string = string
    def __iter__(self):
        return CapitalIterator(self.string)
    
class CapitalIterator:
    def __init__(self, string):
        #self.words = [kata.capitalize() for kata in string.split()]
        self.words =  [ ]
        pecahan = string.split() #split()digunakan untuk memecah nilai string berdasarkan karakter tertentu, cth lain split("A") dipecah ketika bertemu "A"
        for kata in pecahan:
            self.words.append(kata.upper()) #upper() untuk membuat kata menjadi bentuk kapital/huruf besar, lower() kebalikannya
        self.index = 0
    def __next__(self): #ini adalah overiding fungsi asli next iter
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word
    def __iter__(self): #ini akan mengoveride fungsi asli iter, digunaan ketika ingin membuat iterasi custom
        return self
    

#main
kalimat = "Saya kuliah di universitas mikroskil"
iterable = CapitalIterable(kalimat)

print("\nVersi While:\n")
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

print("\nVersi For : \n")
for kata in iterable:
    print(kata)
