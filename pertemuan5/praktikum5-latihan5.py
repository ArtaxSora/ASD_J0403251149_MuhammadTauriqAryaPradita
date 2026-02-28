# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:           # Base case: jika panjang PIN sudah sesuai
        print("PIN:", hasil)            # Cetak PIN yang sudah terbentuk
        return                          # Hentikan rekursi untuk cabang ini
    
    for angka in ["0", "1", "2"]:       # Perulangan untuk setiap kemungkinan angka
        buat_pin(panjang, hasil + angka) # Rekursi dengan menambahkan angka ke hasil

buat_pin(3)                             # Memanggil fungsi untuk membuat PIN 3 digit