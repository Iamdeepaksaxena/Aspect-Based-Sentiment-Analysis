from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch.nn.functional as F
import warnings

warnings.filterwarnings("ignore")

# Load models once
absa_tokenizer = AutoTokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
absa_model = AutoModelForSequenceClassification.from_pretrained(
    "yangheng/deberta-v3-base-absa-v1.1"
)

sentiment_model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
sentiment_model = pipeline(
    "sentiment-analysis",
    model=sentiment_model_path,
    tokenizer=sentiment_model_path
)


def analyze_aspects(sentence, aspects):
    results = []

    for aspect in aspects:
        inputs = absa_tokenizer(f"[CLS] {sentence} [SEP] {aspect} [SEP]", return_tensors="pt")
        outputs = absa_model(**inputs)

        probs = F.softmax(outputs.logits, dim=1)
        probs = probs.detach().numpy()[0]

        results.append({
            "aspect": aspect,
            "negative": float(probs[0]),
            "neutral": float(probs[1]),
            "positive": float(probs[2])
        })

    return results


def analyze_overall(sentence):
    result = sentiment_model([sentence])[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }