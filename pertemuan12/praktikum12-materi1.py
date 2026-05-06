#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Materi 1 : Studi Kasus Dijkstra 
#=================================================

import heapq  # Mengimpor modul heapq untuk menggunakan priority queue (antrian prioritas)

# Representasi graph dalam bentuk dictionary (adjacency list)
graph = {
    'A': {'B': 4, 'C': 2},  # Node A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},          # Node B terhubung ke D (bobot 5)
    'C': {'D': 1},          # Node C terhubung ke D (bobot 1)
    'D': {}                 # Node D tidak memiliki tetangga
}

def dijkstra(graph, start):
    # Membuat dictionary untuk menyimpan jarak minimum dari start ke setiap node
    distances = {node: float('inf') for node in graph}  # Inisialisasi semua jarak = tak hingga
    
    distances[start] = 0  # Jarak dari start ke dirinya sendiri adalah 0

    # Membuat priority queue (min-heap) untuk memilih node dengan jarak terkecil
    pq = [(0, start)]  # Format: (jarak, node)

    while pq:  # Loop selama masih ada node dalam antrian
        current_distance, current_node = heapq.heappop(pq)  
        # Mengambil node dengan jarak terkecil dari priority queue

        # Iterasi semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight  
            # Menghitung jarak baru ke neighbor melalui current_node

            # Jika jarak baru lebih kecil dari jarak yang sudah tersimpan
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Update jarak minimum
                
                # Masukkan neighbor ke priority queue dengan jarak terbaru
                heapq.heappush(pq, (distance, neighbor))

    return distances  # Mengembalikan hasil jarak minimum ke semua node

# Memanggil fungsi dijkstra dengan node awal 'A'
hasil = dijkstra(graph, 'A')

print(hasil)  # Menampilkan hasil jarak terpendek dari A ke semua node