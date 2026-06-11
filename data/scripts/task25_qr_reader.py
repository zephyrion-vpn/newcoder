import os
import tempfile


def decode_qr(path: str) -> list[str]:
    try:
        from PIL import Image
        from pyzbar.pyzbar import decode

        return [item.data.decode("utf-8") for item in decode(Image.open(path))]
    except ImportError:
        pass
    import cv2

    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Не удалось открыть изображение: {path}")
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    return [data] if data else []


def _generate_qr(text: str, path: str) -> bool:
    try:
        import qrcode

        qrcode.make(text).save(path)
        return True
    except ImportError:
        pass
    try:
        import cv2

        encoder = cv2.QRCodeEncoder_create()
        image = encoder.encode(text)
        image = cv2.copyMakeBorder(image, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=255)
        image = cv2.resize(image, None, fx=8, fy=8, interpolation=cv2.INTER_NEAREST)
        cv2.imwrite(path, image)
        return True
    except Exception:
        return False


def main() -> None:
    text = "https://example.com/secret-token"
    path = tempfile.mktemp(suffix=".png")
    if not _generate_qr(text, path):
        print("Нет библиотеки для генерации QR. Передайте путь к изображению в decode_qr().")
        return
    try:
        print("Содержимое QR:", decode_qr(path))
    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
