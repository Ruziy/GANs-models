import torch
import clip
from PIL import Image
import numpy as np
from scipy.spatial.distance import cosine

# Функция для вычисления CLIP Score
def compute_clip_score(image_path, prompt):
    # Загружаем модель CLIP
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device)

    # Загружаем и подготавливаем изображение
    image = Image.open(image_path)
    image_input = preprocess(image).unsqueeze(0).to(device)

    # Подготавливаем текстовый prompt
    text_input = clip.tokenize([prompt]).to(device)

    # Вычисляем фичи изображения и текста
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_input)

    # Нормализуем фичи
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)

    # Вычисляем косинусное расстояние
    similarity = (image_features @ text_features.T).item()

    return similarity

# Пример использования
image_path = [r"metrics\images\abandoned_amusement_park_image.png"]  # Путь к сгенерированному изображению
prompt = "An abandoned amusement park where nature has taken over, and trees wrap around carousels, and flowers grow on roller coasters. The park features old rides covered in moss and vines, as well as deserted kiosks with faded signs. At the center of the park, there is a large lake covered in lilies, where swans and ducks swim."   # Твой prompt

for el in image_path:
    clip_score = compute_clip_score(el, prompt)
    print(f"CLIP Score: {clip_score}")
