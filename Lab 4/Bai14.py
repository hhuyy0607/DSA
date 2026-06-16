class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


def selection_sort(head):
    sorted_head = None
    sorted_tail = None

    while head:
        min_node = head
        min_prev = None

        current = head
        prev = None

        while current.next:
            if current.next.data < min_node.data:
                min_node = current.next
                min_prev = current

            current = current.next

        if min_prev:
            min_prev.next = min_node.next
        else:
            head = head.next

        min_node.next = None

        if sorted_head is None:
            sorted_head = min_node
            sorted_tail = min_node
        else:
            sorted_tail.next = min_node
            sorted_tail = min_node

    return sorted_head


head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

print("Danh sách ban đầu:")
print_list(head)

head = selection_sort(head)

print("Danh sách sau khi sắp xếp:")
print_list(head)