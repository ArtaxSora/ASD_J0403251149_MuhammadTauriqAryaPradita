#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
#Latihan 3 : Membuat Node traversal preorder
#=================================================

#Class node digunakan unutuk dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        pass

#membuat fungsi preorder
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#Membuat sebuah node root
root = Node("A")

#Membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

root.right.right = Node("F")

#Menampilkan isi Node
print("Preorder Traversal: ",end= "")
preorder(root)

#Pembahasan : 
# Preorder traversal adalah salah satu cara untuk menjelajahi (traversal) pohon biner.
# Dalam preorder, kita mengunjungi node root terlebih dahulu, kemudian subtree kiri, dan terakhir subtree kanan.
# Pada kode ini, kita membuat sebuah binary tree dengan root "A", yang memiliki child kiri "B" dan kanan "C".
# "B" memiliki child kiri "D" dan kanan "E", sedangkan "C" memiliki child kanan "F".
# Fungsi preorder() akan mencetak nilai node dalam urutan: root, kiri, kanan.
# Output yang dihasilkan adalah: A B D E C F
# Ini sesuai dengan urutan preorder traversal.