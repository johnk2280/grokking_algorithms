class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def print_all_nodes(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node:
            if node.value == val:
                return node

            node = node.next

        return None

    def delete(self, val, all=False):
        """Метод удаления одного узла по его значению, где флажок all=False по
        умолчанию - удаляем только первый нашедшийся элемент.
        
        Удаление всех узлов по конкретному значению - флажок all=True.
            
        """
        node = self.head
        prev = Node(None)
        while node:
            next_node = node.next
            if node.value == val:
                node.next = None
                prev.next = next_node
                if node is self.head:
                    self.head = next_node

                if node is self.tail:
                    self.tail = prev if self.head else None

                if not all:
                    return

            prev = node
            node = next_node

        return

    def clean(self):
        """Метод очистки всего содержимого (создание пустого списка).
        
        """
        self.head = None
        self.tail = None

    def find_all(self, val):
        """Метод поиска всех узлов по конкретному значению,
        возвращается стандартный питоновский список найденных узлов.
            
        """
        result = []
        node = self.head
        while node:
            if node.value == val:
                result.append(node)

            node = node.next

        return result

    def len(self):
        """Метод вычисления текущей длины списка.
        
        """
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next

        return result

    def insert(self, after_node, new_node):
        """Метод вставки узла newNode после заданного узла after_node. 
        Если afterNode = None, добавьте новый элемент первым в списке.
            
        """
        if not after_node:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node

        if after_node:
            node = self.head
            while node:
                if node == after_node:
                    new_node.next = node.next
                    node.next = new_node
                    if node == self.tail:
                        self.tail = new_node

                    return

                node = node.next

        return
