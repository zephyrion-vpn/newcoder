import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def decode_qr(image_path: str) -> Optional[list[str]]:
    try:
        from pyzbar.pyzbar import decode  # type: ignore
        from PIL import Image  # type: ignore
    except ImportError:
        logger.warning("Библиотеки pyzbar/Pillow не установлены, пробую cv2...")
        return _decode_with_cv2(image_path)
    try:
        results = decode(Image.open(image_path))
    except FileNotFoundError:
        logger.error("Файл не найден: %s", image_path)
        return None
    return [item.data.decode("utf-8", errors="replace") for item in results]


def _decode_with_cv2(image_path: str) -> Optional[list[str]]:
    try:
        import cv2  # type: ignore
    except ImportError:
        logger.error("Ни pyzbar, ни cv2 не установлены. Установите: pip install pyzbar pillow или opencv-python")
        return None
    image = cv2.imread(image_path)
    if image is None:
        logger.error("Не удалось открыть изображение: %s", image_path)
        return None
    detector = cv2.QRCodeDetector()
    text, _, _ = detector.detectAndDecode(image)
    return [text] if text else []


def main() -> None:
    results = decode_qr("sample_qr.png")
    if results is None:
        print("Декодирование недоступно (нет библиотек или файла).")
    elif not results:
        print("QR-код не найден на изображении.")
    else:
        for text in results:
            print(f"Распознано: {text}")


if __name__ == "__main__":
    main()
