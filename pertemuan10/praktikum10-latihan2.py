#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Latihan 4 : Membuat BST yang tidak seimbang
#=================================================
# Penjelasan Logika :
# 1. Logika dasar fungsi `insert` pada BST adalah membandingkan nilai: jika data > root, maka ke kanan; jika data < root, maka ke kiri.
# 2. Karena array `data_list` berisi nilai yang sudah terurut naik secara berurutan [10, 20, 30], kondisi logika `(data > root.data)` akan selalu bernilai Benar (True) setiap kali fungsi `insert` dipanggil.
# 3. Akibatnya, eksekusi kode akan selalu masuk ke blok `root.right = insert(...)`. Logika untuk masuk ke cabang kiri (`root.left`) sama sekali tidak pernah terpenuhi dan dieksekusi.
# 4. Ketiadaan logika penyeimbang otomatis (self-balancing mechanism seperti pada algoritma AVL atau Red-Black Tree) di dalam fungsi `insert` ini membuat tree dibiarkan tumbuh ke satu sisi saja secara terus-menerus.
# 5. Secara struktural, logika ini mengubah kompleksitas struktur data BST yang seharusnya efisien menjadi sangat tidak efisien (berubah menjadi linear mirip Linked List).

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):                               # Konstruktor untuk membuat node baru
        self.data = data                                    # Menyimpan nilai/angka ke dalam node
        self.left = None                                    # Pointer untuk anak cabang kiri (awalnya kosong)
        self.right = None                                   # Pointer untuk anak cabang kanan (awalnya kosong)

# Fungsi insert untuk BST
def insert(root, data):                                     # Fungsi untuk memasukkan data baru ke dalam BST
    if root is None:                                        # Jika posisi saat ini kosong (base case rekursi)
        return Node(data)                                   # Buat dan kembalikan node baru di posisi tersebut
    
    if data < root.data:                                    # LOGIKA KIRI: Jika data lebih kecil (tidak pernah terjadi di kasus ini)
        root.left = insert(root.left, data)                 # Buat node di subtree kiri
    elif data > root.data:                                  # LOGIKA KANAN: Jika data lebih besar (selalu True di kasus ini)
        root.right = insert(root.right, data)               # Buat node di subtree kanan

    return root                                             # Kembalikan struktur tree yang sudah diperbarui

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):                                         # Fungsi penelusuran dengan urutan Akar-Kiri-Kanan
    if root is not None:                                    # Jika node tidak kosong
        print(root.data, end=" ")                           # Cetak nilai node saat ini
        preorder(root.left)                                 # Telusuri logika cabang kiri
        preorder(root.right)                                # Telusuri logika cabang kanan

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):          # Fungsi rekursif untuk visualisasi bentuk tree
    if root is not None:                                    # Selama node ada isinya
        print("  " * level + f"{posisi}: {root.data}")      # Cetak dengan indentasi (level) untuk visualisasi hierarki
        tampil_struktur(root.left, level + 1, "L")          # Visualisasikan cabang Kiri (L)
        tampil_struktur(root.right, level + 1, "R")         # Visualisasikan cabang Kanan (R)

# -----------------------------
# Program utama
# -----------------------------
root = None                                                 # Inisialisasi awal tree dalam keadaan kosong

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]                                    # Array terurut yang memicu kondisi worst-case BST

for data in data_list:                                      # Iterasi untuk memasukkan data
    root = insert(root, data)                               # Eksekusi fungsi insert
    
print("Preorder BST:")                                      # Cetak teks pembuka
preorder(root)                                              # Panggil fungsi preorder

print("\n\nStruktur BST:")                                  # Cetak teks pembuka untuk visualisasi
tampil_struktur(root)                                       # Panggil fungsi visualisasi struktur