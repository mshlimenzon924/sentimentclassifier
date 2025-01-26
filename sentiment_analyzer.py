# to make program work need to install in venv:
# pip install --upgrade pip
# pip install transformers torch numpy flask
# pip install numpy<2
# rm -rf venv

from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english") # assigning label to given sequence of text

def analyze_sentiment(text):
    result = classifier(text)
    return result[0]


if __name__ == "__main__":
    text = input("Enter text to analyze: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment['label']} with a confidence score: {sentiment['score']:.2f}")