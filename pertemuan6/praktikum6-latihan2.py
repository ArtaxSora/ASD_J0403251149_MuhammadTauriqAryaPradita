# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Latihan 2 Melengkapi Potongan Kode
# ===============================================================

# Kode Awal
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 : # And______________________: 
            data[j + 1] = data[j]
            j -= 1

        # ______________________

    return data

# Soal:
# 1. Lengkapi kondisi agar menjadi sorting ascending.
def insertion_sort_asc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

# 2. Ubah agar menjadi descending.
def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data