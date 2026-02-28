# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    if n == 0:                     # Base case: jika n sudah 0
        print("Selesai")           # Tampilkan pesan selesai
        return                     # Hentikan rekursi
    
    print("Masuk:", n)             # Dicetak sebelum pemanggilan rekursif
    countdown(n - 1)               # Pemanggilan fungsi sendiri dengan n-1
    print("Keluar:", n)            # Dicetak setelah rekursi selesai (proses balik)

countdown(3)                       # Memulai fungsi dengan nilai 3