#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
#Latihan 6 : Stuktur Organisasi Perusahaan
#=================================================

#Class node digunakan unutuk dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        pass

#membuat fungsi Preorder
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#Membuat sebuah node root
root = Node("Direktur")

#Membuat child level 1
root.left = Node("Manager A")
root.right = Node("Manager B")

#membuat child level 2
root.left.left = Node("Staf 1")
root.left.right = Node("Staf 2")

root.right.right = Node("Staf 3")

#Menampilkan isi Node
print("Struktur Organisasi:(preorder) ",end= "")
preorder(root)

#Pembahasan : 
# Kode ini menggambarkan struktur organisasi perusahaan menggunakan binary tree.
# Root adalah "Direktur", yang memiliki dua manager: "Manager A" dan "Manager B".
# "Manager A" memiliki dua staf: "Staf 1" dan "Staf 2", sedangkan "Manager B" memiliki satu staf: "Staf 3".
# Preorder traversal digunakan untuk menampilkan struktur organisasi dari atas ke bawah.
# Output yang dihasilkan adalah: Direktur Manager A Staf 1 Staf 2 Manager B Staf 3
# Ini menunjukkan hierarki organisasi dimulai dari direktur, lalu manager, dan staf.