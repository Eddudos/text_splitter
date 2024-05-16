from typing import List

from text_splitter.splitters.base import BaseSplitter
from text_splitter.utils.tokenizer import Tokenizer


class TokenSplitter(BaseSplitter):
    """
    Стратегия разделения текста по максимальному количеству токенов
    """

    def __init__(self, max_tokens: int, tokenizer: Tokenizer):
        """
        Инициализация TokenSplitter

        Args:
            max_tokens: Максимальное количество токенов в одном фрагменте
            tokenizer: Токенизатор, используемый для разделения текста на токены
        """
        self.max_tokens = max_tokens
        self.tokenizer = tokenizer

    def split(self, text: str) -> List[str]:
        """
        Разделяет текст на фрагменты по максимальному количеству токенов

        Args:
            text: Текст для разделения
        Returns:
            Список фрагментов текста
        """
        if self.max_tokens <= 0:
            raise ValueError("max_tokens должно быть положительным числом.")

        tokens = self.tokenizer.tokenize(text)
        fragments = []
        current_fragment = []
        current_token_count = 0

        for token in tokens:
            current_fragment.append(token)
            current_token_count += 1

            if current_token_count == self.max_tokens:
                fragments.append(" ".join(current_fragment))
                current_fragment = []
                current_token_count = 0

        if current_fragment:
            fragments.append(" ".join(current_fragment))

        return fragments
