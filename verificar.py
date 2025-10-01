import os
import cv2

# Rutas a las carpetas
images_dir = r"C:\Users\artur\OneDrive\Escritorio\Programacion\Python\detecta_signos\hongos\images\train"
labels_dir = r"C:\Users\artur\OneDrive\Escritorio\Programacion\Python\detecta_signos\hongos\labels\train"

# Función para verificar una imagen y su label
def verificar_imagen_y_label(imagen_path, label_path):
    if not os.path.exists(label_path):
        print(f"No hay label para la imagen: {imagen_path}")
        return
    
    img = cv2.imread(imagen_path)
    if img is None:
        print(f"Imagen no válida o corrupta: {imagen_path}")
        return

    height, width, _ = img.shape

    with open(label_path, 'r') as f:
        for i, line in enumerate(f):
            parts = line.strip().split()
            if len(parts) != 5:
                print(f"Línea malformada en {label_path} (línea {i+1})")
                continue
            cls, x, y, w, h = map(float, parts)
            if not (0 <= x <= 1 and 0 <= y <= 1 and 0 <= w <= 1 and 0 <= h <= 1):
                print(f"Coordenadas fuera de rango en {label_path} (línea {i+1}): {x}, {y}, {w}, {h}")
    
    print(f"{os.path.basename(imagen_path)} está OK")

# Verificar todos los archivos
for image_name in os.listdir(images_dir):
    if image_name.endswith(('.jpg', '.jpeg', '.png')):
        name = os.path.splitext(image_name)[0]
        image_path = os.path.join(images_dir, image_name)
        label_path = os.path.join(labels_dir, name + ".txt")
        verificar_imagen_y_label(image_path, label_path)
