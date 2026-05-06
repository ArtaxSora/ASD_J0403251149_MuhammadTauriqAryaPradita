#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# A -> B -> D
# A -> C -> D
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Total bobot jalur A -> B -> D adalah:
#    A -> B (4) + B -> D (5) = 9
#
# 2. Total bobot jalur A -> C -> D adalah:
#    A -> C (2) + C -> D (1) = 3
#
# 3. Jalur terpendek yang dipilih adalah:
#    A -> C -> D, karena memiliki total bobot lebih kecil (3 < 9)
#
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit
#    karena yang diperhitungkan adalah total bobot (weight), bukan jumlah langkah.
#    Bisa saja jalur dengan lebih sedikit edge memiliki bobot besar, sedangkan
#    jalur dengan lebih banyak edge justru memiliki total bobot yang lebih kecil.