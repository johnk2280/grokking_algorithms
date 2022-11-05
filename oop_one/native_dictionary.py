"""
Задание 8

Спроектируйте АТД NativeDictionary на основе концепции (не шаблона) словаря из
занятия по алгоритмам и выполните его реализацию.

В качестве ключа выступает значение строкового типа.
"""
import abc
from typing import Any


class NativeDictionary(abc.ABC):

    def __init__(self, *args, **kwargs):
        """
        Конструктор класса расширен дополнительным массивом для
        хранения значений слотов.
        """
        super().__init__(*args, **kwargs)
        self.slots = [None] * self.size()

    # =========== команды ==========
    @abc.abstractmethod
    def remove(self, key: Any) -> None:
        """
        Предусловие: в массиве slots имеется удаляемый ключ - метод find() вернул True.
        Постусловие: ключ удален из массива slots, значение удалено из массива values
         - remove_status установлен в 1.
        :param key:
        :return:
        """
        pass

    @abc.abstractmethod
    def put(self, key: Any) -> None:
        """
        Предусловие:
        1) в массиве slots имеется значение key - метод find() вернул True.
        2) если в массиве slots отсутствует значение key, то в массивах
        slots и values имеются свободные ячейки - метод find() вернул False.
        Постусловие: элемент вставлен в массив values, в slots вставлен key
        - put_status установлен в 1.
        :param key:
        :return:
        """
        pass

    @abc.abstractmethod
    def get(self, key: Any) -> Any:
        """
        Предусловие: в массиве slots имеется элемент key - метод find() вернул True.
        Постусловие: из массива values удален искомый элемент,
        из массива slots удален key - remove_status установлен в 1.
        :param key:
        :return:
        """
        pass

    @abc.abstractmethod
    def set_find_status(self) -> None:
        """
        Постусловие: установлен код состояния.
        :return:
        """
        pass

    @abc.abstractmethod
    def set_put_status(self) -> None:
        """
        Постусловие: установлен код состояния.
        :return:
        """
        pass

    @abc.abstractmethod
    def set_remove_status(self) -> None:
        """
        Постусловие: установлен код состояния.
        :return:
        """
        pass

    # ==== Запросы ====
    @abc.abstractmethod
    def size(self) -> int:
        """
        :return: количество заполненных слотов в таблице.
        """

    @abc.abstractmethod
    def find(self, value: Any) -> bool:
        """
        Постусловие: возвращено булево значение.
        :param value:
        :return:
        """
        pass

    @abc.abstractmethod
    def get_find_status(self) -> int:
        """
        Постусловие: возвращает код состояния.
        :return:
        """
        pass

    @abc.abstractmethod
    def get_put_status(self) -> int:
        """
        Постусловие: возвращает код состояния.
        :return:
        """
        pass

    @abc.abstractmethod
    def get_remove_status(self) -> int:
        """
        Постусловие: возвращает код состояния.
        :return:
        """
        pass
