import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("C:\\Users\\dila\\Desktop\\opencv.project\\input\\para2.jpg")  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Gürültüyü azaltma
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 3. Eşikleme işlemi (Thresholding)
ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 4. Morfolojik işlemler (Gereksiz noktaları temizleme)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 5. Kesin arka planı belirleme (Dilation işlemi)
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 6. Mesafe dönüşümü ile ön plan belirleme
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# 7. Bilinmeyen alanları belirleme
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 8. İşaretleme (Markers)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1  # Arka planı 1 olarak ayarla
markers[unknown == 255] = 0  # Bilinmeyen alanları sıfırla

# 9. Watershed Algoritmasını Uygula
markers = cv2.watershed(image, markers)
image[markers == -1] = [0, 0, 255]  # Sınırları kırmızıya boya

# 10. Sonucu Gösterme
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Watershed Sonucu")
plt.subplot(1, 2, 2)
plt.imshow(markers, cmap="jet")
plt.title("Segmentasyon Haritası")
plt.show()