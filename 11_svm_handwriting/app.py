from os import path
from sklearn import cross_validation, svm, metrics
from sklearn.externals import joblib
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/judge")
def api_judge():
    data = request.args.get("data").split(",")
    data = [float(d) / 256 for d in data]
    # print("data.size=", len(data), data)

    # 機械学習の結果を読み込む.
    pklfile = path.join("data-clf", "freq.pkl")
    clf = joblib.load(pklfile)

    # 予測
    print("#### 予測開始")
    predict = clf.predict([data])
    print(predict)

    return str(predict.tolist()[0])

if __name__ == "__main__":
    app.run(debug=True, port=5002)

