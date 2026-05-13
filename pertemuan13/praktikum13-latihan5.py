# ==========================================================
# Nama  : Muhammad Tauriq Arya Pradita
# NIM   : J0403251149
# Kelas : KELAS B
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Studi Kasus 1: Jaringan Jalan Antar Kota
# Representasi weighted graph: (Jarak/Bobot, Kota1, Kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Implementasi menggunakan Algoritma Kruskal
edges.sort()

mst = []
total_bobot = 0
connected = set()

for bobot, asal, tujuan in edges:
    # Memastikan tidak terjadi rute melingkar (cycle)
    if asal not in connected or tujuan not in connected:
        mst.append((asal, tujuan, bobot))
        total_bobot += bobot
        connected.add(asal)
        connected.add(tujuan)

print("Jaringan Jalan Terpilih (Minimum Spanning Tree):")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} (Jarak: {edge[2]})")

print("\nTotal jarak minimum =", total_bobot)

# ==========================================================
# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus 1: Jaringan Jalan Antar Kota.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Bogor - Depok (2), Depok - Jakarta (3), dan Depok - Bandung (4).
#
# 4. Berapa total bobot MST?
#    Total bobot/jarak MST adalah 9 (2 + 3 + 4).
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Edge Bogor-Jakarta (5) dan Jakarta-Bandung (6) tidak dipilih karena rute 
#    tersebut memiliki jarak yang lebih jauh dan jika dipaksakan masuk akan 
#    membentuk cycle (kota-kota tersebut sudah bisa diakses melalui Depok dengan 
#    jarak yang lebih efisien).
# ==========================================================