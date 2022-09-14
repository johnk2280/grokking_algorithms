"""
Задание 2.

2.1. Опишите АТД LinkedList с предложенным набором операций.
Разделите операции на запросы и команды.
Добавьте, где необходимо предусловия и постусловия.
Добавьте запросы статуса команд, для работы которых требуются предусловия 
(учитывайте в частности случаи, когда список пустой).

2.2. Почему операция tail не сводима к другим операциям (если исходить из 
эффективной реализации)?

2.3. Операция поиска всех узлов с заданным значением, выдающая список таких 
узлов, уже не нужна. Почему?

"""

import abc
from typing import Any


# 2.1
class LinkedList(abc.ABC):

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = self.head
    
    @abc.abstractmethod
    def set_to_head(self) -> None:
        pass
        
    @abc.abstractmethod
    def set_to_tail(self) -> None:
        pass
        
    @abc.abstractmethod
    def move_right(self) -> None:
        pass
        
    @abc.abstractmethod
    def get_current(self) -> Any:
        pass
        
    @abc.abstractmethod
    def put_right(self, value: Any) -> None:
        pass
        
    @abc.abstractmethod
    def put_left(self, value: Any) -> None:
        pass
        
    @abc.abstractmethod
    def remove_current(self) -> None:
        pass
        
    @abc.abstractmethod
    def clear(self) -> None:
        pass
        
    @abc.abstractmethod
    def size(self) -> int:
        pass
        
    @abc.abstractmethod
    def add_in_tail(self, value: Any) -> None:
        pass
        
    @abc.abstractmethod
    def replace_current(self, value: Any) -> None:
        pass
        
    @abc.abstractmethod
    def find(self, value: Any) -> Any:
        pass
        
    @abc.abstractmethod
    def remove_all(self, value: Any) -> None:
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
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
