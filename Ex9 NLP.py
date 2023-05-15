"""# Ex. 9 Natural Language Processing"""

# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Define a sample text
text = "Natural Language Processing (NLP) is a subfield of artificial intelligence concerned with the interaction between computers and humans in natural language."

# Tokenize the text
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Perform stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

# Perform sentiment analysis
analyzer = SentimentIntensityAnalyzer()
sentiment_score = analyzer.polarity_scores(text)

# Print the results
print("Original text: ", text)
print("Tokenized text: ", tokens)
print("Filtered tokens: ", filtered_tokens)
print("Stemmed tokens: ", stemmed_tokens)
print("Sentiment score: ", sentiment_score)
