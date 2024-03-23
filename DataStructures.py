import sortedcontainers

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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
            print("Попереднього вузла не існує.")
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

'''    def merge_sorted_lists(self, list1, list2):
        dummy_head = Node(0)
        tail = dummy_head
        l1 = list1.head  # Отримуємо голову списку
        l2 = list2.head  # Отримуємо голову списку

        while True:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break

            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next
        
        merged_head = dummy_head.next

        sorted_list = self.merge_sort(merged_head)

        return sorted_list'''

if __name__ == '__main__':

    first_list = LinkedList()

    first_list.insert_at_beginning(5)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(15)
    first_list.insert_at_end(20)
    first_list.insert_at_end(25)
    print("Зв'язний список:")
    first_list.print_list()

    first_list.reverse()
    print("Зв'язний список після реверсування :")
    first_list.print_list()

    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список відсортовано:")
    first_list.print_list()

    second_list = LinkedList()
    first_list.insert_at_beginning(59)
    first_list.insert_at_beginning(20)
    first_list.insert_at_beginning(35)

    first_list.merge_sorted_lists(first_list, second_list)
    print("Зв'язний список відсортовано та замерджено:")
    first_list.print_list()
