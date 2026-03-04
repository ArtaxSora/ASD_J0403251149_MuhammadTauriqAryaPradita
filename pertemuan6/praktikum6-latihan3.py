# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Latihan 3 . Tracing Insertion Sort
# ===============================================================

# Buat program dengan menggunakan algoritma insertion sort
# Tracing dengan data = [5, 2, 4, 6, 1, 3]

def insertion_sort(data):
    #melihat data awal
    print(f"Data Awal : {data}")
    print("="*50)

    #loop mulai dari data ke-2
    for i in range(1, len(data)):

        key = data[i]   #simpan nilai yang disisipkan
        j = i - 1       #index elemen terakhir dibagian kiri
        
        print(f"Iterasi ke-{i}:")
        print(f"Key yang disisipkan: {key}")
        print(f"Elemen kiri (Terurut): {data[:i]}")
        print(f"Elemen kanan (Belum Terurut): {data[i:]}")

        #Geser
        while j >= 0 and key < data[j]: #loop untuk membandingkan key dengan elemen sebelumnya
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j + 1] = key
        print(f"Setelah disisipkan: {data}")
        print("-"*50)

    return data

angka = [5, 2, 4, 6, 1, 3]
print("Data sebelum diurutkan:", angka)
sorted_angka = insertion_sort(angka)
print("Data setelah diurutkan:", sorted_angka)

# Soal:
# 1. Tuliskan isi list setelah iterasi i = 1.
# [2, 5, 4, 6, 1, 3]
# 2. Tuliskan isi list setelah iterasi i = 3.
# [2, 4, 5, 6, 1, 3]
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?
# 4 Kali pergeseran