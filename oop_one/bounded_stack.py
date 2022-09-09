from typing import Any


class BoundedStack:
    """АТД BoundedStack - это ограниченный стек, конструктор которого получает
    целое положительное значение, задающее максимально допустимое количество
    элементов в стеке. Если параметр не задан, конструктор по умолчанию
    формирует стек максимум на 32 элемента.

    """
    _stack: list = []  # основное хранилище стека
    _peek_status: int = None  # статус запроса peek()
    _pop_status: int = None  # статус команды pop()
    _push_status: int = None  # статус команды push()

    # интерфейс реализующий АТД BoundedStack
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2
    PUSH_NIL = 0
    PUSH_OK = 1
    PUSH_ERR = 2

    def __init__(self, limit=32):
        """Конструктор.

        :param limit: (int): целое положительное значение,
        задающее максимально допустимое количество элементов в стеке
        """
        self.clear()
        self.limit = limit

    def push(self, value: Any) -> None:
        """Метод добавления элемента в стек, если размер стека не превышает
        максимально допустимый лимит.

        :param value: (Any): элемент для добавления в стек.
        :return: None
        """
        if self.size() < self.limit:
            self._stack.append(value)
            self._push_status = self.PUSH_OK
        else:
            self._push_status = self.PUSH_ERR

    def pop(self) -> Any:
        """Метод удаляет верхний элемент стека удаля его.

        :return: (Any): элемент стека, либо `0`, если стек пустой.
        """
        result = 0
        if self.size() > 0:
            result = self._stack.pop(-1)
            self._pop_status = self.POP_OK
        else:
            self._pop_status = self.POP_ERR

        return result

    def clear(self) -> None:
        """Метод очищает стек и устанавливает статусы операций в начальное
        значение.

        :return: (None)
        """
        self._stack = []
        self._peek_status = self.PEEK_NIL
        self._pop_status = self.POP_NIL
        self._push_status = self.PUSH_NIL

    def peek(self) -> Any:
        """Метод возвращает верхний элемент стека.

        :return: (Any): элемент стека, либо `0` если стек пустой.
        """
        result = 0
        self._peek_status = self.PEEK_ERR
        if self.size() > 0:
            result = self._stack[-1]
            self._peek_status = self.PEEK_OK

        return result

    def size(self) -> int:
        """Метод возвращает размер стека.

        :return: (int): размер стека.
        """
        return len(self._stack)

    def get_pop_status(self) -> int:
        """Метод возвращает текущий статус метода pop().

        :return: (int) статус метода pop().
        """
        return self._pop_status

    def get_peek_status(self) -> int:
        """Метод возвращает текущий статус метода peek().

        :return: (int) статус метода peek().
        """
        return self._peek_status

    def get_push_status(self) -> int:
        """Метод возвращает текущий статус метода push().

        :return: (int) статус метода push().
        """
        return self._push_status
