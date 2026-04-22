#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Latihan 6 : Rotasi Kanan pada BST Tidak Seimbang
#=================================================
# Penjelasan Alur Logika (Rotasi Kanan):
# 1. Posisi Awal: Tree miring ke kiri (30 -> 20 -> 10). Akar (root) saat ini adalah 30.
# 2. Pemanggilan: Fungsi `rotate_right` dipanggil dengan `y` = Node(30).
# 3. Identifikasi: 
#    - `x` diset menjadi anak kiri dari 30, yaitu Node(20).
#    - `T2` diset menjadi anak kanan dari 20. Karena tidak ada, `T2` bernilai None.
# 4. Eksekusi Rotasi:
#    - Node 30 (`y`) ditarik turun dan bergeser menjadi anak kanan dari 20 (`x.right = y`).
#    - Posisi anak kiri dari 30 yang kosong diisi oleh `T2` (`y.left = T2`), yang dalam hal ini None.
# 5. Hasil Akhir: Fungsi mengembalikan Node(20) sebagai Akar (root) yang baru.
#    - Sekarang 20 ada di puncak. 10 ada di kiri, dan 30 ada di kanan. Tree menjadi seimbang!

# Class Node
class Node:
    def __init__(self, data):                               # Konstruktor untuk membuat node
        self.data = data                                    # Menyimpan nilai/angka node
        self.left = None                                    # Pointer child kiri
        self.right = None                                   # Pointer child kanan

# Fungsi preorder untuk melihat isi tree
def preorder(root):                                         # Penelusuran Akar-Kiri-Kanan
    if root is not None:                                    # Selama node tidak kosong
        print(root.data, end=" ")                           # Cetak nilai node
        preorder(root.left)                                 # Telusuri cabang kiri
        preorder(root.right)                                # Telusuri cabang kanan

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):          # Visualisasi bentuk hierarki tree
    if root is not None:                                    # Selama node tidak kosong
        print("  " * level + f"{posisi}: {root.data}")      # Cetak dengan indentasi level
        tampil_struktur(root.left, level + 1, "L")          # Visualisasikan cabang Kiri
        tampil_struktur(root.right, level + 1, "R")         # Visualisasikan cabang Kanan

# Fungsi rotasi kanan
def rotate_right(y):                                        # Fungsi utama untuk menyeimbangkan tree (Rotasi Kanan)
    # y adalah root lama (dalam kasus ini: 30)
    x = y.left                                              # x adalah child kiri y (dalam kasus ini: 20)
    T2 = x.right                                            # T2 adalah subtree kanan milik x (disimpan sementara)
    
    # Proses rotasi
    x.right = y                                             # y (30) ditarik turun menjadi child kanan dari x (20)
    y.left = T2                                             # child kiri y (30) diganti dengan T2 (None)
    
    # x menjadi root baru
    return x                                                # Kembalikan x (20) agar menjadi root utama tree

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang (Left-Skewed):
# Data: 30, 20, 10
root = Node(30)                                             # Membuat root awal dengan nilai 30
root.left = Node(20)                                        # Menambahkan 20 di sebelah kiri 30
root.left.left = Node(10)                                   # Menambahkan 10 di sebelah kiri 20

print("Preorder sebelum rotasi kanan:")                     # Cetak teks pembuka
preorder(root)                                              # Hasil: 30 20 10

print("\n\nStruktur sebelum rotasi kanan:")                 # Cetak visualisasi awal
tampil_struktur(root)                                       # Terlihat 30 punya kiri 20, 20 punya kiri 10

# Melakukan rotasi kanan pada root
root = rotate_right(root)                                   # Panggil fungsi rotasi dan perbarui letak root

print("\nPreorder sesudah rotasi kanan:")                   # Cetak teks pembuka setelah rotasi
preorder(root)                                              # Hasil: 20 10 30

print("\n\nStruktur sesudah rotasi kanan:")                 # Cetak visualisasi akhir
tampil_struktur(root)                                       # Terlihat 20 jadi root, 10 di Kiri, 30 di Kanan