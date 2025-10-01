# detectar.py
import torch
from PIL import Image

# Cargar el modelo entrenado
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\artur\OneDrive\Escritorio\Programacion\Python\detecta_signos\yolov5\runs\train\detectahongos\weights\best.pt')


# Imagen para detectar
img_path = r"C:\Users\artur\OneDrive\Escritorio\Programacion\Python\detecta_signos\raw_input\img6.jpg"

# Detección
results = model(img_path)
results.print()
results.show()  # Muestra la imagen con los resultados

# Guardar resultados
results.save(save_dir='C:/Users/artur/OneDrive/Escritorio/Programacion/Python/detecta_signos/resultados')
