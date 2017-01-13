from os import path
from sklearn import cross_validation, svm, metrics

# TODO リソース閉じる

if __name__ == "__main__":

    print("#### データ読み込み開始")
    
    traing_data  = path.join("./data_training", "images.csv")
    traing_label = path.join("./data_training", "labels.csv")
    test_data  = path.join("./data_test", "images.csv")
    test_label = path.join("./data_test", "labels.csv")

    # トレーニング用のデータ（5,000件に絞る）
    training_size = 2000
    training = { "labels": [], "images": [] }
    images = open(traing_data, "r").read().split("\n")[:training_size]
    labels = open(traing_label, "r").read().split("\n")[:training_size]
    for label, image in zip(labels, images):
        image = [int(i)/256 for i in image.split(",")]
        training["labels"].append(int(label))
        training["images"].append(image)
    print("\ttraining: %d, %d" % (len(training["labels"]), len(training["images"])))

    # テスト用のデータ（5,000件に絞る）
    test_size = 1000
    test = { "labels": [], "images": [] }
    images = open(traing_data, "r").read().split("\n")[:test_size]
    labels = open(traing_label, "r").read().split("\n")[:test_size]
    for label, image in zip(labels, images):
        image = [int(i)/256 for i in image.split(",")]
        test["labels"].append(int(label))
        test["images"].append(image)
    print("\ttest: %d, %d" % (len(test["labels"]), len(test["images"])))

    # 学習
    print("#### 学習開始")
    clf = svm.SVC()
    clf.fit(training["images"], training["labels"])

    # 予測
    print("#### 予測開始")
    predict = clf.predict(test["images"])

    # 結果表示
    print("#### 結果だよー")
    ac_score = metrics.accuracy_score(test["labels"], predict)
    cl_report = metrics.classification_report(test["labels"], predict)
    print("正解率 = ", ac_score)
    print(cl_report)
