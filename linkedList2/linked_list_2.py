from typing import List


class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None
        
        
class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_in_tail(self, node: Node) -> None:
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            
        self.tail = node
        
    def print_all_nodes(self) -> None:
        pass
        
    def find(self, val) -> Node:
        pass
        
    def find_all(self, val) -> List[Node]:
        pass
        
    def clean(self) -> None:
        pass
        
    def len(self) -> int:
        node = self.head
        i = 0
        while node:
            i += 1
            node = node.next
        
        return i
        
    def delete(self, val, all=False) -> None:
        pass
        
    def insert(self, after_node, new_node) -> None:
        """Добавьте в класс LinkedList2 метод вставки узла после заданного узла
        insert(afterNode, newNode) Если afterNode = None и список пустой, 
        добавьте новый элемент первым в списке. Если afterNode = None и список 
        непустой, добавьте новый элемент последним в списке.
        
        """
        pass
        
    def add_in_head(self, node: Node) -> None:
        pass
