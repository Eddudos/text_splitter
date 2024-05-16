from text_splitter import TextSplitter


# Пример текста для разделения
text = """This is a long text that we will split into smaller chunks. It consists of several sentences and should demonstrate various splitting strategies."""

# 1. Разделение по количеству символов
char_splitter = TextSplitter(max_chars=30, split_strategy='char')
char_fragments = char_splitter.split_text(text)
print("Разделение по символам:")
for i, fragment in enumerate(char_fragments):
    print(f"Фрагмент {i+1}: {fragment}")

# 2. Разделение по количеству токенов (NLTK)
nltk_splitter = TextSplitter(max_tokens=4, split_strategy='token', tokenizer='nltk')
nltk_fragments = nltk_splitter.split_text(text)
print("\nРазделение по токенам (NLTK):")
for i, fragment in enumerate(nltk_fragments):
    print(f"Фрагмент {i+1}: {fragment}")

# 3. Разделение по предложениям (SpaCy)
spacy_splitter = TextSplitter(split_strategy='sentence', tokenizer='spacy')
spacy_fragments = spacy_splitter.split_text(text)
print("\nРазделение по предложениям (SpaCy):")
for i, fragment in enumerate(spacy_fragments):
    print(f"Фрагмент {i+1}: {fragment}")