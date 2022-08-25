"""Найдите центральный элемент списка за один проход?"""

from linkedList.linked_list import LinkedList
from linkedList.linked_list import Node

a = Node(1)
b = Node(3)
c = Node(19)
d = Node(15)
e = Node(8)
f = Node(11)

ll = LinkedList()
for node in [a, b, c, d, e, f]:
    ll.add_in_tail(node)


def get_central_element(lst: LinkedList) -> Node:
    fast = lst.head
    slow = lst.head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow


if __name__ == '__main__':
    print(get_central_element(ll) == d)
