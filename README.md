# YouTube and Twitter Sentiment Analysis

This project performs sentiment analysis on YouTube comments and Twitter tweets. It consists of three major parts:

1. **Data Collection**: 
   - `data_fetch.py`: Collects comments from a specified YouTube video using the YouTube Data API.
   - `tweet analysis.py`: Scrapes tweets from Twitter using `snscrape`.

2. **Data Cleaning and Sentiment Analysis**:
   - `polarity.py`: Cleans the data, filters English text, performs sentiment analysis using TextBlob, and applies topic modeling using LDA. It also extracts keywords using RAKE.


## Structure

📁 your-repo/
├── src/                       # Python scripts
│   ├── data_fetch.py
│   ├── tweet_analysis.py
│   └── polarity.py
├── data/                      # Output and intermediate data
├── docs/                      # Documentation files (Problem_Statement.docx, etc.)
├── README.md
├── requirements.txt
└── .gitignore


## Outputs:
- `youtube_comments.csv`: Raw YouTube comments.
- `cleaned_youtube_comments.csv`: Cleaned comments after preprocessing.
- `labeled_youtube_comments.csv`: Comments labeled with sentiment (positive, negative, neutral).
- `straykids_tweets.csv`: Scraped tweets related to Stray Kids.

## Requirements:
See `requirements.txt` for the list of necessary packages.

## Notes:
- Ensure you have a valid YouTube Data API key before running `data_fetch.py`.
- Twitter scraping is done using the `snscrape` module, which doesn't require Twitter API credentials.

