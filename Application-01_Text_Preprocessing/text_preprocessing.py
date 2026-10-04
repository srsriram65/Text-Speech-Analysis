
import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = input("Enter a sentence: ")

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(
    str.maketrans('', '', string.punctuation)
)

# Tokenization
words = word_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))

filtered_words = []

for word in words:
    if word not in stop_words:
        filtered_words.append(word)

print("\nOriginal Text:")
print(text)

print("\nProcessed Text:")
print(filtered_words)
