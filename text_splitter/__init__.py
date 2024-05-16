from typing import List, Optional, Union

from text_splitter.splitters import (
    BaseSplitter,
    CharSplitter,
    TokenSplitter,
    SentenceSplitter,
)
from text_splitter.utils.tokenizer import Tokenizer, NLTKTokenizer, SpaCyTokenizer


class TextSplitter:
    """
    Разделяет текст на фрагменты, используя различные стратегии
    """

    def __init__(
        self,
        max_chars: Optional[int] = None,
        max_tokens: Optional[int] = None,
        split_strategy: str = None,
        tokenizer: Union[str, Tokenizer] = None,
        language: str = "english",
    ):
        """
        Инициализация объекта TextSplitter

        Args:
            max_chars: Максимальное количество символов в одном фрагменте
            max_tokens: Максимальное количество токенов в одном фрагменте
            split_strategy: Выбранная стратегия разделения:
                - 'char': Разделение по количеству символов
                - 'token': Разделение по количеству токенов
                - 'sentence': Разделение по предложениям
            tokenizer: Используемый токенизатор:
                - 'nltk': Токенизатор NLTK
                - 'spacy': Токенизатор SpaCy
                - Объект класса, реализующего интерфейс Tokenizer
            language: Язык текста (используется только для токенизации)
        """
        if (
            max_chars is None
            and max_tokens is None
            and split_strategy is not "sentence"
        ):
            raise ValueError(
                "Set one of the parameters: max_chars \
                              or max_tokens or split_strategy=sentence"
            )

        if tokenizer:
            self.tokenizer: Tokenizer = self._get_tokenizer(tokenizer, language)

        self.max_chars = max_chars
        self.max_tokens = max_tokens
        self.splitter: BaseSplitter = self._get_splitter(split_strategy)

    def split_text(self, text: str) -> List[str]:
        """
        Разделяет текст на фрагменты
        Args:
            text: Текст для разделения
        Returns:
            Список фрагментов текста
        """
        return self.splitter.split(text)

    def _get_splitter(self, split_strategy: str) -> BaseSplitter:
        """
        Возвращает объект стратегии разделения, соответствующий выбранной стратегии
        """
        if split_strategy == "char":
            return CharSplitter(self.max_chars)
        elif split_strategy == "token":
            return TokenSplitter(self.max_tokens, self.tokenizer)
        elif split_strategy == "sentence":
            return SentenceSplitter(self.tokenizer)
        else:
            raise ValueError(f"Неизвестная стратегия разделения: {split_strategy}")

    def _get_tokenizer(
        self, tokenizer: Union[str, Tokenizer], language: str
    ) -> Tokenizer:
        """
        Возвращает объект токенизатора, соответствующий выбранному типу
        """
        if isinstance(tokenizer, str):
            if tokenizer == "nltk":
                return NLTKTokenizer(language)
            elif tokenizer == "spacy":
                return SpaCyTokenizer(language)
            else:
                raise ValueError(f"Неизвестный тип токенизатора: {tokenizer}")
        elif isinstance(tokenizer, Tokenizer):
            return tokenizer
        else:
            raise TypeError(f"Неверный тип токенизатора: {type(tokenizer)}")
