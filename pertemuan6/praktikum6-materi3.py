# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Merge Sort (Ascending)
# ===============================================================

def merge_sort(data):

    # Base case (kondisi berhenti)
    if len(data) <= 1:
        return data

    # Divide : Membagi data menjadi dua bagian
    mid = len(data) // 2  
    left = data[:mid]   # Slicing bagian kiri
    right = data[mid:]  # Slicing bagian kanan

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0

    # Merge : Menggabungkan dua bagian yang sudah terurut
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Menambahkan sisa elemen dari left atau right jika ada
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    

angka = [13, 7, 28, 5, 19, 36, 4]
print("Hasil Sorting:", merge_sort(angka))