# ================================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ================================================================

# ================================================================
# Bubble Sort
# ================================================================

# Definisi: Bubble Sort adalah algoritma pengurutan paling sederhana. 
# Dinamakan "Bubble" karena elemen yang besar akan "mengapung" dan bertukar posisi akhir seperti gelembung.

# Konsep: Bandingkan dua angka bersebelahan. 
# Jika angka kiri lebih besar dari angka kanan, tukar posisinya. Ulangi sampai semua urut.


# CARA KERJA
# Bayangkan deretan angka: [5, 1, 4, 2].
# Iterasi 1: Bandingkan 5 dan 1. (5 > 1? Ya, Tukar). Deret jadi [1, 5, 4, 2].
#            Bandingkan 5 dan 4. (5 > 4? Ya, Tukar). Deret jadi [1, 4, 5, 2].
#            Bandingkan 5 dan 2. (5 > 2? Ya, Tukar). Deret jadi [1, 4, 2, 5].
#            Sekarang, angka 5 sudah di posisi paling benar (paling kanan).



def bubble_sort(data):
    # Mengambil panjang list untuk menentukan berapa kali kita harus melakukan pengecekan
    n = len(data)
    
    # Loop luar: Berfungsi sebagai putaran. 
    # Setiap putaran, satu angka terbesar akan mengapung untuk berpindah ke posisi paling kanan
    for i in range(n):
        print(f"Iterasi ke-{i+1}:")
        
        # Loop dalam: Melakukan perbandingan antar angka.
        # Batas (n - i - 1) digunakan karena di setiap iterasi ke-i, 
        # sebanyak 'i' elemen di akhir list sudah berada di posisi yang benar.
        for j in range(0, n - i - 1):
            
            # Logika: Bandingkan elemen saat ini dengan elemen di sebelahnya.
            # Jika angka di kiri (data[j]) lebih besar dari angka di kanan (data[j+1]):
            if data[j] > data[j + 1]:
                
                # Proses Penukaran (Swap)
                # Sisi kiri (data[j], data[j+1]) akan diisi oleh nilai dari sisi kanan.
                data[j], data[j + 1] = data[j + 1], data[j]
                
                # Cetak progres setiap kali terjadi perubahan posisi
                print(f"  Tukar {data[j+1]} dengan {data[j]} -> {data}")
            else:
                # Jika angka sudah benar (kiri <= kanan), tidak perlu ditukar.
                print(f"  {data[j]} tidak lebih besar dari {data[j+1]}, tetap.")

# --- Bagian Eksekusi ---

# Data mentah yang akan diurutkan secara menaik (Ascending)
angka = [64, 34, 25, 12, 22]



print(f"Data Awal: {angka}\n")

# Memanggil fungsi bubble_sort dan mengirimkan list 'angka' ke dalamnya
bubble_sort(angka)

# Menampilkan hasil akhir setelah semua iterasi selesai
print(f"\nData Akhir Terurut: {angka}")