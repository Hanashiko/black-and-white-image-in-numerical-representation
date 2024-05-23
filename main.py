from PIL import Image
import numpy as np

image = Image.open('digit.png').convert('L') 

print("Розмір зображення:", image.size)  # Очікується (28, 28)

pixel_array = np.array(image)

print("Форма масиву пікселів:", pixel_array.shape)  # Очікується (28, 28)

pixel_vector = pixel_array.flatten()

print("Довжина розгорнутого масиву:", len(pixel_vector))  # Очікується 784

np.set_printoptions(threshold=np.inf)

print(", ".join(map(str, pixel_vector.tolist())))
