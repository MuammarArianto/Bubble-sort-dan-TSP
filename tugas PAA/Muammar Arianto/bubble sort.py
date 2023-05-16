def bubble_sort(arr):
    n = len(arr)

    # Iterasi melalui semua elemen array
    for i in range(n):

        # Setiap iterasi akan memindahkan elemen terbesar ke posisi terakhir-i
        for j in range(0, n - i - 1):

            # Membandingkan dua elemen berdekatan
            if arr[j] > arr[j + 1]:
                # Jika elemen saat ini lebih besar dari elemen berikutnya, tukar posisi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Array setelah diurutkan:")
print(sorted_arr)
