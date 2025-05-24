import pandas as pd
import re
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from rake_nltk import Rake
from langdetect import detect
import langdetect


df = pd.read_csv("youtube_comments.csv")


df = df.dropna(subset=["comment"])


df = df.drop_duplicates()


def is_valid_comment(text):
    text = str(text).strip()
    if not text:
        return False
    return bool(re.search(r'[a-zA-Z]', text))  # At least one letter

df = df[df['comment'].apply(is_valid_comment)]


df['comment'] = df['comment'].str.lower().str.strip()


df.to_csv("cleaned_youtube_comments.csv", index=False)
print(f"✅ Cleaned and saved {len(df)} valid comments.")


def get_sentiment(text):
    try:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0.1:
            return "positive"
        elif polarity < -0.1:
            return "negative"
        else:
            return "neutral"
    except:
        return "neutral"


df['sentiment'] = df['comment'].apply(get_sentiment)


df.to_csv("labeled_youtube_comments.csv", index=False)
print(df['sentiment'].value_counts())
print("✅ Sentiment labeling done and saved.")

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Load cleaned comments
df = pd.read_csv('cleaned_youtube_comments.csv')  # Your cleaned file

# Text preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return ' '.join(tokens)

def is_english(text):
    try:
        return detect(text) == 'en'
    except langdetect.lang_detect_exception.LangDetectException:
        return False

# Filter English-only comments
df['is_english'] = df['comment'].apply(is_english)
df = df[df['is_english']]


df['cleaned'] = df['comment'].apply(preprocess)

# Vectorize for LDA
vectorizer = CountVectorizer(max_df=0.95, min_df=2)
dtm = vectorizer.fit_transform(df['cleaned'])

# Fit LDA
n_topics = 5
lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
lda.fit(dtm)

# Show topics
def display_topics(model, feature_names, n_top_words):
    for idx, topic in enumerate(model.components_):
        print(f"Topic {idx + 1}:")
        print(", ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()

display_topics(lda, vectorizer.get_feature_names_out(), 10)

# Keyword extraction using RAKE
r = Rake(stopwords=stop_words)
all_text = ' '.join(df['cleaned'])
r.extract_keywords_from_text(all_text)
print("Top Keywords by RAKE:")
print(r.get_ranked_phrases()[:20])

