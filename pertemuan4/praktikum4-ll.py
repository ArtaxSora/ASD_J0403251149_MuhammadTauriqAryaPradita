# ==============================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==============================================

#===============================================
#Impelementasi Dasar : Node pasa Linked Listsssss
#===============================================


# membuat class nod (Merupakan unit dasar dari linked list)
class Node:
    def __init__(self,data):
        self.data = data  #menyimpan data/nilai
        self.next = None  #menyimpan alamat node selanjutnya

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan node A->B->C->None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) menentukan node pertama sebagai head
head = nodeA

# 4) Traversal : menelusuri dari head hingga none
current = head
while current is not None:
    print(current.data)  #menampilkan data pada node saat ini
    current = current.next  #pindah ke node berikutnya

# ==============================================
# Implementasi Dasar : Linked List + Insert awal
# ==============================================

class LinkedList: #class inplementasi stack
    def __init__(self):
        self.head = None  #inisialisasi head sebagai None

    def insert_awal(self,data): # push dalam stack
        #1) buat node baru
        nodeBaru = Node(data) #panggil class node

        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3) Head pindah  ke node baru
        self.head = nodeBaru

    def hapus_awal(self): #pop dalam stack
        data_terhapus = self.head.data  #peek dalam stack
        # menggeser head ke node berikutnya
        self.head = self.head.next
        print("node yang dihapus adalah:", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("===list baru===")
ll = LinkedList() # instantiasi objek  ke class linked list
ll.insert_awal("x")
ll.insert_awal("y")
ll.insert_awal("z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()