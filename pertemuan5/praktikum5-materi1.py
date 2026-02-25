# ==============================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==============================================

#===============================================
#Materi Rekursif : Faktorial
# recursive case => 3! = 3 x 2 x 1
# base case => 0 berhenti
#===============================================

def faktorial(n):
    #base case
    if n == 0:
        return 1
    #recursive case
    return n * faktorial(n-1)  # n-1*n-2*n-3 .................. n-?
print ("========= Program Faktoril =========")
input_user = int(input("Masukkan angka : "))
print(f"{input_user}! = {faktorial(input_user)}")
