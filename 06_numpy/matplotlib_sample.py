# -*- coding: utf-8 -*-
# A sample of Matplotlib, especially for matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# Sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
# plt.plot(x,y)
# plt.show()

# Multiple lines, a title, legend and axis labels.
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# plt.plot(x, y_sin)
# plt.plot(x, y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine and Cosine')
# plt.legend(['Sine', 'Cosine'])
# plt.show()


## Subplots.
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# Setup a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
# plt.subplot(2, 1, 1)
# # Make the first plot.
# plt.plot(x, y_sin)
# plt.title('Sine')
# # Set the second subplot as active, and make the second plot.
# plt.subplot(2, 1, 2)
# plt.plot(x, y_cos)
# plt.title('Cosine')
# # Show
# plt.show()


## Image.
from scipy.misc import imread
img = imread('dog.png')
img_tinted = img * [1, 0.2, 0.2, 1]
# Show the original image.
plt.subplot(1, 2, 1)
plt.imshow(img)
# Show the tinted image.
plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))
# Show
plt.show()























































