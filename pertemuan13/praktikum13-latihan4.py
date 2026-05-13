# ==========================================================
# Nama  : Muhammad Tauriq Arya Pradita
# NIM   : J0403251149
# Kelas : KELAS B
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Menggunakan Algoritma Kruskal
# Representasi weighted graph dalam bentuk list of tuple (bobot, asal, tujuan)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan biaya dari yang termurah
edges.sort()

mst = []
total_biaya = 0
connected = set()

print("Pembangunan Jaringan Kabel Kampus:")
for biaya, u, v in edges:
    # Jika salah satu gedung belum terkoneksi ke jaringan, maka hubungkan
    if u not in connected or v not in connected:
        mst.append((u, v, biaya))
        total_biaya += biaya
        connected.add(u)
        connected.add(v)

print("Edge jaringan yang dipilih:")
for edge in mst:
    print(f"Hubungkan {edge[0]} dan {edge[1]} dengan biaya {edge[2]}")

print(f"\nTotal biaya minimum jaringan kabel = {total_biaya}")

# ==========================================================
# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal.
#
# 2. Edge mana saja yang dipilih?
#    GedungC - GedungD (1), GedungA - GedungC (2), dan GedungB - GedungD (3).
#
# 3. Berapa total biaya minimum?
#    Total biaya minimum adalah 6 (1 + 2 + 3).
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuannya adalah menghubungkan semua gedung ke dalam satu jaringan 
#    dengan total biaya seminimal mungkin. MST menjamin semua gedung terkoneksi 
#    tanpa adanya jalur ganda (cycle) yang memboroskan kabel.
# ==========================================================