class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("The previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def merge_sort(self, head):

        if head is None or head.next is None:
            return head

        mid = self.get_middle(head)
        left_half = head
        right_half = mid.next
        mid.next = None

        left = self.merge_sort(left_half)
        right = self.merge_sort(right_half)

        sorted_list = self.merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow_ptr = head
        fast_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

    def merge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.merge(a.next, b)
        else:
            result = b
            result.next = self.merge(a, b.next)

        return result

    def merge_sorted_lists(self, list1, list2):
        dummy = Node()  # Dummy node to build the merged list
        tail = dummy

        while True:
            # If either list1 or list2 becomes empty, append the remaining nodes of the other list
            if list1 is None:
                tail.next = list2
                break
            elif list2 is None:
                tail.next = list1
                break

            # Compare the data of the nodes and append the smaller one to the merged list
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # Update the head of the merged list
        self.head = dummy.next

if __name__ == '__main__':

    first_list = LinkedList()

    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("First linked list:")
    first_list.print_list()

    first_list.reverse()
    print("Linked list after reversal:")
    first_list.print_list()

    first_list.head = first_list.merge_sort(first_list.head)
    print("Linked list sorted:")
    first_list.print_list()

    second_list = LinkedList()
    second_list.insert_at_beginning(2)
    second_list.insert_at_end(12)
    second_list.insert_at_end(18)
    print("Second linked list:")
    second_list.print_list()

    merged_list = LinkedList()
    merged_list.merge_sorted_lists(first_list.head, second_list.head)
    print("Merged and sorted linked list:")
    merged_list.print_list()
