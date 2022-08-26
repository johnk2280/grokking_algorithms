import pytest

from .linked_list_2 import LinkedList2
from .linked_list_2 import Node


def test_add_in_tail_empty_list():
    ll2 = LinkedList2()
    a = Node(1)
    b = Node('123')
    c = Node('qwerty')
    d = Node(None)
    e = Node(0.98)
    
    ll2.add_in_tail(a)
    assert ll2.len() == 1
    assert ll2.head == a
    assert ll2.head.next is None
    assert ll2.head.prev is None
    assert ll2.tail == a
    assert ll2.tail.next is None
    assert ll2.tail.prev is None    
    
    
def test_add_in_tail_list_of_one_node():
    ll2 = LinkedList2()
    a = Node(1)
    b = Node('123')
    c = Node('qwerty')
    d = Node(None)
    e = Node(0.98)
    
    ll2.add_in_tail(a)
    ll2.add_in_tail(b)
    assert ll2.len() == 2
    assert ll2.head == a
    assert ll2.head.next is b
    assert ll2.head.prev is None
    assert ll2.tail == b
    assert ll2.tail.next is None
    assert ll2.tail.prev is a

    
def test_add_in_tail_list_of_two_nodes():
    ll2 = LinkedList2()
    a = Node(1)
    b = Node('123')
    c = Node('qwerty')
    d = Node(None)
    e = Node(0.98)
    
    ll2.add_in_tail(a)
    ll2.add_in_tail(b)
    ll2.add_in_tail(c)
    assert ll2.len() == 3
    assert ll2.head == a
    assert ll2.head.next is b
    assert ll2.head.next.next is ll2.tail
    assert ll2.head.next.next is c
    assert ll2.head.prev is None
    assert ll2.tail == c
    assert ll2.tail.next is None
    assert ll2.tail.prev is b   
    assert ll2.tail.prev.prev is ll2.head
    assert ll2.tail.prev.prev is a   

    
def test_add_in_tail_list_of_three_nodes():
    ll2 = LinkedList2()
    a = Node(1)
    b = Node('123')
    c = Node('qwerty')
    d = Node(None)
    e = Node(0.98)
    
    ll2.add_in_tail(a)
    ll2.add_in_tail(b)
    ll2.add_in_tail(c)
    ll2.add_in_tail(d)
    assert ll2.len() == 4
    assert ll2.head == a
    assert ll2.head.next is b
    assert ll2.head.next.next is c
    assert ll2.head.next.next.next is ll2.tail
    assert ll2.head.next.next.next is d
    assert ll2.head.prev is None
    assert ll2.tail is d
    assert ll2.tail.next is None
    assert ll2.tail.prev is c   
    assert ll2.tail.prev.prev is b 
    assert ll2.tail.prev.prev.prev is ll2.head
    assert ll2.tail.prev.prev.prev is a 

    
def test_add_in_tail_default():
    pass
    
    
def test_add_in_tail_to_list_with_one_node():
    pass
    

def test_add_in_head_empty_list():
    pass
    
    
def test_add_in_head_not_empty_list():
    pass
    
    
def test_add_in_head_to_list_with_one_node():
    pass
    
    
def test_delete_head():
    pass
    

def test_delete_tail():
    pass    
    
    
def test_delete_one_node_from_empty_list():
    pass
    
    
def test_delete_one_node_from_not_emty_list():
    pass
    

def test_delete_few_nodes_from_not_empty_list():
    pass
    

def test_delete_all_nodes_from_not_empty_list():
    pass

