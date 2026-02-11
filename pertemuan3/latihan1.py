# Latihan 1: fungsi	untuk menghapus	node dengan nilai tertentu
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# ================
# Contoh penggunaan
# ================
if __name__ == "__main__":
    llist = LinkedList() 
    # input data
    data_input = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")
    data_list = list(map(int, data_input.split(",")))
    for data in data_list:
        llist.append(data)
    # Menampilkan linked list sebelum penghapusan
    print("Linked List sebelum penghapusan:")
    llist.print_list()
    # Input untuk menghapus nilai tertentu
    key = int(input("Masukkan nilai node yang ingin dihapus: "))
    llist.delete_node(key)
    # Menampilkan linked list setelah penghapusan
    print("Linked List setelah penghapusan:")
    llist.print_list()