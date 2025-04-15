import matplotlib.pyplot as plt
import numpy as np


def plot_image(image):
    plt.figure(figsize=(12, 4))
    cmap = "gray" if image.ndim == 2 else None
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    plt.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(
        nrows=1, ncols=number_images, figsize=(4 * number_images, 4)
    )
    if number_images == 1:
        axis = [axis]  # Garantir que seja iterável
    names_lst = ["Image {}".format(i) for i in range(1, number_images)]
    names_lst.append("Result")
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)
        cmap = "gray" if image.ndim == 2 else None
        ax.imshow(image, cmap=cmap)
        ax.axis("off")
    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("A imagem deve ser RGB com 3 canais para o histograma.")

    fig, axis = plt.subplots(
        nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True
    )
    color_lst = ["red", "green", "blue"]
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title("{} Histogram".format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
    fig.tight_layout()
    plt.show()
