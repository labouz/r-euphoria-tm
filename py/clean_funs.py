
# load spacy stopwords and lemmatizer
import spacy
nlp = spacy.load('en_core_web_sm')
sw_spacy = nlp.Defaults.stop_words | {'rt', 'via', '…'}

# remove non=english comments
from langdetect import detect

# add a new column for language
def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'

# function to detect if a pattern is in a string
# for removal of spam comments

spam_patterns = ['[deleted]', 'Thank you for your submission', 'Paypal',
                 'Here is [Rue 21 Coupon Code]', 'JAX\_Jacksonville\_127',
                 'The word detective did not', 'On my way to trinoma/vertis north',
                 'Shipping:', 'Albums', 'Deliver Service',
                 'One-Stop-Shop', 'Strong Deliver', 'Marketing', 'Operations',
                 'Affordable', 'Customer', 'Service', 'Investment', 'Wholesalers',
                 'Shareholders', 'Retailing', 'Retail', 'Markets',
                 '!\~JWPLayer\*', 'Butterburger', 'Tastes Exceptional',
                 'The Committed', 'SIDEX', 'Opinion Poll', 'GoogleDrive', 
                 'Food Ingredients', 'fragrance', 'PayPal', 'Rue Porter',
                 'Fragrances', 'Free shipping', 'PM me with any questions',
                 'View Poll', 'Fangamer','The following description is not provided by this sub']

def clean_spam(text):
    for pattern in spam_patterns:
        if pattern in text:
            return 'spam'
    return 'not spam'

# load libraries
from string import punctuation
import re
import unicodedata

# using regex - clean and remove URLs
def cleaning_URLs(text):
    return re.sub(r"\S*https?:\S*", "",text)

def clean_round1(text):
    # convert all to string
    text = str(text)
    # lower
    text = text.lower()
    # text in squre brackets
    text = re.sub('\[.*?\]', ' ', text)
    # urls
    text = cleaning_URLs(text)
    # punctuation
    text = re.sub('[%s]' % re.escape(punctuation), ' ', text)
    # remove numbers
    text = re.sub('[0-9]+', '', text)
    # it looks like there are edits being made to comments
    # remove any instance of edit:
    text = re.sub('edit:', '', text)
    # remove any user handles
    text = re.sub('@[a-zA-Z0-9_]+', '', text)
    return text

round1 = lambda x: clean_round1(x)

# round two of cleaning: remove line breaks, emojis, qutes, etc.
def clean_round2(text):
    text = re.sub('\n', '', text)
    # text = re.sub('[''""...]', '', text)
    # remove emojis
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return text

round2 = lambda x: clean_round2(x)

# round 3 cleaning: expand contractions: i'd, you've, you're etc
import contractions
def clean_round3(text):
    # expand contractions
    text = contractions.fix(text)
    return text

round3 = lambda x: clean_round3(x)

# another round with lemmatization and stemming
# from nltk.stem import WordNetLemmatizer

# def clean_round3a(text):
#     # stemming
#     # stemmer = PorterStemmer()
#     # text = ' '.join([stemmer.stem(word) for word in text.split()])
#     # lemmatization
#     lemmatizer = WordNetLemmatizer()
#     text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])

#     return text


def clean_round3a(text):
    doc = nlp(text)
    text2 = ' '.join(token.lemma_ for token in doc)

    return text2


round3a = lambda x: clean_round3a(x)

# remove accented characters
def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

do_not_mod_ls = ['good', 'spelling', 'telling', 'addiction','addicts', 'finally', 'all', 'personally', 'struggles', 'really', 'cassie', 'free', 
                 'feeling', 'elliot', 'maddy', 'literally', 'getting', 'better', 'actually', 'totally', 'telling', 'supposed', 'teen',
                 'stuff', 'sorry', 'soon', 'sells', 'sees', 'schools', 'rooms', 'redeeming', 'reddit', 'putting', 'pretty', 'official', 'need',
                 'messages', 'matters', 'looks', 'little', 'kills', 'issues', 'horror', 'hell', 'happens', 'happy', 'gonna', 'getting', 'especially',
                 'different', 'classic', 'businesses', 'attention', 'basically', 'apples', 'weeks', 'streets', 'needles', 'planning', 'full', 'fully',
                 'agreed', 'will', 'been', 'seeds', 'desserts', 'google', 'seen', 'addictions', 'foot', 'funny', 'comments', 'comment', 'poll',
                 'channel', 'well', 'wall', 'hall', 'selling', 'blood', 'beep',
                 'beeping', 'seem', 'seems', 'support', 'maddie', 'still', 'loss']

from operator import contains
def modify(s):
    # split comments into words
    comment = []
    for word in s.split():
        if any(word in x for x in do_not_mod_ls if contains(x, word)):
            comment.append(word)
        else:
            word = re.sub(r'([a-z])\1+', r'\1', word)
            comment.append(word)
    # join the words back together
    comment = ' '.join(comment)
    return comment

# remove repeating characters and non unicode characters
def clean_round4(text):
    # text = remove_accented_chars(text)
    # text = cleaning_repeating_char(text)
    # remove non unicode characters
    text = re.sub('[^\x00-\x7F]+', '', text)
    # remove repeating characters
    text = modify(text)
    text = text.strip()
    return text

round4 = lambda x: clean_round4(x)
