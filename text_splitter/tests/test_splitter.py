import unittest

from typing import List
from text_splitter import TextSplitter
from text_splitter.utils.tokenizer import NLTKTokenizer, SpaCyTokenizer, Tokenizer


class TestTextSplitter(unittest.TestCase):
    """
    Тут приведены игрушечные тест кейсы 
    """
    def test_char_splitter(self):
        splitter = TextSplitter(max_chars=10, split_strategy='char')
        text = "This is a test string."
        expected_output = ['This is a ', 'test strin', 'g.']
        self.assertEqual(splitter.split_text(text), expected_output)

    def test_token_splitter_nltk(self):
        splitter = TextSplitter(max_tokens=3, split_strategy='token', tokenizer='nltk')
        text = "This is a test string."
        expected_output = ['This is a', 'test string .']
        self.assertEqual(splitter.split_text(text), expected_output)

    def test_token_splitter_spacy(self):
        splitter = TextSplitter(max_tokens=3, split_strategy='token', tokenizer='spacy')
        text = "This is a test string."
        expected_output = ['This is a', 'test string .']
        self.assertEqual(splitter.split_text(text), expected_output)

    def test_sentence_splitter_nltk(self):
        splitter = TextSplitter(split_strategy='sentence', tokenizer='nltk')
        text = "This is a test. This is another sentence."
        expected_output = ['This is a test.', 'This is another sentence.']
        self.assertEqual(splitter.split_text(text), expected_output)

    def test_sentence_splitter_spacy(self):
        splitter = TextSplitter(split_strategy='sentence', tokenizer='spacy')
        text = "This is a test. This is another sentence."
        expected_output = ['This is a test.', 'This is another sentence.']
        self.assertEqual(splitter.split_text(text), expected_output)

    def test_custom_tokenizer(self):
        class CustomTokenizer(Tokenizer):
            def tokenize(self, text: str) -> List[str]:
                return text.split()

            def sentence_tokenize(self, text: str) -> List[str]:
                return text.split('.')

        splitter = TextSplitter(max_tokens=2, split_strategy='token', tokenizer=CustomTokenizer())
        text = "This is a test string. This is another sentence."
        expected_output = ['This is', 'a test', 'string. This', 'is another', 'sentence.']
        self.assertEqual(splitter.split_text(text), expected_output)


if __name__ == '__main__':
    unittest.main()