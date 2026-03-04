# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Latihan  5 Melengkapi Fungsi Merge
# ===============================================================

# Kode Awal
# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if ___________________ :
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
    
#     return result

# Soal:
# 1. Lengkapi kondisi agar menjadi ascending.
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
# 2. Jelaskan fungsi result.extend().
# Menambahkan sisa elemen yang belum dimasukkan ke dalam result.