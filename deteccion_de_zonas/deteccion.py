import cv2
import os
import numpy as np
from glob import glob

# Ruta donde están tus imágenes (ajústala según tu carpeta)
input_folder = "C:\\Users\\artur\\OneDrive\\Escritorio\\Programacion\\Python\\detecta_signos\\raw_input"
output_folder = "C:\\Users\\artur\\OneDrive\\Escritorio\\Programacion\\Python\\detecta_signos\\yolo_output"

# Definimos el rango de marrón en HSV
lower_brown = np.array([10, 100, 20])
upper_brown = np.array([30, 255, 200])

# ID de clase para YOLO
class_id = 0

# Procesamos cada imagen .jpg
image_paths = glob(os.path.join(input_folder, "*.jpg"))

for img_path in image_paths:
    img = cv2.imread(img_path)
    h, w, _ = img.shape

    # Convertimos a HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Creamos la máscara del color marrón
    mask = cv2.inRange(hsv, lower_brown, upper_brown)

    # Obtenemos los contornos de las zonas marrones
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    yolo_lines = []
    for cnt in contours:
        x, y, bw, bh = cv2.boundingRect(cnt)

        # Ignorar regiones pequeñas para evitar ruido
        if bw * bh < 100:
            continue

        # Coordenadas normalizadas para YOLO
        x_center = (x + bw / 2) / w
        y_center = (y + bh / 2) / h
        norm_w = bw / w
        norm_h = bh / h

        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {norm_w:.6f} {norm_h:.6f}")

    # Guardamos el .txt
    base = os.path.splitext(os.path.basename(img_path))[0]
    txt_path = os.path.join(output_folder, base + ".txt")
    with open(txt_path, "w") as f:
        f.write("\n".join(yolo_lines))

    print(f"Anotaciones generadas para: {base}")
