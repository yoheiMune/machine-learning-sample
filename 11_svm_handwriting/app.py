from os import path
from sklearn import svm
from sklearn.externals import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/judge")
def api_judge():
    data = request.args.get("data").split(",")
    data = [float(d) / 256 for d in data]

    # Load the training result.
    pklfile = path.join("result", "svm.pkl")
    clf = joblib.load(pklfile)

    # Predict
    predict = clf.predict([data])

    return str(predict.tolist()[0])

if __name__ == "__main__":
    app.run(debug=True, port=5002)

