from typing import List

from text_splitter.splitters.base import BaseSplitter


class CharSplitter(BaseSplitter):
    """
    Стратегия разделения текста по максимальному количеству символов
    """

    def __init__(self, max_chars: int):
        """
        Инициализация CharSplitter

        Args:
            max_chars: Максимальное количество символов в одном фрагменте
        """
        if max_chars <= 0:
            raise ValueError("max_chars должно быть положительным числом.")
        self.max_chars = max_chars

    def split(self, text: str) -> List[str]:
        """
        Разделяет текст на фрагменты по максимальному количеству символов

        Args:
            text: Текст для разделения
        Returns:
            Список фрагментов текста
        """
        return [
            text[i : i + self.max_chars] for i in range(0, len(text), self.max_chars)
        ]
