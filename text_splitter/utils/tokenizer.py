import subprocess
import importlib.util
from abc import ABC, abstractmethod
from typing import List


class Tokenizer(ABC):
    """
    базовый класс для токенизаторов
    """

    @abstractmethod
    def tokenize(self, text: str) -> List[str]:
        """
        Разбивает текст на токены

        Args:
            text: Текст для токенизации
        Returns:
            Список токенов
        """
        pass

    @abstractmethod
    def sentence_tokenize(self, text: str) -> List[str]:
        """
        Разбивает текст на предложения

        Args:
            text: Текст для разделения
        Returns:
            Список предложений
        """
        pass


class NLTKTokenizer(Tokenizer):
    """
    Токенизатор на основе NLTK. Библиотеку NLTK надо установить заранее
    """

    def __init__(self, language: str = "english"):
        """
        Инициализация NLTKTokenizer

        Args:
            language: Язык текста
        """
        if not importlib.util.find_spec("nltk"):
            print("Библиотека NLTK не установлена")

        import nltk

        nltk.download("punkt", quiet=True)
        self.language = language

    def tokenize(self, text: str) -> List[str]:
        """
        Разбивает текст на токены с помощью NLTK
        """
        from nltk.tokenize import word_tokenize

        return word_tokenize(text, language=self.language)

    def sentence_tokenize(self, text: str) -> List[str]:
        """
        Разбивает текст на предложения
        """
        from nltk.tokenize import sent_tokenize

        return sent_tokenize(text, language=self.language)


class SpaCyTokenizer(Tokenizer):
    """
    Токенизатор на основе SpaCy. Библиотеку SpaCy надо установить заранее
    """

    def __init__(self, language: str = "en"):
        """
        Инициализация SpaCyTokenizer

        Args:
            language: Язык текста
        """
        if importlib.util.find_spec("spacy"):
            pass
        else:
            print("Библиотека SpaCy не установлена")

        from spacy.lang.en import English

        if language == "english":
            nlp = English()
            self.nlp = nlp
        else:
            raise ValueError(f"Model '{language}' is not implemented")

    def tokenize(self, text: str) -> List[str]:
        """
        Разбивает текст на токены с помощью SpaCy
        """
        doc = self.nlp(text)
        return [token.text for token in doc]

    def sentence_tokenize(self, text: str) -> List[str]:
        """
        Разбивает текст на предложения
        """
        self.nlp.add_pipe("sentencizer")
        doc = self.nlp(text)
        return [sent.text for sent in doc.sents]
