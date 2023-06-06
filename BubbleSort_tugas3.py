def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Jika dalam satu iterasi tidak ada pertukaran elemen, berarti array sudah terurut
        if not swapped:
            break


# Contoh penggunaan dengan dataset buah
buah = ['apel', 'duku', 'gersen', 'jeruk', 'kelengkeng']
print("Buah sebelum diurutkan:")
print(buah)

bubble_sort(buah)

print("Buah terurut:")
print(buah)