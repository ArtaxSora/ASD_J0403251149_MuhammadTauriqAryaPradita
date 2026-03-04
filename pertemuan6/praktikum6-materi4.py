# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Merge Sort dengan Tracing (Ascending)
# ===============================================================

def merge_sort(data,level=0):
    indent = "  " * level  # Untuk tampilan bertingkat
    print(f"{indent}Memanggil merge_sort({data})")

    # Base case (kondisi berhenti)
    if len(data) <= 1:
        return data

    # Divide : Membagi data menjadi dua bagian
    mid = len(data) // 2  
    left = data[:mid]   # Slicing bagian kiri
    right = data[mid:]  # Slicing bagian kanan

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    hasil = merge(left_sorted, right_sorted, level)
    print(f"{indent}Hasil merge {left_sorted} + {right_sorted} = {hasil}")
    
    return hasil


def merge(left, right, level):
    indent = "  " * level
    print(f"{indent}Menggabungkan {left} dan {right}")

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
print("\n=== PROSES MERGE SORT ===\n")
hasil = merge_sort(angka)
print("\nHasil Akhir:", hasil)