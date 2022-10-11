"""
Задание 5

Спроектируйте АТД Queue на основе концепции (не шаблона) очереди из занятия по
алгоритмам и выполните её реализацию.

"""

import abc
from typing import Any


class ParentList(abc.ABC):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = self.head

    def put_right(self, item):
        pass

    def size(self) -> int:
        pass


class GetMixin(abc.ABC):

    def get(self) -> Any:
        pass


class Queue(GetMixin, ParentList):

    def __init__(self):
        super(Queue, self).__init__()

    # ===Команды================
    def put(self, item) -> None:
        """
        Постусловие: размер очереди увеличен на 1
        :param item:
        :return:
        """
        pass

    def get(self) -> Any:
        """
        Предусловие: очередь не пуста.
        Постусловие: размер очереди уменьшен на 1.
        :return:
        """
        pass

    # ===Запросы================
    def size(self) -> int:
        pass
