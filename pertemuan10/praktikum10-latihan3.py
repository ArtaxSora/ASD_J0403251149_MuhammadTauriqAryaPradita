#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang
#=================================================
# Penjelasan Alur Logika (Rotasi Kiri):
# 1. Posisi Awal: Tree miring ke kanan (10 -> 20 -> 30). Akar (root) saat ini adalah 10.
# 2. Pemanggilan: Fungsi `rotate_left` dipanggil dengan `x` = Node(10).
# 3. Identifikasi: 
#    - `y` diset menjadi anak kanan dari 10, yaitu Node(20).
#    - `T2` diset menjadi anak kiri dari 20. Karena tidak ada, `T2` bernilai None.
# 4. Eksekusi Rotasi:
#    - Node 10 (`x`) dipindah ke bawah, ditugaskan menjadi anak kiri dari 20 (`y.left = x`).
#    - Posisi anak kanan dari 10 yang kosong tadi diisi oleh `T2` (`x.right = T2`), dalam hal ini tetap None.
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

# Fungsi rotasi kiri
def rotate_left(x):                                         # Fungsi utama untuk menyeimbangkan tree (Rotasi Kiri)
    # x adalah root lama (dalam kasus ini: 10)
    y = x.right                                             # y adalah child kanan x (dalam kasus ini: 20)
    T2 = y.left                                             # T2 adalah subtree kiri milik y (disimpan sementara)
    
    # Proses rotasi
    y.left = x                                              # x (10) ditarik turun menjadi child kiri dari y (20)
    x.right = T2                                            # child kanan x (10) diganti dengan T2 (None)
    
    # y menjadi root baru
    return y                                                # Kembalikan y (20) agar menjadi root utama tree

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang (Right-Skewed):
# 10 -> 20 -> 30
root = Node(10)                                             # Membuat root awal dengan nilai 10
root.right = Node(20)                                       # Menambahkan 20 di sebelah kanan 10
root.right.right = Node(30)                                 # Menambahkan 30 di sebelah kanan 20

print("Preorder sebelum rotasi kiri:")                      # Cetak teks pembuka
preorder(root)                                              # Hasil: 10 20 30

print("\n\nStruktur sebelum rotasi kiri:")                  # Cetak visualisasi awal
tampil_struktur(root)                                       # Akan terlihat 10 punya kanan 20, 20 punya kanan 30

# Melakukan rotasi kiri pada root
root = rotate_left(root)                                    # Panggil fungsi rotasi dan perbarui letak root

print("\nPreorder sesudah rotasi kiri:")                    # Cetak teks pembuka setelah rotasi
preorder(root)                                              # Hasil: 20 10 30 (Akar-Kiri-Kanan)

print("\n\nStruktur sesudah rotasi kiri:")                  # Cetak visualisasi akhir
tampil_struktur(root)                                       # Akan terlihat 20 jadi root, 10 di Kiri, 30 di Kanan