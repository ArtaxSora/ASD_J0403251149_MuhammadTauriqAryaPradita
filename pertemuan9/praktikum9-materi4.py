#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
#Latihan 4 : Membuat Node traversal inorder
#=================================================

#Class node digunakan unutuk dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        pass

#membuat fungsi inorder : left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

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
print("Inorder Traversal: ",end= "")
inorder(root)

#Pembahasan : 
# Inorder traversal adalah metode traversal pohon biner dimana kita mengunjungi subtree kiri terlebih dahulu,
# kemudian node root, dan terakhir subtree kanan.
# Urutan traversal inorder adalah: kiri -> root -> kanan.
# Pada kode ini, binary tree yang dibuat sama seperti sebelumnya dengan root "A".
# Fungsi inorder() akan mencetak nilai node dalam urutan inorder.
# Output yang dihasilkan adalah: D B E A C F
# Ini sesuai dengan aturan inorder: mulai dari kiri paling bawah, lalu naik ke root, dan ke kanan.