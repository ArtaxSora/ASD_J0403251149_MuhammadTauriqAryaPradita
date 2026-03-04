# ==========================================================
# Nama : Muhammad Tauriq Arya Pradita
# NIM  : J0403251149
# KELAS: KELAS B
# ==========================================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no              # Menyimpan nomor antrian
        self.nama = nama          # Menyimpan nama pelanggan
        self.servis = servis      # Menyimpan jenis servis
        self.next = None          # Pointer ke node berikutnya (awal = None)


class QueueBengkel:
    def __init__(self):
        self.front = None         # Menunjuk pelanggan paling depan
        self.rear = None          # Menunjuk pelanggan paling belakang

    def enqueue(self, no, nama, servis):
        new_node = Node(no, nama, servis)   # Membuat node baru
        
        if self.rear is None:               # Jika antrian masih kosong
            self.front = self.rear = new_node  # Front dan rear menunjuk node baru
            print("Pelanggan berhasil ditambahkan.")
            return
        
        self.rear.next = new_node           # Node terakhir menunjuk ke node baru
        self.rear = new_node                # Rear dipindah ke node baru
        print("Pelanggan berhasil ditambahkan.")

    def dequeue(self):
        if self.front is None:              # Jika antrian kosong
            print("Antrian kosong, tidak ada yang dilayani.")
            return
        
        temp = self.front                   # Simpan node terdepan
        print(f"Melayani pelanggan: {temp.no} - {temp.nama} ({temp.servis})")
        
        self.front = self.front.next        # Front maju ke node berikutnya
        
        if self.front is None:              # Jika setelah dihapus menjadi kosong
            self.rear = None                # Rear juga dikosongkan

    def tampilkan(self):
        if self.front is None:              # Jika antrian kosong
            print("Antrian kosong.")
            return
        
        current = self.front                # Mulai dari depan
        print("\nDaftar Antrian:")
        
        while current:                      # Loop selama node masih ada
            print(f"No: {current.no}, Nama: {current.nama}, Servis: {current.servis}")
            current = current.next          # Pindah ke node berikutnya


def main():
    q = QueueBengkel()                      # Membuat objek antrian
    
    while True:                             # Loop utama program
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilih = input("Pilih menu: ")       # Input pilihan user
        
        if pilih == "1":
            no = input("No Antrian : ")     # Input nomor antrian
            nama = input("Nama : ")         # Input nama pelanggan
            servis = input("Servis : ")     # Input jenis servis
            q.enqueue(no, nama, servis)     # Tambahkan ke antrian
        
        elif pilih == "2":
            q.dequeue()                     # Layani pelanggan terdepan
        
        elif pilih == "3":
            q.tampilkan()                   # Tampilkan seluruh antrian
        
        elif pilih == "4":
            break                           # Keluar dari program
        
        else:
            print("Pilihan tidak valid")    # Jika input tidak sesuai


if __name__ == "__main__":
    main()                                  # Menjalankan fungsi utama