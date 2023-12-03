import cv2
import numpy as np

# Resmi yükle
image_path = "pirinc.jpg"
image = cv2.imread(image_path)

# Resmin başarıyla yüklenip yüklenmediğini kontrol et
if image is None:
    print(f"Hata: {image_path} dosyası bulunamadı veya okunamadı.")
else:
    # Gri seviyeye dönüştür
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Eşikleme yap
    _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)

    # Morfolojik işlemler (istenmeyen arka planları temizleme)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Konturları bul
    contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Her bir konturu çiz ve say
    rice_count = 0
    for contour in contours:
        # Kontur alanını hesapla
        area = cv2.contourArea(contour)

        # Belirli bir alanın altındaki konturları filtrele
        if 100 < area < 5000:  # Minimum ve maksimum alan değerlerini ayarlayın
            # Konturu çiz
            cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)

            # Pirinç sayısını artır
            rice_count += 1

    # Sonuçları ekrana yazdır
    print(f"Pirinç Sayısı: {rice_count}")

    # Görüntüleri göster
    cv2.imshow("Original Image", image)
    cv2.imshow("Thresholded Image", opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
