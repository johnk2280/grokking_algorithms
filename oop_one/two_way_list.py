"""
Задание 3.
Объедините АТД LinkedList и TwoWayList в иерархию, как только что было
предложено, и дополните реализацией.

"""

import abc
from typing import Any


class ParentList(abc.ABC):

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = self.head

    # ====Команды======
    @abc.abstractmethod
    def set_to_head(self) -> None:
        """
        Предусловие: список не пустой.
        Постусловие: курсор установлен на первый узел в списке.
        :return: None
        """
        pass

    @abc.abstractmethod
    def set_to_tail(self) -> None:
        """
        Предусловие: список не пустой.
        Постусловие: курсор установлен на последний узел в списке.
        :return: None
        """
        pass

    @abc.abstractmethod
    def move_current_to_right(self) -> None:
        """
        Предусловие: список не пустой и курсор находится не на последнем узле.
        Постусловие: курсор сдвинут на следующий справа узел.
        :return: None
        """
        pass

    @abc.abstractmethod
    def put_right(self, value: Any) -> None:
        """
        Предусловие: список не пустой.
        Постусловие: узел с указанным значением вставлен следом за текущим.
        :param value: Any
        :return: None
        """
        pass

    @abc.abstractmethod
    def put_left(self, value: Any) -> None:
        """
        Предусловие: список не пустой.
        Постусловие: узел с указанным значением вставлен перед текущим.
        :param value: Any
        :return: None
        """
        pass

    @abc.abstractmethod
    def remove_current(self) -> None:
        """
        Предусловие: список не пустой.
        Постусловие: текущий узел удален.
        :return: None
        """
        pass

    @abc.abstractmethod
    def clear(self) -> None:
        """
        Постусловие: список пуст.
        :return: None
        """
        pass

    @abc.abstractmethod
    def add_in_tail(self, value: Any) -> None:
        """
        Постусловие: узел с указанным значением добавлен в хвост списка, если
                    список не пустой.
                    Либо добавлен в голову и в хвост, если список был пустым
                    перед вызовом метода.
        :param value: Any
        :return: None
        """
        pass

    @abc.abstractmethod
    def replace_current(self, value: Any) -> None:
        """
        Предусловие: список не пустой.
        Постусловие: значение текущего узла равно указанному значению.
        :param value: Any
        :return: None
        """
        pass

    @abc.abstractmethod
    def remove_all(self, value: Any) -> None:
        """
        Постусловие: из списка удалены все узлы с указанным значением.
        :param value: Any
        :return: None
        """
        pass

    # ====Запросы======
    @abc.abstractmethod
    def get_current(self) -> Any:
        pass

    @abc.abstractmethod
    def size(self) -> int:
        pass

    @abc.abstractmethod
    def find(self, value: Any) -> Any:
        pass

    @abc.abstractmethod
    def is_head(self) -> bool:
        pass

    @abc.abstractmethod
    def is_tail(self) -> bool:
        pass

    @abc.abstractmethod
    def is_value(self) -> bool:
        pass


class LinkedList(ParentList):
    def __init__(self):
        super(LinkedList, self).__init__()

    def set_to_head(self) -> None:
        pass

    def set_to_tail(self) -> None:
        pass

    def move_current_to_right(self) -> None:
        pass

    def put_right(self, value: Any) -> None:
        pass

    def put_left(self, value: Any) -> None:
        pass

    def remove_current(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def add_in_tail(self, value: Any) -> None:
        pass

    def replace_current(self, value: Any) -> None:
        pass

    def remove_all(self, value: Any) -> None:
        pass

    def get_current(self) -> Any:
        pass

    def size(self) -> int:
        pass

    def find(self, value: Any) -> Any:
        pass

    def is_head(self) -> bool:
        pass

    def is_tail(self) -> bool:
        pass

    def is_value(self) -> bool:
        pass


class LeftShiftMixin:
    """
    Класс миксин для расширения классов наследованных от класса ParentList
    методом смещения курсора влево - move_current_to_left().
    """
    def move_current_to_left(self) -> None:
        """
        Предусловие: список не пустой и курсор находится не на первом узле.
        Постусловие: курсор сдвинут на следующий слева узел.
        :return:
        """
        pass


class TwoWayList(LeftShiftMixin, ParentList):
    def __init__(self):
        super(TwoWayList, self).__init__()

    def set_to_head(self) -> None:
        pass

    def set_to_tail(self) -> None:
        pass

    def move_current_to_right(self) -> None:
        pass

    def move_current_to_left(self) -> None:
        """
        Добавленный метод из миксина LeftShiftMixin.
        :return:
        """
        pass

    def put_right(self, value: Any) -> None:
        pass

    def put_left(self, value: Any) -> None:
        pass

    def remove_current(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def add_in_tail(self, value: Any) -> None:
        pass

    def replace_current(self, value: Any) -> None:
        pass

    def remove_all(self, value: Any) -> None:
        pass

    def get_current(self) -> Any:
        pass

    def size(self) -> int:
        pass

    def find(self, value: Any) -> Any:
        pass

    def is_head(self) -> bool:
        pass

    def is_tail(self) -> bool:
        pass

    def is_value(self) -> bool:
        pass
