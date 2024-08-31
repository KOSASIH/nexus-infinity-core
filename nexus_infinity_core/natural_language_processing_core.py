import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy

class NaturalLanguageProcessingCore:
    """
    Natural Language Processing Core for text analysis and understanding.

    Attributes:
    -----------
    text : str
        Input text to analyze.
    """

    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")

    def tokenize_text(self):
        """
        Tokenize the input text into individual words.

        Returns:
        -------
        tokens : list
            List of tokens (words) in the input text.
        """
        tokens = word_tokenize(self.text)
        return tokens

    def analyze_sentiment(self):
        """
        Analyze the sentiment of the input text.

        Returns:
        -------
        sentiment : float
            Sentiment score of the input text (range: -1 to 1).
        """
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(self.text)["compound"]
        return sentiment

    def extract_entities(self):
        """
        Extract entities (e.g., names, locations, organizations) from the input text.

        Returns:
        -------
        entities : list
            List of extracted entities.
        """
        doc = self.nlp(self.text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        return entities

    def perform_named_entity_recognition(self):
        """
        Perform named entity recognition on the input text.

        Returns:
        -------
        ner_results : list
            List of named entity recognition results.
        """
        doc = self.nlp(self.text)
        ner_results = [(entity.text, entity.label_) for entity in doc.ents]
        return ner_results
