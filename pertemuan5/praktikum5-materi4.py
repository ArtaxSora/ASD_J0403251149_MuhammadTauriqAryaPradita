# ==============================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==============================================

#===============================================
#Contoh Backtracking 1: Kombinasi Biner (n)
#===============================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")

print ("========= Program Kombinasi Biner (n) =========")
n = int(input("Masukkan nilai n (jumlah digit biner) : "))
print(f"Kombinasi biner dengan {n} digit adalah :")
biner(n)