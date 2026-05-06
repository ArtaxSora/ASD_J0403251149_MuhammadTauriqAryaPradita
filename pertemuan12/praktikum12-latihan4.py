#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Lokasi yang paling dekat dari Gerbang adalah:
#    Kantin dengan waktu tempuh 2 menit
#
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah:
#    6 menit (jalur terbaik: Gerbang -> Kantin -> Lab -> Aula)
#    = 2 + 4 + 1 = 7 menit
#    (Catatan: jalur lain seperti melalui Perpustakaan juga menghasilkan 10 menit)
#
# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil karena:
#    bobot setiap edge bisa berbeda-beda. Jalur langsung bisa saja lebih jauh
#    dibanding jalur tidak langsung yang memiliki total bobot lebih kecil.
#
# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini karena:
#    - Semua bobot bernilai positif (waktu tempuh tidak mungkin negatif)
#    - Tujuan adalah mencari jalur tercepat antar lokasi
#    - Algoritma ini efisien untuk graf seperti peta atau navigasi