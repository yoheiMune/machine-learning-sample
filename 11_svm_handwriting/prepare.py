#
# Conver MNIST data to csv files.
#
import sys
import os
from os import path
import gzip
import struct

# TODO リファクタリングするー

"""
    ・ファイルを解凍してcsvを作成（データ、ラベルそれぞれ）（→data1フォルダ）
    ・画像サンプルを出力（→data_img_sampleフォルダ）
    ・5,000件でトレーニングとテスト
"""

def to_csv(type_, label_path, data_path):
    """MNIST形式からCSV出力を行います"""

    # ラベルデータをCSVに出力します（1行で1枚の画像中）
    data_f = gzip.open(label_path, "rb")
    magic_number, img_count = struct.unpack(">II", data_f.read(8))
    labels = []
    for i in range(img_count):
        label = str(struct.unpack("B", data_f.read(1))[0])
        labels.append(label)
    # 書き出し
    dirname_out = "./data_" + type_
    training_label_csv = path.join(dirname_out, "labels.csv")
    with open(training_label_csv, "w") as f:
        f.write("\n".join(labels))
    
    # トレーニングデータをCSVに出力します（1ピクセルで1データ、1行で1枚の画像）
    data_f = gzip.open(data_path, "rb")
    # ラベル読み込み, 画像数
    magic_number, img_count = struct.unpack(">II", data_f.read(8))
    # 画像1枚あたりの縦幅と横幅
    rows, cols = struct.unpack(">II", data_f.read(8))
    pixels = rows * cols
    # 画像読み込み
    images = []
    for i in range(img_count):
        binary = data_f.read(pixels)
        images.append(",".join([str(b) for b in binary]))
    # 書き出し
    dirname_out = "./data_" + type_
    training_data_csv = path.join(dirname_out, "images.csv")
    with open(training_data_csv, "w") as f:
        f.write("\n".join(images))

    # サンプル書き出し
    # TODO できればpng出力にしたいなー
    if type_ == "training":
        # 10個だけ画像として書きだし
        for i, image in enumerate(images[:10]):
            s = "P2 28 28 255\n"
            s += " ".join(image.split(","))
            p = path.join("data_image_sample", str(i) + ".pgm")
            print(p)
            with open(p, "w", encoding="utf-8") as f:
                f.write(s)

    # TODO 
    # リソースのクローズ.


if __name__ == "__main__":

    dirname = "./data_mnist"
    training_data  = path.join(dirname, "train-images-idx3-ubyte.gz")
    training_label = path.join(dirname, "train-labels-idx1-ubyte.gz")
    test_data  = path.join(dirname, "t10k-images-idx3-ubyte.gz")
    test_label = path.join(dirname, "t10k-labels-idx1-ubyte.gz")

    to_csv("training", training_label, training_data)
    to_csv("test", test_label, test_data)
