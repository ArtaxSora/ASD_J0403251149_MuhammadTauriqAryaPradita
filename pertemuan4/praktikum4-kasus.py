# ==============================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==============================================

#===============================================
#Studi kasus : sistem layanan akademik
#Implementasi  Queue =>
# Enqueue : memindahkan pointer rear (Menambah data baru dari belakang)
# Dequeue : memindahkan pointer front (Menghapus data dari depan) 
# Front-> B-> C-> Rear
#===============================================

#1) MEndefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim    = nim    #menyimpan nim mahasiswa
        self.nama   = nama   #menyimpan nama mahasiswa
        self.next   = None  #pointer ke node berikutnya

#2) Mendefinisikan Queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front  = None  #pointer ke depan
        self.rear   = None  #pointer ke belakang

    def is_empty(self):
        return self.front is None  #mengembalikan True jika queue kosong
    
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue(self,nim,nama):
        nodeBaru = Node(nim,nama)
        #jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #jika queue tidak kosong maka rear menunjuk ke node baru dan rear pindah ke node baru
        self.rear.next = nodeBaru  
        self.rear = nodeBaru  

    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        if self.is_empty():
            print("Queue kosong, tidak ada data yang bisa dihapus")
            return None

        #liahat data bgaian front, simpan di variabel data yang akan di hapus(dilayani)
        node_dilayani = self.front
        #geser pointer front ke next front
        self.front = self.front.next
        #jika front menjadi none (data antrian terakhir yang dilayani), maka front - rear = none
        if self.front is None:
            self.rear = None

        return node_dilayani
    
    def tampilkan(self):

        print("Daftar Antrian Layanan Akademi") #menampilkan daftar antrian
        current = self.front    #mulai dari front
        no = 1  #nomor urut untuk menampilkan data
        while current is not None: #selama masih ada node dalam antrian
            print(f"{no}. NIM: {current.nim}, Nama: {current.nama}") # tampilkan data mahasiswa
            current = current.next #pindah ke node berikutnya
            no += 1 #increment nomor urut

#program utama
def main():

    #initialisasi queue akademik
    antrian = queueAkademik()

    while True:
        print("==================== Sistem Antrian Layanan Akademik ====================")
        print("1. Tambah Antrian (Enqueue)")
        print("2. Layani Antrian (Dequeue)")    
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            nim = input("Masukkan NIM mahasiswa: ").strip()
            nama = input("Masukkan nama mahasiswa: ").strip()
            antrian.enqueue(nim, nama)
            print("Antrian berhasil ditambahkan.")
        elif pilihan == '2':
            mahasiswa_dilayani = antrian.dequeue()
            if mahasiswa_dilayani:
                print(f"Mahasiswa dengan NIM: {mahasiswa_dilayani.nim} dan Nama: {mahasiswa_dilayani.nama} telah dilayani.")
        elif pilihan == '3':
            antrian.tampilkan()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian layanan akademik.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()