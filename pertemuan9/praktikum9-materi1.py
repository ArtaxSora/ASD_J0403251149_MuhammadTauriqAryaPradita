#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
#Latihan 1 : Membuat Node
#=================================================

#Class node digunakan unutuk dasar dari
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        pass

#Membuat root
root = Node("A")

#Menampilkan isi Node
print("Data pada root", root.data)
print("Child kiri root", root.left)
print("Child kanan root", root.right)

#Pembahasan :
# Kode ini mendemonstrasikan pembuatan node dasar dalam struktur data pohon (tree).
# Class Node memiliki tiga atribut: data untuk menyimpan nilai node, left untuk child kiri, dan right untuk child kanan.
# Root node dibuat dengan data "A", dan kedua child-nya diinisialisasi sebagai None karena belum ada node anak.
# Output menunjukkan bahwa data root adalah "A", sedangkan child kiri dan kanan adalah None.
# Konsep ini merupakan dasar untuk membangun struktur pohon biner, di mana setiap node dapat memiliki maksimal dua anak.