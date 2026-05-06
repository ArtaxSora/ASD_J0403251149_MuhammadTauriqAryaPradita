#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==========================================================
# Studi Kasus: Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq  # Untuk priority queue (min-heap)

# 1. Representasi graph berbobot menggunakan dictionary
# Setiap kota terhubung dengan kota lain beserta bobot (jarak)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra untuk mencari jarak terpendek
def dijkstra(graph, start):
    # Inisialisasi semua jarak = tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue untuk memilih node dengan jarak terkecil
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Jika sudah ada jalur lebih baik, lewati
        if current_distance > distances[current_node]:
            continue

        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# 3. Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma
hasil = dijkstra(graph, start_node)

# 4. Output jarak terpendek
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Node awal yang digunakan adalah: Bogor
#
# 2. Node dengan jarak paling kecil dari node awal:
#    Depok (jarak 2)
#
# 3. Node dengan jarak paling besar dari node awal:
#    Bandung (jarak 8)
#
# 4. Cara kerja Dijkstra pada kasus ini:
#    - Algoritma mulai dari Bogor dengan jarak 0
#    - Memilih jalur terpendek sementara ke tetangga (Depok dan Jakarta)
#    - Memperbarui jarak jika ditemukan jalur yang lebih pendek melalui node lain
#    - Menggunakan priority queue untuk selalu memilih node dengan jarak terkecil
#    - Proses berlanjut sampai semua node mendapatkan jarak minimum