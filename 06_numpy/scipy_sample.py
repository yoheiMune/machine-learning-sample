# -*- coding: utf-8 -*-
# Scipy Sample.
# http://cs231n.github.io/python-numpy-tutorial/
# pip install --upgrade Pillow
"""
Note that the Python Imaging Library (PIL) is not a dependency of SciPy and therefore the pilutil module is not available on systems that don’t have PIL installed.

by http://docs.scipy.org/doc/scipy/reference/misc.html

http://pillow.readthedocs.org/en/latest/installation.html#mac-os-x-installation

pip3 uninstall scipy
pip3 install --upgrade scipy

brew install libtiff libjpeg webp little-cms2
pip3 install --upgrade Pillow
"""
import numpy as np
from scipy.misc import imread, imsave, imresize

# Load an image as an nparray.
img = imread('./dog.png')
print(img.dtype, img.shape)

# Resize.
img_resize = imresize(img, (100, 100))
imsave('./dist/dog_resize.png', img_resize)

# Modify.
img_changed = img * [0, 1, 0, 0.5]
imsave('./dist/dog_green.png', img_changed)


### Distance between points
from scipy.spatial.distance import euclidean, cosine
# Euclidean distance
d = euclidean([1,0], [2,5])
print(d)
# Cosine distance
d = cosine([1,1], [1,5])
print(d)


