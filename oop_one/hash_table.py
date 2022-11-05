"""
Задание 7

Спроектируйте АТД HashTable на основе концепции (не шаблона) хэш-таблицы из
занятия по алгоритмам и выполните его реализацию.

В данном задании мы отказываемся от индексации и используем хэш-таблицу
исключительно как хранилище неупорядоченных значений с возможностью их
добавления и удаления и с быстрой проверкой за O(1), принадлежит ли некоторое
значение этой таблице.

Учитывайте, что попытка добавления нового элемента в хэш-таблицу может
закончиться неудачей (например, из-за ограничений механизма разрешения коллизий).

Сделайте единственный параметром конструктора максимальный размер хэш-таблицы.
Более универсальный способ, конечно, обойтись без такого ограничения: расширить
хэш-таблицу возможностями динамического массива, чтобы при её полном заполнении
внутренний буфер автоматически увеличивался.
"""
import abc
from typing import Optional, Any


class AbstractHashTable(abc.ABC):
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    FIND_NIL = 0
    FIND_OK = 1
    FIND_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    # ==== Команды ====
    @abc.abstractmethod
    def remove(self, value: Any) -> None:
        """
        Предусловие: в таблице имеется удаляемый элемент - метод find() вернул True.
        Постусловие: элемент удален - remove_status установлен в 1.
        :param value:
        :return:
        """
        pass

    @abc.abstractmethod
    def put(self, value: Any) -> None:
        """
        Предусловие: в таблице имеется свободный слот и метод find() вернул False.
        Постусловие: элемент вставлен в таблицу - put_status установлен в 1.
        :param value:
        :return:
        """
        pass

    @abc.abstractmethod
    def get(self, value: Any) -> Any:
        """
        Предусловие: в таблице имеется искомый элемент - метод find() вернул True.
        Постусловие: из таблицы удален искомый элемент - remove_status установлен в 1.
        :param value:
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
        :return: количество элементов в таблице.
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
