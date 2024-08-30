import re
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def remove_stopwords(text, stopwords):
    tokens = text.split()
    tokens = [token for token in tokens if token not in stopwords]
    return " ".join(tokens)

def stem_words(text):
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    tokens = text.split()
    tokens = [stemmer.stem(token) for token in tokens]
    return " ".join(tokens)

def lemmatize_words(text):
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)

def extract_entities(text):
    from nltk import ne_chunk
    tokens = text.split()
    entities = ne_chunk(tokens)
    return [(entity.label(), " ".join(entity.leaves())) for entity in entities]

def calculate_string_similarity(str1, str2):
    from difflib import SequenceMatcher
    return SequenceMatcher(None, str1, str2).ratio()

# Example usage:
text = "Hello, world! This is a sample text."
text = remove_punctuation(text)
print("Text without punctuation:", text)

stopwords = ["is", "a", "the"]
text = remove_stopwords(text, stopwords)
print("Text without stopwords:", text)

text = stem_words(text)
print("Text with stemmed words:", text)

text = lemmatize_words(text)
print("Text with lemmatized words:", text)

entities = extract_entities(text)
print("Extracted entities:", entities)

str1 = "This is a sample text."
str2 = "This is another sample text."
similarity = calculate_string_similarity(str1, str2)
print("String similarity:", similarity)
