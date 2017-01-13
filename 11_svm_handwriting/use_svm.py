from os import path
from sklearn import cross_validation, svm, metrics
from sklearn.externals import joblib

if __name__ == "__main__":

    # 機械学習の結果を読み込む.
    print("#### 機械学習結果の開始")
    pklfile = path.join("data-clf", "freq.pkl")
    clf = joblib.load(pklfile)

    traing_data  = path.join("./data_training", "images.csv")
    traing_label = path.join("./data_training", "labels.csv")
    test_data  = path.join("./data_test", "images.csv")
    test_label = path.join("./data_test", "labels.csv")

    # テスト用のデータ
    print("#### データ読み込み開始")
    test_size = 10000
    test = { "labels": [], "images": [] }
    images = open(traing_data, "r").read().split("\n")[:test_size]
    labels = open(traing_label, "r").read().split("\n")[:test_size]
    for label, image in zip(labels, images):
        image = [int(i)/256 for i in image.split(",")]
        test["labels"].append(int(label))
        test["images"].append(image)
    print("\ttest: %d, %d" % (len(test["labels"]), len(test["images"])))

    # 予測
    print("#### 予測開始")
    predict = clf.predict(test["images"])

    # 結果表示
    print("#### 結果だよー")
    ac_score = metrics.accuracy_score(test["labels"], predict)
    cl_report = metrics.classification_report(test["labels"], predict)
    print("正解率 = ", ac_score)
    print(cl_report)

