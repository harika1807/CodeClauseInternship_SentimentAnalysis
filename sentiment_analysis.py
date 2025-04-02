from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze sentiment of the given text."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Sentiment score ranges from -1 to 1
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Taking user input
text = input("Enter a sentence or review: ")

# Analyzing sentiment
sentiment = analyze_sentiment(text)

# Displaying result
print(f"Sentiment: {sentiment}")
