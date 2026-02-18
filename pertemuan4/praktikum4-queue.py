# ==============================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==============================================

#===============================================
#Impelementasi Dasar : Queue Berbaris Linked List
#===============================================

# membuat class nod (Merupakan unit dasar dari linked list)
class Node:
    def __init__(self,data):
        self.data = data  #menyimpan data/nilai
        self.next = None  #pointer ke node berikutnya (Awal = none)

#Queue dengan 2 pointer : front dan rear
class Queuell: 
    def __init__(self):
        self.front = None  # node paling depan (awal antrian)
        self.rear = None # node paling belakang (akhir antrian)

    def enqueue(self,data):
        # Menambah data di belakang antrian (rear)
        nodeBaru = Node(data) #buat node baru

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.rear is None and self.front is None:
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #Rear pindah ke node baru
        self.rear = nodeBaru # rear pindah ke node baru

    def dequeue(self):
        #Menghapus data dari depan 
        #1) ambil data yang paling depan (front)
        data_terhapus = self.front.data #simpan data yang akan dihapus
        #2) geser front ke node berikutnya
        self.front = self.front.next #front pindah ke node berikutnya
        #3) jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None: #jika setelah dihapus queue menjadi kosong
            self.rear = None #rear juga harus di set ke None

        return data_terhapus #kembalikan data yang dihapus

    def tampilkan(self):
        #menampilkan isi queue dari front ke rear
        current = self.front #mulai dari front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next #pindah ke node berikutnya
        print("Rear")

#intantiasi objek class Queuell
queue = Queuell()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

queue.tampilkan()

queue.dequeue()
queue.tampilkan()
