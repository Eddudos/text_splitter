## Text Splitter

A simple Python library for splitting text into smaller chunks using different strategies
### Installation

You can install the library using pip:

```bash
pip install -e .
```

### Usage

```python
from text_splitter import TextSplitter

# Example text
text = "This is a long text. We will split it into smaller chunks."

# Split by character count
char_splitter = TextSplitter(max_chars=20, split_strategy='char')
char_fragments = char_splitter.split_text(text)

# Split by token count (using NLTK)
nltk_splitter = TextSplitter(max_tokens=20, split_strategy='token', tokenizer='nltk')
nltk_fragments = nltk_splitter.split_text(text)

# Split by sentences (using SpaCy)
spacy_splitter = TextSplitter(split_strategy='sentence', tokenizer='spacy')
spacy_fragments = spacy_splitter.split_text(text)
```

### Components

* **TextSplitter:** The main class for splitting text. Accepts `max_chars`, `max_tokens`, `split_strategy` and `tokenizer` parameters in the constructor. Provides `split_text(text)` method to split the text using the chosen strategy. 
* **Splitters:** Module containing different splitting strategies.
  - `CharSplitter`: Splits text by character count
  - `TokenSplitter`: Splits text by token count
  - `SentenceSplitter`: Splits text by sentences
* **Utils:** Module containing helper functions
  - `Tokenizer`: Abstract base class for tokenizers 
  - `NLTKTokenizer`: Tokenizer based on NLTK  
  - `SpaCyTokenizer`: Tokenizer based on SpaCy
* **Tests:** Simple test-cases implementation 
### Contributing

Thank me very much. 

### License

[MIT](https://choosealicense.com/licenses/mit/)
