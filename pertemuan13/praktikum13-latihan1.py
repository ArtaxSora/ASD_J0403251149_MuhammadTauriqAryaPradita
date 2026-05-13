# ==========================================================
# Nama  : Muhammad Tauriq Arya Pradita
# NIM   : J0403251149
# Kelas : KELAS B
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid (menghubungkan semua node tanpa cycle)
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal adalah keseluruhan jaringan yang menghubungkan titik-titik (node) 
#    dan bisa memiliki lintasan melingkar (cycle). Sedangkan Spanning Tree adalah 
#    sub-graph dari graph awal yang menghubungkan semua node tanpa adanya cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena fungsi utama spanning tree adalah mencari rute atau koneksi paling 
#    esensial yang menghubungkan semua titik. Jika ada cycle, berarti ada edge 
#    (koneksi) berlebih yang sebenarnya tidak diperlukan untuk menghubungkan graph.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena pada graph dengan N buah node, Spanning Tree yang valid hanya 
#    membutuhkan tepat N-1 buah edge untuk menghubungkan semuanya. Edge sisanya 
#    dibuang untuk menghindari cycle.
# ==========================================================