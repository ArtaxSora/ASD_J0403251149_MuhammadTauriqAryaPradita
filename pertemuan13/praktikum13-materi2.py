# ==========================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ========================================================== 
# Praktikum 13 : Implementasi Prims 
# ========================================================== 

import heapq  # Mengimpor modul heapq untuk mengelola antrean prioritas (min-heap)

# Representasi graf menggunakan Adjacency List (Dictionary di dalam Dictionary)
# Struktur: {node: {tetangga: bobot, ...}}
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Set untuk melacak node mana saja yang sudah dikunjungi (masuk ke MST)
    visited = set([start])
    
    # List untuk menyimpan kandidat edge yang akan diproses oleh min-heap
    edges = []
    
    # Memasukkan semua tetangga dari node awal ke dalam priority queue
    for neighbor, weight in graph[start].items():
        # heapq menyimpan tuple (bobot, asal, tujuan) dan otomatis mengurutkan berdasarkan bobot terkecil
        heapq.heappush(edges, (weight, start, neighbor))
    
    # List untuk menyimpan hasil akhir edge yang membentuk MST
    mst = []
    
    # Variabel untuk menghitung akumulasi bobot seluruh edge di MST
    total_weight = 0
    
    # Terus berjalan selama masih ada edge di dalam priority queue
    while edges:
        # Mengambil edge dengan bobot terkecil dari heap (pop)
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan (v) belum dikunjungi, maka edge ini valid untuk MST
        if v not in visited:
            # Tandai node v sebagai sudah dikunjungi
            visited.add(v)
            
            # Masukkan edge tersebut ke dalam daftar MST
            mst.append((u, v, weight))
            
            # Tambahkan bobotnya ke total
            total_weight += weight
            
            # Periksa semua tetangga dari node baru (v) yang baru saja ditambahkan
            for neighbor, w in graph[v].items():
                # Jika tetangga tersebut belum dikunjungi, masukkan ke priority queue
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    # Mengembalikan hasil MST dan total bobotnya
    return mst, total_weight

# Memanggil fungsi Prim dimulai dari node 'A'
mst, total = prim(graph, 'A')

# Menampilkan hasil output
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)