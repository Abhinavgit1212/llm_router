from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_request_semantics(request_text):
    labels = ["complex", "general", "simple"]
    result = classifier(request_text, candidate_labels=labels)
    return result["labels"][0]
