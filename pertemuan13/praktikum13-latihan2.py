# ==========================================================
# Nama  : Muhammad Tauriq Arya Pradita
# NIM   : J0403251149
# Kelas : KELAS B
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Edge ('C', 'D') dengan bobot 1.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal menggunakan pendekatan Greedy, di mana solusi optimal 
#    (biaya terendah) dicari dengan selalu mengambil bobot terkecil yang tersedia 
#    di setiap langkahnya.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobotnya adalah 6 (1 + 2 + 3).
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge ('A', 'B') dengan bobot 4 dan ('A', 'D') dengan bobot 5 tidak dipilih 
#    karena akan membentuk cycle. Node A, B, dan D sudah saling terhubung melalui 
#    edge yang lebih murah.
# ==========================================================