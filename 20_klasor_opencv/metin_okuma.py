from PIL import Image 
import pytesseract

img = Image.open("C:\\Users\\dila\\Desktop\\opencv.project\\input\\text.png")
text = pytesseract.image_to_string(img,lang="eng")
print(text)