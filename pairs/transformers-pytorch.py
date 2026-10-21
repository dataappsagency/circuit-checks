from transformers import pipeline
def check():
    r = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", framework="pt")("circuit makes this easy")
    assert r and r[0]["label"] in ("POSITIVE", "NEGATIVE"), r
    return f"classified a sentence on PyTorch: {r[0]['label']}"
