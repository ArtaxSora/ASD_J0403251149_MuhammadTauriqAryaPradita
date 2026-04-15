#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
#Latihan 5 : Membuat Node traversal postorder
#=================================================

#Class node digunakan unutuk dasar pada tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan
        pass

#membuat fungsi inorder : left -> root -> right
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

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
print("postorder Traversal: ",end= "")
postorder(root)

#Pembahasan : 
# Postorder traversal adalah metode traversal pohon biner dimana kita mengunjungi subtree kiri terlebih dahulu,
# kemudian subtree kanan, dan terakhir node root.
# Urutan traversal postorder adalah: kiri -> kanan -> root.
# Pada kode ini, binary tree yang dibuat sama seperti sebelumnya dengan root "A".
# Fungsi postorder() akan mencetak nilai node dalam urutan postorder.
# Output yang dihasilkan adalah: D E B F C A
# Ini sesuai dengan aturan postorder: mulai dari kiri paling bawah, lalu kanan, dan akhirnya root.