#latihan 3: fungsi untuk mencari node dengan nilai tertentu
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# ======================
# Program utama
# ======================

dll = DoublyLinkedList()

# input elemen
data_input = input("Masukkan elemen untuk Doubly Linked List (pisahkan dengan koma): ")
data_list = list(map(int, data_input.split(",")))
# menambahkan elemen ke dalam Doubly Linked List
for x in data_list:
    dll.append(x)
# menampilkan isi Doubly Linked List
print("Isi Doubly Linked List:")
dll.print_list()

# input pencarian
cari = int(input("Masukkan elemen yang ingin dicari: "))
# melakukan pencarian dan menampilkan hasil
if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan.")
