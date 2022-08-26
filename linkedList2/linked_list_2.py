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
        
    def print_all_nodes(self, reverse=False) -> None:
        node = self.head if not reverse else self.tail
        while node:
            print(node.value)
            node = node.next if not reverse else node.prev
  
        
    def find(self, val, reverse=False) -> Node:
        node = self.head if not reverse else self.tail
        while node:
            if node.value == val:
                return node
            
            node = node.next if not reverse else node.prev
        
    def find_all(self, val, reverse=False) -> List[Node]:
        node = self.head if not reverse else self.tail
        result = []
        while node:
            if node.value == val:
                result.append(node)
            
            node = node.next if not reverse else node.prev
        
        return node
        
    def clean(self) -> None:
        self.head = None
        self.tail = None
        
    def len(self) -> int:
        node = self.head
        i = 0
        while node:
            i += 1
            node = node.next
        
        return i
        
    def delete(self, val, all=False) -> None:   
        #if self.head:
         #   fake_head = Node(None)
          #  self.head.prev = fake_head
            
        node = self.head
        # TODO: проходят не все тесты   
        while node:
            if node.value == val:
                if node.prev is None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                    
                node.next.prev = node.prev
                if node is self.head:
                    self.head = node.next
                    
                if not all:
                    return
            
            node = node.next

                
        
    def insert(self, after_node, new_node) -> None:
        """Добавьте в класс LinkedList2 метод вставки узла после заданного узла
        insert(afterNode, newNode) Если afterNode = None и список пустой, 
        добавьте новый элемент первым в списке. Если afterNode = None и список 
        непустой, добавьте новый элемент последним в списке.
        
        """
        pass
        
    def add_in_head(self, node: Node) -> None:
        if self.head:
            node.next = self.head
            self.head.prev = node
        else:
            self.tail = node
        
        self.head = node
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
