from skimage.io import imread, imsave


def read_image(path, is_gray=False):
    if is_gray:
        image = imread(path, channel_axis=None)  # Lê como escala de cinza
    else:
        image = imread(path)  # Lê como imagem colorida
    return image


def save_image(image, path):
    imsave(path, image)
