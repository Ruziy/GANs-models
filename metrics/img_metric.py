import cv2
import numpy as np

def calculate_blur_and_detail(image_path):
    """
    Определяет чёткость и качество деталей изображения.

    :param image_path: Путь к изображению.
    :return: Значения дисперсии (чёткости), качество деталей и статус изображения.
    """
    # Загрузка изображения
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Изображение по пути {image_path} не найдено.")

    # Преобразование в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Вычисление Лапласиана для определения чёткости
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Использование волнового преобразования для оценки качества деталей
    coeffs = cv2.dct(np.float32(gray) / 255.0)  # Дискретное косинусное преобразование
    detail_quality = np.mean(np.abs(coeffs))

    # Условие для определения чёткости (порог можно настроить)
    blur_threshold = 1000.0  # Порог для чёткости
    detail_threshold = 0.02  # Порог для качества деталей (подбирается эмпирически)

    blur_status = "Чёткое" if laplacian_var > blur_threshold else "Размытое"
    detail_status = (
        "Высокое качество деталей" if detail_quality > detail_threshold else "Низкое качество деталей"
    )

    return laplacian_var, blur_status, detail_quality, detail_status


if __name__ == "__main__":
    # Пример использования
    image_path = r"metrics\images\2.png".strip()
    try:
        blur_value, blur_status, detail_value, detail_status = calculate_blur_and_detail(image_path)
        print(f"Чёткость изображения: {blur_value:.2f}")
        print(f"Статус изображения: {blur_status}")
        print(f"Качество деталей: {detail_value:.4f}")
        print(f"Статус качества деталей: {detail_status}")
    except Exception as e:
        print(f"Ошибка: {e}")
