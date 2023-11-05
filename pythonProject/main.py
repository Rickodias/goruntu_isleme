import cv2
import numpy as np
import matplotlib.pyplot as plt


def calculate_histogram(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    histogram = np.zeros(256, dtype=int)

    for row in gray_image:
        for pixel in row:
            histogram[pixel] += 1

    return histogram


image = cv2.imread('/Users/rickodias/PycharmProjects/pythonProject/foto.png')


histogram = calculate_histogram(image)

plt.bar(np.arange(256), histogram, width=1.0, color='gray')
plt.title('Gri Seviye Histogram')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()