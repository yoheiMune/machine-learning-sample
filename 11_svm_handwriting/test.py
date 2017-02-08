import struct
import gzip

# Read MNIST `label`.
fpath = "./data_mnist/train-labels-idx1-ubyte.gz"
with gzip.open(fpath, "rb") as f:
    magic_number, img_count = struct.unpack(">II", f.read(8))
    labels = []
    for i in range(img_count):
        label = str(struct.unpack("B", f.read(1))[0])
        labels.append(label)

# Write as csv.
outpath = './csv/train-labels.csv'
with open(outpath, "w") as f:
    f.write("\n".join(labels))


# import struct
# import gzip

# # Read MNIST `images`.
# fpath = "./data_mnist/train-images-idx3-ubyte.gz"
# with gzip.open(fpath, "rb") as f:
#     _, img_count = struct.unpack(">II", f.read(8))
#     rows, cols = struct.unpack(">II", f.read(8))
#     images = []
#     for i in range(img_count):
#         binary = f.read(rows * cols)
#         images.append(",".join([str(b) for b in binary]))

# # Write as csv.
# outpath = './csv/train-images.csv'
# with open(outpath, "w") as f:
#     f.write("\n".join(images))

with open("./csv/train-images.csv") as f:
    images = f.read().split("\n")

for i, image in enumerate(images[:10]):
    with open("./image/%d.pgm" % i, "w") as fw:
        s = "P2 28 28 255\n"
        s += " ".join(image.split(","))
        fw.write(s)

# Use SVM.

from sklearn import svm

# Load training data.
with open("./csv/train-images.csv") as f:
    images = f.read().split("\n")[:500]
with open("./csv/train-labels.csv") as f:
    labels = f.read().split("\n")[:500]

# Convert data.
images = [[int(i)/256 for i in image.split(",")] for image in images]
labels = [int(l) for l in labels]

# Use SVM.
clf = svm.SVC()
clf.fit(images, labels)


# Evaluate.
##############################################

from sklearn import metrics

with open("./csv/train-images.csv") as f:
    images = f.read().split("\n")[:500]
with open("./csv/train-labels.csv") as f:
    labels = f.read().split("\n")[:500]

# Convert data.
# test_images = #読み込み処理は省略#
# test_labels = #読み込み処理は省略#
test_images = [[int(i)/256 for i in image.split(",")] for image in images]
test_labels = [int(l) for l in labels]

# Predict.
predict = clf.predict(test_images)

# Result.
ac_score = metrics.accuracy_score(test_labels, predict)
print("Accuracy:", ac_score)
cl_report = metrics.classification_report(test_labels, predict)
print(cl_report)


# Save.
###################################################

# Save the training result.
from sklearn.externals import joblib
joblib.dump(clf, "./result/svm.pkl")






