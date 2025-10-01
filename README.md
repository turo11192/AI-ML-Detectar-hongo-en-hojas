#Cómo correr todo

**Instalación de dependencias:

git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt


**Entrenamiento:

python train.py --img 640 --batch 16 --epochs 100 --data ../hongos.yaml --weights yolov5s.pt --name detectahongos
Detección:

python ../detecta.py
