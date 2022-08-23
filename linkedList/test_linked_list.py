import pytest

from linked_list import LinkedList
from linked_list import Node


def test_add_in_tail():
    ll = LinkedList()
    a = Node(1)
    b = Node('32')
    c = Node('qwerty')
    d = Node(125)
    e = Node(0.98)

    ll.add_in_tail(a)
    assert ll.head == a
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
    nodes = [a, b, c, d, e]
    for node in nodes:
        ll.add_in_tail(node)

    assert ll.find('32') == b
    assert ll.find('124') is None
    assert ll.find(1) == a
    assert ll.find(125) == d
    assert ll.find(e.value) == e
    assert ll.find('qwerty') == c


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
    assert ll.head.next == d

    ll.delete(0.98)
    assert ll.len() == 3
    assert ll.tail == d
    assert ll.tail.next is None
    # TODO: дописать тесты
