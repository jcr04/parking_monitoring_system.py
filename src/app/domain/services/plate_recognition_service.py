# Em domain/services/plate_recognition_service.py
import cv2  # OpenCV
import pytesseract
from typing import Optional

class PlateRecognitionService:
    def __init__(self, tesseract_cmd: str):
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd  # Caminho para o executável do Tesseract
    
    def recognize_plate(self, image_path: str) -> Optional[str]:
        # Carregue a imagem
        image = cv2.imread(image_path)
        
        if image is None:
            raise ValueError(f"Unable to load image at path: {image_path}")
        
        # Converta a imagem para escala de cinza
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Aplique um desfoque para remover ruídos
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Detecte bordas
        edged = cv2.Canny(blurred, 50, 200, 255)
        
        # Encontre contornos na imagem
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        # Ordene os contornos com base na área em ordem decrescente
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        
        plate_number = None
        for contour in contours:
            # Aproxime o contorno
            peri = cv
