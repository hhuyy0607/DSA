class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("null")


def insertion_sort(head):
    sorted_head = None

    while head:
        current = head
        head = head.next

        if sorted_head is None or current.data < sorted_head.data:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head

            while temp.next and temp.next.data < current.data:
                temp = temp.next

            current.next = temp.next
            temp.next = current

    return sorted_head


head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

head = insertion_sort(head)

print_list(head)