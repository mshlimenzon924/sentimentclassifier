## Virtual Environment Setup Guide

- python -m venv venv
- source venv/bin/activate
- pip install --upgrade pip
- pip install transformers torch "numpy<2" flask
- rm -rf venv
- ./run_sentiment_analyzer.sh
- deactivate

- if any issue, encountered can reset venv: rm -rf venv
