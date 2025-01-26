from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english") # assigning label to given sequence of text

def analyze_sentiment(text):
    result = classifier(text)
    return result[0]


if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment['label']} with a confidence score: {sentiment['score']:.2f}")