# Redimensionador de imagens em lote
from PIL import Image
import os

def batch_resize(folder, width, height):
    for filename in os.listdir(folder):
        if filename.endswith(('.jpeg', '.jpg', '.png')):
            img = Image.open(os.path.join(folder, filename))
            img = img.resize((width, height))
            img.save(os.path.join(folder, f"resized_{filename}"))
            print(f'Resized {filename}')

batch_resize('/path/to/images', 800, 600)