# ===============================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ===============================================================
# Insertion Sort (Ascending)
# ===============================================================

def insertion_sort(data):
    #loop mulai dari data ke-2
    for i in range(1, len(data)):

        key = data[i]   #simpan nilai yang disisipkan
        j = i - 1       #index elemen terakhir dibagian kiri
        
        #Geser
        while j >= 0 and key < data[j]: #loop untuk membandingkan key dengan elemen sebelumnya
            data[j + 1] = data[j]
            j -= 1
        #sisipkan key ke posisi yang benar
        data[j + 1] = key
    return data

angka = [7,8,5,2,4,6]
print("Data sebelum diurutkan:", angka)
sorted_angka = insertion_sort(angka)
print("Data setelah diurutkan:", sorted_angka)