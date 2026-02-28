# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat(a, n):
    # Base case
    if n == 0:                 # Jika pangkat bernilai 0
        return 1               # Hasil selalu 1 (a^0 = 1)
    
    # Recursive case
    return a * pangkat(a, n - 1)    # Mengalikan a dengan hasil pangkat(a, n-1)
                                    # Fungsi memanggil dirinya sendiri hingga n = 0

print(pangkat(2, 4)) # Output: 16
