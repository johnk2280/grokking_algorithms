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

    def put_right(self, item):
        pass

    def size(self) -> int:
        pass


class GetMixin(abc.ABC):

    def get(self) -> Any:
        pass


class PutLeftMixin(abc.ABC):
    def put_left(self, item) -> None:
        pass
