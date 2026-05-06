from flask import Flask, render_template, request, redirect
from helper import preprocessing, get_prediction
from logger import logging

app = Flask(__name__)

data = dict()
reviews = []
positive = 0
negative = 0


@app.route("/")
def index():
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative

    logging.info("========== Open home page ============")

    return render_template("index.html", data=data)


@app.route("/", methods=["POST"])
def my_post():
    global positive, negative

    text = request.form["text"]
    logging.info(f"Text : {text}")

    preprocessed_txt = preprocessing(text)
    logging.info(f"Preprocessed Text : {preprocessed_txt}")

    prediction = get_prediction(text)
    logging.info(f"Prediction : {prediction}")

    if prediction == "negative":
        negative += 1
    else:
        positive += 1

    reviews.insert(0, text)

    return redirect(request.url)


if __name__ == "__main__":
    app.run(debug=True)