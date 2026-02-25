# ==============================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==============================================

#===============================================
#Materi Rekursif : call stack
# Tracing suatu bilangan yang masuk atau keluar
# input 3
# masuk 1 - 2 - 3
# #keluar 
#===============================================

def hitung(n):
    #base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk :", n)
    hitung(n-1) #recursive case
    print("Keluar :", n)

print ("========= Program Call Stack =========")
input_user = int(input("Masukkan angka : "))   
hitung(input_user)

