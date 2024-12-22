import torch
from pytorch_pretrained_biggan import (BigGAN, one_hot_from_names, truncated_noise_sample)
from PIL import Image
import numpy as np

# Настройка журнала
import logging
logging.basicConfig(level=logging.INFO)

# Загрузка модели
model = BigGAN.from_pretrained('biggan-deep-256')

# Подготовка данных
truncation = 0.4
class_vector = one_hot_from_names(['city'], batch_size=3)
noise_vector = truncated_noise_sample(truncation=truncation, batch_size=3)

# Преобразование в тензоры
noise_vector = torch.from_numpy(noise_vector)
class_vector = torch.from_numpy(class_vector)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
noise_vector = noise_vector.to(device)
class_vector = class_vector.to(device)
model.to(device)

# Генерация изображений
with torch.no_grad():
    output = model(noise_vector, class_vector, truncation)

# Преобразование в numpy массив
output = output.cpu().numpy()

# Преобразуем в диапазон [0, 255] и меняем размерность
output = (output + 1) / 2  # Нормализация в диапазон [0, 1]
output = (output * 255).astype(np.uint8)

# Если это batch, берём первое изображение (output[0])
# Также проверим, что размерность верна: (height, width, channels)
img = Image.fromarray(output[0].transpose(1, 2, 0))  # Преобразуем из (channels, height, width) в (height, width, channels)

# Сохранение изображения
img.save("output_image.png")
print("Изображение сохранено.")
