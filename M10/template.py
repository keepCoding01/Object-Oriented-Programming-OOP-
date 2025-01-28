import time

class Pencarian:
    def __init__(self, arr, data):
        self.arr = arr[:]
        self.data = data

    def pengurutan(self):
        return self.arr

    def pencarian(self):
        for i in range(len(self.arr)):
            if self.arr[i] == self.data:
                return i
        return -1

    def cetakArr(self):
        return self.arr

    def main(self):
        self.pengurutan() 
        return self.pencarian() 


class FungsiSort(Pencarian):
    def pengurutan(self):
        self.arr.sort() 
        return self.arr


class BubbleSort(Pencarian):
    def pengurutan(self):
        arr = self.arr[:]
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        self.arr = arr
        return self.arr


class InsertionSort(Pencarian):
    def pengurutan(self):
        arr = self.arr[:]
        for i in range(1, len(arr)):
            key_item = arr[i]
            j = i - 1
            while j >= 0 and key_item < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item
        self.arr = arr
        return self.arr


if __name__ == '__main__':
    data = [10, 11, 6, 19, -3, 5, 9, 100, 50, 49, 101, 200, 67, 891, 892, 1000, 60, -37]
    cari = 11

    start_time = time.time()
    algo1 = FungsiSort(data, cari)
    print(f"Angka {cari} ada di urutan ke-{algo1.main()}")
    print(f"Hasil pengurutan = {algo1.cetakArr()}")
    print(f"Hasil Fungsi Sort = {time.time() - start_time} seconds\n")

    start_time = time.time()
    algo2 = InsertionSort(data, cari)
    print(f"Angka {cari} ada di urutan ke-{algo2.main()}")
    print(f"Hasil pengurutan = {algo2.cetakArr()}")
    print(f"Hasil Insertion Sort = {time.time() - start_time} seconds\n")

    start_time = time.time()
    algo3 = BubbleSort(data, cari)
    print(f"Angka {cari} ada di urutan ke-{algo3.main()}")
    print(f"Hasil pengurutan = {algo3.cetakArr()}")
    print(f"Hasil Bubble Sort = {time.time() - start_time} seconds\n")
