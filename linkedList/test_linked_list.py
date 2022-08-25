import pytest

from .linked_list import LinkedList
from .linked_list import Node


def test_add_in_tail():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node('qwerty')
    d = Node(125)
    e = Node(0.98)

    ll.add_in_tail(a)
    assert ll.head == a
    assert ll.head.next is None
    assert ll.tail == a
    assert ll.tail.next is None

    ll.add_in_tail(b)
    assert ll.head == a
    assert ll.tail == b
    assert ll.len() == 2
    assert ll.tail.value == '32'
    assert ll.tail.next is None

    ll.add_in_tail(c)
    assert ll.head == a
    assert ll.tail == c
    assert ll.len() == 3
    assert ll.tail.value == 'qwerty'
    assert ll.tail.next is None

    ll.add_in_tail(d)
    assert ll.head == a
    assert ll.tail == d
    assert ll.len() == 4
    assert ll.tail.value == 125
    assert ll.tail.next is None

    ll.add_in_tail(e)
    assert ll.head == a
    assert ll.tail == e
    assert ll.len() == 5
    assert ll.tail.value == 0.98
    assert ll.tail.next is None


def test_find():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node('qwerty')
    d = Node(125)
    e = Node(0.98)
    for node in [a, b, c, d, e]:
        ll.add_in_tail(node)

    assert ll.find('32') == b
    assert ll.find('124') is None
    assert ll.find(1) == a
    assert ll.find(125) == d
    assert ll.find(e.value) == e
    assert ll.find('qwerty') == c


def test_delete_head():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node('qwerty')
    d = Node(125)
    e = Node(0.98)
    nodes = [a, b, c, d, e]
    for node in nodes:
        ll.add_in_tail(node)

    assert ll.len() == 5

    ll.delete(1)
    assert ll.len() == 4
    assert ll.head == b
    assert a.next is None


def test_delete_tail():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node('qwerty')
    d = Node(125)
    e = Node(0.98)
    nodes = [a, b, c, d, e]
    for node in nodes:
        ll.add_in_tail(node)

    assert ll.len() == 5

    ll.delete(0.98)

    assert ll.len() == 4
    assert ll.tail == d
    assert ll.head == a
    assert ll.head.next.next.next == d


def test_delete_one():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node('qwerty')
    d = Node(125)
    e = Node(0.98)
    nodes = [a, b, c, d, e]
    for node in nodes:
        ll.add_in_tail(node)

    assert ll.len() == 5

    ll.delete('qwerty')
    assert ll.len() == 4
    assert ll.head.next == b
    assert ll.head.next.next == d


def test_delete_alone():
    ll = LinkedList()
    a = Node(1)
    ll.add_in_tail(a)

    assert ll.len() == 1
    assert ll.head == a
    assert ll.tail == a

    ll.delete(1)
    assert ll.len() == 0
    assert ll.head is None
    assert ll.tail is None


def test_delete_some_nodes_with_head():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node(1)
    d = Node(125)
    e = Node(0.98)
    nodes = [a, b, c, d, e]
    for node in nodes:
        ll.add_in_tail(node)

    assert ll.len() == 5

    ll.delete(1, all=True)
    assert ll.len() == 3
    assert ll.head == b
    assert ll.head.next == d
    assert ll.head.next.next == e
    assert ll.tail == e
    assert ll.tail.next is None


def test_delete_some_nodes_with_head_and_tail():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node(1)
    d = Node(125)
    e = Node(1)
    nodes = [a, b, c, d, e]
    for node in nodes:
        ll.add_in_tail(node)

    assert ll.len() == 5

    ll.delete(1, all=True)
    assert ll.len() == 2
    assert ll.head == b
    assert ll.head.next == d
    assert ll.head.next.next is None
    assert ll.tail == d
    assert ll.tail.next is None


def test_delete_all_nodes():
    ll = LinkedList()
    a = Node(1)
    b = Node(1)
    c = Node(1)
    d = Node(1)
    e = Node(1)
    nodes = [a, b, c, d, e]
    for node in nodes:
        ll.add_in_tail(node)

    assert ll.len() == 5

    ll.delete(1, all=True)
    assert ll.len() == 0
    assert ll.head is None
    assert ll.tail is None


def test_insert_to_empty_list():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')

    assert ll.len() == 0

    ll.insert(after_node=a, new_node=b)
    assert ll.head is None
    assert ll.tail is None
    assert ll.len() == 0

    ll.insert(after_node=None, new_node=a)

    assert ll.len() == 1
    assert ll.head == a
    assert ll.tail == a
    assert ll.head.next is None


def test_insert_to_not_empty_list():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node('qwerty')
    d = Node(125)
    e = Node(0.98)

    ll.add_in_tail(a)
    ll.insert(a, b)
    assert ll.head == a
    assert ll.tail == b
    assert ll.len() == 2
    assert ll.head.next == b

    ll.insert(a, c)
    assert ll.head == a
    assert ll.tail == b
    assert ll.len() == 3
    assert ll.head.next == c
