# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Muhammad Tauriq Arya Pradita
# NIM     : J0403251149
# Kelas   : TPL-B2
# ==============================================================================

nama_file = "buku.txt"

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {} #dictionary kosong untuk menyimpan data buku
    
    with open(nama_file, "r", encoding="utf-8") as file: # Membuka file
        for baris in file:              # Iterasi setiap baris dalam file
            baris = baris.strip()       # Menghilangkan whitespace di awal dan akhir baris
            
            kode_buku, judul, harga = baris.split(",")          # Memisahkan string dengan koma
            database_buku[kode_buku] = {                        # Menambahkan data ke dictionary dengan kode_buku sebagai key
                "judul": judul,
                "harga": int(harga)                             # Konversi harga dari string ke integer
            }

    return database_buku                                        # Mengembalikan dictionary yang telah diisi dengan data dari file

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.judul = judul          # Menyimpan data judul buku sebagai value dalam node
        self.next = None            # Pointer yang menunjuk ke node berikutnya


class LinkedListPromosi:
    def __init__(self):
        self.head = None            # Inisialisasi head pointer yang menunjuk ke node pertama

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        node_baru = Node(judul)         # Membuat node baru dengan judul yang diberikan
        
        if self.head is None:           # Jika list kosong (head == None), jadikan node baru sebagai head
            self.head = node_baru
        else:                           # Jika list tidak kosong, cari node terakhir
            node_saat_ini = self.head
            
            while node_saat_ini.next is not None:   # Looping sampai menemukan node terakhir
                node_saat_ini = node_saat_ini.next

            node_saat_ini.next = node_baru          # Menghubungkan node terakhir dengan node baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        if self.head is None:       # Cek apakah list kosong                        
            print("Daftar promosi masih kosong!")
            return
        
        node_saat_ini = self.head   # Inisialisasi node saat ini dengan head (node pertama)
        nomor_urut = 1              # Inisialisasi counter untuk numbering
        
        print("\n=== DAFTAR BUKU PROMOSI ===")
        while node_saat_ini is not None:                    # Looping traversal: selama node_saat_ini bukan None
            print(f"{nomor_urut}. {node_saat_ini.judul}")   # Menampilkan informasi node (judul buku) dengan nomor urut
            
            node_saat_ini = node_saat_ini.next              # Pindah ke node berikutnya
            nomor_urut += 1                                 # Increment counter untuk nomor urut berikutnya

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []   # Inisialisasi list kosong untuk menyimpan data antrian

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        self.antrean.append(nama_pelanggan)                     # Menambahkan nama pelanggan ke akhir list (append ke belakang)
        print(f"✓ {nama_pelanggan} telah masuk antirean!")     # Menampilkan informasi pelanggan yang baru ditambahkan  

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        if len(self.antrean) == 0:                                              # Validasi: cek apakah antirean kosong atau tidak
            print("Antirean kosong! Tidak ada pelanggan untuk dilayani.")       # Jika kosong, tampilkan pesan dan return None
            return None
        
        pelanggan_dilayani = self.antrean.pop(0)            # Menghapus dan mengambil elemen pertama dari list (index 0)
        print(f"✓ Melayani: {pelanggan_dilayani}")         # Menampilkan informasi pelanggan yang sedang dilayani
        
        return pelanggan_dilayani                           # Mengembalikan nama pelanggan yang telah dilayani

    def tampilkan_antrean(self): # Ide untuk menambahkan function
        """Menampilkan semua pelanggan yang sedang menunggu dalam antirean"""
        print("\n" + "="*50)
        print("--- STATUS ANTIREAN KASIR ---")
        print("="*50)
        
        if len(self.antrean) == 0:                                           # Validasi: cek apakah antirean kosong atau tidak
            print("Antirean kosong! Tidak ada pelanggan yang menunggu.")     # Jika antirean kosong, tampilkan pesan khusus
            print("="*50)
            return
        
        total_pelanggan = len(self.antrean)                                  # Menampilkan jumlah total pelanggan yang menunggu
        print(f"Total Pelanggan Menunggu: {total_pelanggan}")
        print("-"*50)
        print("Urutan Pelanggan:")
        for nomor, nama_pelanggan in enumerate(self.antrean,1):             # Iterasi melalui setiap pelanggan dalam antirean
            print(f"  {nomor}. {nama_pelanggan}")
        print("="*50)

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """Mengurutkan list harga secara manual menggunakan Insertion Sort"""
    data = list_harga 
    
    n = len(data)               # Panjang dari list yang akan diurutkan
    
    for i in range(1, n):       # Looping dari elemen kedua (index 1) hingga akhir list
        key = data[i]           # Menyimpan elemen yang akan diproses (key)
        j = i - 1               # Pointer untuk membandingkan dengan elemen sebelumnya
        
        # Looping mundur: selama j >= 0 dan elemen sebelumnya lebih besar dari key
        # Ini memastikan pencarian posisi yang benar untuk key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]       # Shift elemen yang lebih besar ke posisi berikutnya (geser ke kanan)
            j -= 1                      # Pindah ke elemen sebelumnya
        
        data[j + 1] = key        # Menempatkan key di posisi yang sudah benar
    
    return data                  # Mengembalikan list yang sudah terurut

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)                             # Membaca database buku dari file dan menyimpan ke dictionary
    list_promosi = LinkedListPromosi()                              # Membuat instance Linked List untuk manajemen daftar promosi
    antrean_toko = AntreanKasir()                                   # Membuat instance Queue untuk manajemen antirean kasir
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]      # Data riwayat transaksi untuk contoh data sorting

    # Loop utama program: selama user belum memilih untuk keluar
    while True:
        # Menampilkan menu pilihan utama
        print("\n" + "="*40)
        print("--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("="*40)
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        print("="*40)
        
        # Menerima input pilihan dari user
        pilihan = input("Pilih menu (1-5): ")

        # Kondisi 1: Menampilkan Katalog Buku
        if pilihan == '1':
            print("\n=== KATALOG BUKU ===")
            if len(data_buku) == 0:       # Validasi: cek apakah database kosong
                print("Database buku kosong! Silakan tambahkan data ke file buku.txt")
            else:                         # Iterasi dan tampilkan setiap buku dari dictionary
                for kode, info in data_buku.items():
                    print(f"Kode: {kode} | Judul: {info['judul']} | Harga: Rp{info['harga']:,}")
        
        # Kondisi 2: Mengelola Daftar Promosi menggunakan Linked List
        elif pilihan == '2':
            # Sub-menu untuk Linked List
            while True:
                print("\n--- MENU PROMOSI ---")
                print("1. Tambah Buku ke Promosi")
                print("2. Lihat Daftar Promosi")
                print("3. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih (1-3): ")                          # Menerima input sub-pilihan dari user

                if sub_pilihan == '1':                                        # Sub-kondisi 2.1: Menambah buku promosi
                    judul_baru = input("Masukkan judul buku untuk promosi: ") # Menerima input judul buku dari user
                    list_promosi.tambah_buku_promosi(judul_baru)              # Menambahkan buku ke linked list promosi
                
                elif sub_pilihan == '2':                                      # Sub-kondisi 2.2: Menampilkan daftar promosi
                    list_promosi.tampilkan_promosi()                          # Memanggil fungsi traversal linked list
                
                elif sub_pilihan == '3':                                      # Sub-kondisi 2.3: Kembali ke menu utama
                    break
                
                else:
                    print("Pilihan tidak valid!")
        
        # Kondisi 3: Mengelola Antirean Kasir menggunakan Queue
        elif pilihan == '3':
            # Sub-menu untuk Queue
            while True:
                print("\n--- MENU ANTIREAN KASIR ---")
                print("1. Tambah Pelanggan ke Antirean")
                print("2. Layani Pelanggan Berikutnya")
                print("3. Lihat Daftar Antirean")
                print("4. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih (1-4): ")                            # Menerima input sub-pilihan dari user
                
                if sub_pilihan == '1':                                          # Sub-kondisi 3.1: Menambah pelanggan ke antirean
                    nama = input("Nama Pelanggan: ")                            # Menerima input nama pelanggan dari user
                    antrean_toko.tambah_antrean(nama)                           # Menambahkan pelanggan ke queue (enqueue)
                
                elif sub_pilihan == '2':                                        # Sub-kondisi 3.2: Melayani pelanggan (mengeluarkan dari queue)
                    antrean_toko.layani_pelanggan()                             # Melayani/menghapus pelanggan dari queue (dequeue)
                
                elif sub_pilihan == '3':                                        # Sub-kondisi 3.3: Menampilkan daftar antirean
                    antrean_toko.tampilkan_antrean()                            # Memanggil method untuk menampilkan status antirean
                
                elif sub_pilihan == '4':                                        # Sub-kondisi 3.4: Kembali ke menu utama
                    break
                
                else:
                    print("Pilihan tidak valid!")
        
        # Kondisi 4: Menampilkan Laporan Penjualan Terurut
        elif pilihan == '4':
            print("\n=== LAPORAN TRANSAKSI PENJUALAN ===")
            print("Harga Sebelum Urut:", riwayat_transaksi)                     # Menampilkan data harga sebelum diurutkan
            hasil_sort = urutkan_transaksi(riwayat_transaksi)                   # Memanggil fungsi sorting untuk mengurutkan harga dari terkecil ke terbesar
            print("Harga Sesudah Urut: ", hasil_sort)                           # Menampilkan data harga setelah diurutkan
        
        # Kondisi 5: Keluar dari program
        elif pilihan == '5':
            print("\nProgram selesai. Terima kasih telah menggunakan sistem manajemen toko buku!")
            # Break untuk keluar dari infinite loop
            break
        
        # Kondisi default: Input tidak valid
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()