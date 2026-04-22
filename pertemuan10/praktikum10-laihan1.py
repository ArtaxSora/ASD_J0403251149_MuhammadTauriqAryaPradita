#=================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
#=================================================
# Latihan 1 : Node untuk BST
#=================================================
# Penjelasan Alur :
# 1. Saat fungsi `insert` dipanggil pertama kali dengan `root = None`, angka 50 dijadikan `Node` pertama (Root).
# 2. Untuk angka selanjutnya (misal 30), program membandingkannya dengan Root (50). Karena 30 < 50, angka 30 ditaruh di sebelah kiri (left).
# 3. Untuk angka 70, karena 70 > 50, ditaruh di sebelah kanan (right).
# 4. Proses ini berulang secara rekursif (memanggil dirinya sendiri) hingga menemukan tempat yang kosong (None) untuk meletakkan node baru.
# 5. Jika ada angka yang sama (seperti 50 yang muncul dua kali di list), program akan mengabaikannya karena hanya mengecek kondisi < dan >.

class Node:
    def __init__(self, data):                   # Konstruktor untuk membuat node baru
        self.data = data                        # Menyimpan nilai/angka ke dalam node
        self.left = None                        # Pointer untuk anak cabang kiri (awalnya kosong)
        self.right = None                       # Pointer untuk anak cabang kanan (awalnya kosong)

def insert(root, data):                         # Fungsi untuk memasukkan data baru ke dalam BST
    if root is None:                            # Jika posisi saat ini kosong (tidak ada node)
        return Node(data)                       # Buat dan kembalikan node baru di posisi tersebut

    if data < root.data:                        # Jika data baru lebih kecil dari data pada node saat ini
        root.left = insert(root.left, data)     # Geser ke cabang kiri, lalu lakukan insert lagi
    elif data > root.data:                      # Jika data baru lebih besar dari data pada node saat ini
        root.right = insert(root.right, data)   # Geser ke cabang kanan, lalu lakukan insert lagi

    return root                                 # Kembalikan struktur tree yang sudah diperbarui

# mengisi data BST
root = None                                     # Inisialisasi tree kosong
data_list = [50, 30, 70, 20, 40, 50, 80]        # Daftar angka yang akan dimasukkan ke dalam BST

for data in data_list:                          # Melakukan perulangan untuk setiap angka di dalam list
    root = insert(root, data)                   # Masukkan angka ke dalam BST dan perbarui root

print("BST berhasil dibuat")                    # Pesan konfirmasi

#=================================================
# Latihan 2 : Traversal BST
#=================================================
# Penjelasan Alur :
# Traversal Inorder pada BST memiliki prinsip kerja Kiri-Akar-Kanan (Left-Node-Right).
# 1. Fungsi akan terus menelusuri cabang paling kiri terlebih dahulu sampai mentok (nilai terkecil).
# 2. Setelah itu, ia akan mencetak nilai node tersebut.
# 3. Kemudian, ia akan beralih ke cabang kanan.
# 4. Efek dari traversal Inorder pada BST adalah data akan dicetak secara berurutan dari yang terkecil hingga terbesar (ascending).

def inorder(root):                              # Fungsi untuk membaca isi tree secara Inorder
    if root is not None:                        # Selama node saat ini tidak kosong (ada isinya)
        inorder(root.left)                      # 1. Telusuri terus cabang sebelah kiri
        print(root.data, end=" ")               # 2. Cetak nilai dari node saat ini (end=" " agar sejajar)
        inorder(root.right)                     # 3. Telusuri cabang sebelah kanan

print ("\nhasil inorder :")                     # Cetak teks pembuka
inorder(root)                                   # Panggil fungsi inorder mulai dari root utama

#=================================================
# Latihan 3 : search di BST
#=================================================
# Penjelasan Alur : 
# 1. Fungsi akan membandingkan `key` (angka yang dicari) dengan data di node saat ini, dimulai dari Root.
# 2. Jika sama, pencarian selesai dan mengembalikan `True`.
# 3. Jika `key` lebih kecil dari data saat ini, pencarian dilanjutkan ke cabang sebelah kiri saja.
# 4. Jika `key` lebih besar, pencarian dilanjutkan ke cabang sebelah kanan saja.
# 5. Jika sudah menelusuri sampai ujung bawah (None) tapi angka belum ditemukan, kembalikan `False`.

def search(root, key):                          # Fungsi untuk mencari data di dalam tree
    if root is None:                            # Jika node kosong (sudah sampai ujung/tree kosong)
        return False                            # Data tidak ditemukan, kembalikan False

    if root.data == key:                        # Jika nilai node saat ini sama dengan angka yang dicari
        return True                             # Data ditemukan, kembalikan True
    elif key < root.data:                       # Jika angka yang dicari lebih kecil dari node saat ini
        return search(root.left, key)           # Lanjutkan pencarian ke cabang sebelah kiri
    else:                                       # Jika angka yang dicari lebih besar dari node saat ini
        return search(root.right, key)          # Lanjutkan pencarian ke cabang sebelah kanan
    
# uji pencarian
key = 40                                        # Angka yang ingin dicari di dalam BST

if search(root, key):                           # Panggil fungsi search, jika hasilnya True:
    print("\ndata ditemukan")                   # Cetak pesan ini
else:                                           # Jika hasilnya False:
    print("\ndata tidak ditemukan")             # Cetak pesan ini