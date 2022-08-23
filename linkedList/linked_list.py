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
        # if self.head.value == val:
        #     deleted_node = self.head 
        #     self.head = self.head.next
        #     deleted_node.next = None 

        deleted_nodes = []
        fake_head = Node(None)
        # fake_head.next = self.head
        node = self.head
        prev = fake_head
        while node:
            # TODO: дописать данный метод
            if node.value == val:
                prev.next = node.next
                node.next = None
                if not all:
                    return
            else:
                prev = node

            node = prev.next

    def clean(self):
        """Метод очистки всего содержимого (создание пустого списка)."""
        pass

    def find_all(self):
        """Метод поиска всех узлов по конкретному значению,
            возвращается стандартный питоновский список найденных узлов.
            
        """
        pass

    def len(self):
        """Метод вычисления текущей длины списка."""
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next

        return result

    def insert(self, after_node, new_node):
        """Метод вставки узла newNode после заданного узла after_node. 
            Если afterNode = None, добавьте новый элемент первым в списке."""
        pass
