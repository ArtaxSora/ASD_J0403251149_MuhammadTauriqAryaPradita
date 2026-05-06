#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Materi 2 : Studi Kasus Bellman-Ford 
#=================================================

def bellman_ford(graph, start):
    # Membuat dictionary untuk menyimpan jarak minimum dari start ke setiap node
    distances = {node: float('inf') for node in graph}  # Inisialisasi semua jarak = tak hingga
    
    distances[start] = 0  # Jarak dari node awal ke dirinya sendiri adalah 0

    # Proses relaksasi dilakukan sebanyak (jumlah node - 1) kali
    for _ in range(len(graph) - 1):

        # Iterasi setiap node dalam graph
        for node in graph:

            # Iterasi setiap tetangga dan bobot dari node saat ini
            for neighbor, weight in graph[node].items():

                # Cek apakah jalur melalui node ini lebih pendek
                if distances[node] + weight < distances[neighbor]:
                    
                    # Update jarak jika ditemukan jalur yang lebih pendek
                    distances[neighbor] = distances[node] + weight

    return distances  # Mengembalikan hasil jarak minimum dari start ke semua node