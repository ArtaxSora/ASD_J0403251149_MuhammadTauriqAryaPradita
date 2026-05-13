# ==========================================================
# Nama  : Muhammad Tauriq Arya Pradita
# NIM   : J0403251149
# Kelas : KELAS B
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge dari 'A' ke 'C' dengan bobot 2.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim melihat seluruh edge yang menghubungkan himpunan node yang sudah 
#    dikunjungi (visited) ke node yang belum dikunjungi. Ia selalu memilih edge 
#    dengan bobot paling kecil dari kumpulan pilihan tersebut.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Prim "tumbuh" dari satu node awal dan memperluas MST secara terhubung ke 
#    node tetangga dengan bobot terkecil. Kruskal memilih secara acak dari semua 
#    edge di seluruh graph dari bobot terkecil asalkan tidak membentuk cycle.
# ==========================================================