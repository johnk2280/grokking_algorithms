"""
Задание 9
Спроектируйте АТД PowerSet на основе концепции (не шаблона) множества из
занятия по алгоритмам и выполните его реализацию.

Представьте АТД PowerSet как наследника АТД HashTable -- с ограничением на
максимальное количество элементов в множестве.
"""
from typing import Any, TypeVar, Generic

from oop_one.hash_table import AbstractHashTable

S = TypeVar('S')


class PowerSet(AbstractHashTable, Generic[S]):

    def __init__(self):
        super().__init__()
        self.slots = []

    # ==== Команды ====
    def put(self, value: Any) -> None:
        """
       Предусловие: в таблице имеется свободный слот и метод find() вернул False.
       Постусловие: элемент вставлен в таблицу - put_status установлен в 1.
       :param value:
       :return:
       """
        pass

    def get(self, value: Any) -> Any:
        """
        Предусловие: в таблице имеется искомый элемент - метод find() вернул True.
        Постусловие: из таблицы удален искомый элемент - remove_status установлен в 1.
        :param value:
        :return:
        """
        pass

    def remove(self, value: Any) -> None:
        """
        Предусловие: в таблице имеется удаляемый элемент - метод find() вернул True.
        Постусловие: элемент удален - remove_status установлен в 1.
        :param value:
        :return:
        """
        pass

    def intersection(self, set2: S) -> S:
        """
        Постусловие: возвращено новое множество, содержащее в себе только те
        элементы, которые содержаться в обоих исходных множествах.
        :param set2:
        :return:
        """
        pass

    def union(self, set2: S) -> S:
        """
        Постусловие: возвращено новое множество, содержащее в себе все элементы
        из исходных множеств.
        :param set2:
        :return:
        """
        pass

    def difference(self, set2: S) -> S:
        """
        Постусловие: возвращено подмножество текущего множества содержащее
        элементы, которые не входят во множество-параметр.
        :param set2:
        :return:
        """
        pass

    def set_find_status(self) -> None:
        """
        Постусловие: установлен код состояния.
        :return:
        """
        pass

    def set_put_status(self) -> None:
        """
        Постусловие: установлен код состояния.
        :return:
        """
        pass

    def set_remove_status(self) -> None:
        """
        Постусловие: установлен код состояния.
        :return:
        """
        pass

    # ==== Запросы ====

    def issubset(self, set2: S) -> bool:
        """
        Постусловие: возвращено булево значение.
        :param set2:
        :return:
        """
        pass

    def size(self) -> int:
        """
        :return: количество элементов в таблице.
        """
        pass

    def find(self, value: Any) -> bool:
        """
        Постусловие: возвращено булево значение.
        :param value:
        :return:
        """
        pass

    def get_find_status(self) -> int:
        """
        Постусловие: возвращает код состояния.
        :return:
        """
        pass

    def get_put_status(self) -> int:
        """
        Постусловие: возвращает код состояния.
        :return:
        """
        pass

    def get_remove_status(self) -> int:
        """
        Постусловие: возвращает код состояния.
        :return:
        """
        pass
