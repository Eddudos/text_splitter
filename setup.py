from setuptools import setup, find_packages

setup(
    name='text_splitter',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=['nltk>=3.8.1', 'spacy>=3.7.4'],
)