# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    if len(hasil) == n:              # Base case: jika panjang hasil sudah sama dengan n
        print(hasil)                 # Cetak kombinasi yang sudah terbentuk
        return                       # Hentikan rekursi untuk cabang ini
    
    kombinasi(n, hasil + "A")        # Rekursi dengan menambahkan huruf "A"
    kombinasi(n, hasil + "B")        # Rekursi dengan menambahkan huruf "B"

kombinasi(2)                         # Memanggil fungsi untuk panjang kombinasi 2