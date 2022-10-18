"""
Задание 6

Спроектируйте АТД Deque на основе концепции (не шаблона) двусторонней очереди
из занятия по алгоритмам и выполните его реализацию.
Совместите АТД и реализации Queue и Deque в одну иерархию по схеме, аналогичной
схеме объединения односвязного и двухсвязного списков.
"""
import abc
from typing import Any


class ParentList(abc.ABC):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = self.head

    def put_right(self, item) -> None:
        pass

    def put_left(self, item) -> None:
        pass

    def clear(self) -> None:
        pass

    def size(self) -> int:
        pass


class LeftItemMixin(abc.ABC):

    def get_left(self) -> Any:
        pass

    def remove_left(self) -> None:
        pass


class RightItemMixin(abc.ABC):

    def get_right(self) -> Any:
        pass

    def remove_right(self) -> None:
        pass


class Queue(LeftItemMixin, RightItemMixin, ParentList):

    def __init__(self):
        """
        Постусловие: создана новая очередь.
        """
        super(Queue, self).__init__()

    # ===Команды================
    def clear(self) -> None:
        """
        Постусловие: очередь пуста (создана новая очередь)
        :return:
        """
        pass

    def put_right(self, item) -> None:
        """
        Постусловие: элемент вставлен в хвост
        :param item:
        :return:
        """
        pass

    def remove_right(self) -> None:
        """
        Предусловие: очередь не пустая.
        Постусловие: элемент удален из хвоста.
        :param item:
        :return:
        """
        pass

    def put_left(self, item) -> None:
        """
        Постусловие: элемент вставлен в голову
        :param item:
        :return:
        """
        pass

    def remove_left(self) -> None:
        """
        Предусловие: очередь не пустая.
        Постусловие: элемент удален из головы.
        :param item:
        :return:
        """
        pass

    def get_left(self) -> Any:
        """
        Предусловие: список не пустой.
        Постусловие: получен элемент из хвоста очереди.
        :return:
        """
        pass

    def get_right(self) -> Any:
        """
        Предусловие: список не пустой.
        Постусловие: получен элемент из головы очереди.
        :return:
        """
        pass

    # ===Запросы================
    def size(self) -> int:
        pass
