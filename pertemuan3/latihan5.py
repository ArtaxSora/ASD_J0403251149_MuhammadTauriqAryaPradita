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

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # fungsi reverse
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ======================
# Program utama
# ======================

ll = LinkedList()

data_input = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")
data = list(map(int, data_input.split(",")))  # pisahkan dengan koma

for x in data:
    ll.append(x)

print("\nLinked List sebelum dibalik:")
ll.print_list()

ll.reverse()

print("Linked List setelah dibalik:")
ll.print_list()
