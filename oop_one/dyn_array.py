"""
Задание 4

Спроектируйте АТД DynArray на основе концепции (не шаблона) динамического
массива из занятия по алгоритмам и выполните его реализацию.

"""

import abc
from typing import Any


class DynArray(abc.ABC):

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    # команды
    def make_array(self, new_capacity) -> Any:
        """
        постусловие: создан новый массив указанной емкости
        :param new_capacity:
        :return:
        """
        pass

    def resize(self, new_capacity) -> None:
        """
        Предусловие: массив не пуст, длина массива == емкости буфера.
        постусловие: новый массив с увеличенным буфером.
        :param new_capacity:
        :return:
        """
        pass

    def append(self, item) -> None:
        """
        постусловие: длина увеличилась на 1
        :param item:
        :return:
        """
        pass

    def insert(self, pos, item) -> None:
        """
        предусловие: массив не пуст, pos лежит в пределах длины массива
        постусловие: длина массива больше на 1
        :param pos:
        :param item:
        :return:
        """
        pass

    def delete(self, pos) -> None:
        """
        предусловие: массив не пуст, pos лежит в пределах длины массива
        постусловие: длина массива меньше на 1
        :param pos:
        :return:
        """
        pass

    # запросы
    def __len__(self) -> int:
        pass

    def get(self, pos) -> Any:
        """
        предусловие: pos лежит в пределах длины массива
        :param pos:
        :return:
        """
        pass
