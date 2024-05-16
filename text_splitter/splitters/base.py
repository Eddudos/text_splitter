from typing import List
from abc import ABC, abstractmethod


class BaseSplitter(ABC):
    """
    Базовый класс для стратегий разделения текста
    """

    @abstractmethod
    def split(self, text: str) -> List[str]:
        """
        Разделяет текст на фрагменты

        Args:
            text: Текст для разделения
        Returns:
            Список фрагментов текста
        """
        pass
