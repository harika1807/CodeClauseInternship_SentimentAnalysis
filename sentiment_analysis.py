from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, polarity

while True:
    text = input("\nEnter a sentence (or type 'exit' to stop): ").strip()
    if text.lower() == 'exit':
        print("Exiting Sentiment Analysis...")
        break
    if not text:
        print("Please enter a valid sentence!")
        continue
    
    sentiment, polarity = analyze_sentiment(text)
    print(f"Sentiment: {sentiment} (Polarity Score: {polarity:.2f})")
