# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Latihan  4 Memahami Kode Program (Merge Sort)
# ===============================================================

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    return

# Soal:
# 1. Apa yang dimaksud dengan base case?
# Base case adalah kondisi penghentian dalam rekursi.
# 2. Mengapa fungsi memanggil dirinya sendiri?\
# Karena algoritma Merge Sort menggunakan teknik rekursi dan konsep Divide.
# 3. Apa tujuan fungsi merge()?
# Untuk mengabungkan 2 list yang sudah terurut agar menjadi 1 list yang urut
