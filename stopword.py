import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "The cat is sitting on the mat"

# Tokenize sentence
tokens = word_tokenize(text)

# Load English stop words
stop_words = set(stopwords.words('english'))

# Remove stop words
filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original:", tokens)
print("Filtered:", filtered_words)