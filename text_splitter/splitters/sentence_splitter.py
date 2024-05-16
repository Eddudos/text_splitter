from typing import List

from text_splitter.splitters.base import BaseSplitter
from text_splitter.utils.tokenizer import Tokenizer


class SentenceSplitter(BaseSplitter):
    """
    Стратегия разделения текста по предложениям.
    """

    def __init__(self, tokenizer: Tokenizer):
        """
        Инициализация SentenceSplitter.

        Args:
            tokenizer: Токенизатор, используемый для разделения текста на предложения.
        """
        self.tokenizer = tokenizer

    def split(self, text: str) -> List[str]:
        """
        Разделяет текст на фрагменты по предложениям.

        Args:
            text: Текст для разделения.
        Returns:
            Список фрагментов текста.
        """
        return self.tokenizer.sentence_tokenize(text)