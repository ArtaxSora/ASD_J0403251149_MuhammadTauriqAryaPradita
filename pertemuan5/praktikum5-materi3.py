# ==============================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==============================================

#===============================================
#Materi Rekursif : Menjumlahkan Elemen List
#===============================================

def jumlahkan_list(data,index=0):
    #base case
    if index == len(data):
        return 0
    
    #recursive case
    return data[index] + jumlahkan_list(data,index+1)

print ("========= Program Menjumlahkan Elemen List =========")
input_user = input("Masukkan angka-angka (pisahkan dengan koma) : ")
data_list = [int(x) for x in input_user.split(",")]
print(f"Jumlah elemen dalam list {data_list} adalah : {jumlahkan_list(data_list)}")
