# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Latihan 1 Memahami Kode Program (Insertion Sort)
# ===============================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

            data[j + 1] = key

    return data

# Soal:
# 1. Mengapa perulangan dimulai dari indeks 1?
# Karena pada algoritma Insertion Sort, elemen pertama (indeks 0) dianggap sudah dalam keadaan terurut.
# 2. Apa fungsi variabel key?
# Berfungsi untuk menyimpan nilai yang sedang diproses atau yang ingin disisipkan.
# 3. Mengapa digunakan while, bukan for?
# Karena jumlah pergeseran tidak tetap dan tergantung kondisi.
# 4. Operasi apa yang terjadi di dalam while?
# - Pergeseran Elemen = data[j + 1] = data[j]
# - Perpindahan indeks = j -= 1
# - Penyisipan key = data[j + 1] = key
