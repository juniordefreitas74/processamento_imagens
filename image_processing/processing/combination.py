import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_difference(image1, image2):
    assert image1.shape == image2.shape, "As imagens devem ter o mesmo formato."
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    score, difference_image = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similaridade entre as imagens:", score)
    normalized_difference_image = (difference_image - np.min(difference_image)) / (
        np.max(difference_image) - np.min(difference_image)
    )
    return normalized_difference_image


def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, channel_axis=-_
