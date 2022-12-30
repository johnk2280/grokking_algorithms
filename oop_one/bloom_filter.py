"""
Задание 10

Спроектируйте АТД BloomFilter на основе концепции (не шаблона) фильтра Блюма из
занятия по алгоритмам и выполните его реализацию.
"""

from abc import ABC, abstractmethod


class ABloomFilter(ABC):

    # ==== Команды ====
    @abstractmethod
    def add(self, str1: str):
        """
        Постусловие: строка добавлена в фильтр, актуализирована битовая маска
        :param str1:
        :return:
        """

    # ==== Запросы ====

    @abstractmethod
    def is_value(self, str1) -> bool:
        """
        Предусловие: имеется строка в фильтре.
        :param str1:
        :return:
        """