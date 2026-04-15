#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
#Latihan 2 : Membuat Node Tree
#=================================================

#Class node digunakan unutuk dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        pass

#Membuat sebuah node root
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.left = Node("F")
root.right.right = Node("G")

#Menampilkan isi Node
print("Data pada root", root.data)
print("Child kiri root", root.left.data)
print("Child kanan root", root.right.data)
print("Child kiri child dari Node B", root.left.left.data)
print("Child kanan child dari Node B", root.left.right.data)
print("Child kiri child dari Node C", root.right.left.data)
print("Child kanan child dari Node C", root.right.right.data)

#Pembahasan :
# Kode ini menunjukkan cara membangun struktur pohon biner lengkap.
# Root node "A" memiliki dua anak: "B" di kiri dan "C" di kanan.
# Node "B" memiliki anak kiri "D" dan kanan "E".
# Node "C" memiliki anak kiri "F" dan kanan "G".
# Ini membentuk pohon biner dengan tinggi 2.
# Output menampilkan data dari setiap node, menunjukkan bagaimana data disimpan dan diakses dalam struktur pohon.
# Konsep ini penting untuk memahami traversal dan operasi pada pohon biner.