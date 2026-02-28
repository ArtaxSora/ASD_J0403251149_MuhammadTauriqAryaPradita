# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:          # Jika sudah di elemen terakhir
        return data[index]              # Kembalikan nilai terakhir
    
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)   # Cari nilai maksimum dari sisa list
    
    if data[index] > maks_sisa:         # Bandingkan elemen sekarang dengan maksimum sisa
        return data[index]              # Jika lebih besar, kembalikan elemen sekarang
    else:
        return maks_sisa                # Jika tidak, kembalikan maksimum dari sisa


angka = [3, 7, 2, 9, 5]                 # List data angka
print("Nilai maksimum:", cari_maks(angka))  # Cetak nilai maksimum hasil rekursi