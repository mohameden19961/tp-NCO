from PIL import Image
import numpy as np


def rle_compression(image_array):
    rle = []
    count = 1
    prev = image_array[0]

    for pixel in image_array[1:]:
        if pixel == prev:
            count += 1
        else:
            rle.append((prev, count))
            prev = pixel
            count = 1

    rle.append((prev, count))
    return rle

def gain_compression(original_size, compressed_size):
    return (1 - compressed_size / original_size) * 100

def main():
    image = Image.open("./image.png").convert("L")

    image_array = np.array(image)

    flat_image = image_array.flatten()

    compressed = rle_compression(flat_image)

    original_size = len(flat_image)

    compressed_size = len(compressed) * 2

    gain = gain_compression(original_size, compressed_size)

    print("Taille originale :", original_size)
    print("Taille compressée :", compressed_size)
    print("Gain de compression : {:.2f}%".format(gain))
main()