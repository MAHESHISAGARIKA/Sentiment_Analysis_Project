import pickle
import re
import string

# Load trained model
with open("static/model/model.pickle", "rb") as f:
    model = pickle.load(f)

# Load TF-IDF vectorizer
with open("static/model/vectorizer.pickle", "rb") as f:
    vectorizer = pickle.load(f)


def preprocessing(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def get_prediction(text):
    cleaned_text = preprocessing(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]

    if prediction == 1:
        return "negative"
    else:
        return "positive"