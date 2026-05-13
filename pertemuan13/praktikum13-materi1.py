# ==========================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ========================================================== 
# Praktikum 13 : Implementasi Kruskal 
# ========================================================== 

# Mendefinisikan daftar edge (sisi) dalam bentuk tuple: (bobot, node_asal, node_tujuan)
edges = [
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D')
]

# Mengurutkan semua edge berdasarkan bobot terkecil (syarat utama Algoritma Kruskal)
edges.sort()

# Inisialisasi list untuk menyimpan hasil edge yang terpilih masuk ke MST
mst = []

# Variabel untuk menjumlahkan total bobot dari seluruh edge di MST
total_weight = 0

# Menggunakan set untuk melacak node mana saja yang sudah terhubung dalam MST
connected = set()

# Melakukan iterasi melalui setiap edge yang sudah diurutkan
for weight, u, v in edges:
    
    # Mengecek apakah salah satu atau kedua node belum ada di dalam set 'connected'
    # Catatan: Logika ini adalah pendekatan sederhana untuk mencegah cycle
    if u not in connected or v not in connected:
        
        # Menambahkan edge ke dalam daftar MST
        mst.append((u, v, weight))
        
        # Menambahkan bobot edge tersebut ke total bobot MST
        total_weight += weight
        
        # Memasukkan node u dan v ke dalam set agar ditandai sebagai 'terhubung'
        connected.add(u)
        connected.add(v)

# Menampilkan judul output
print("Minimum Spanning Tree:")

# Melakukan looping untuk mencetak setiap edge yang terpilih dalam MST
for edge in mst:
    print(edge)

# Menampilkan hasil akhir total bobot dari MST yang terbentuk
print("Total bobot =", total_weight)