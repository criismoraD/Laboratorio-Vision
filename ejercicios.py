# ══════════════════════════════════════════════
# Datos de los 4 ejercicios de Visión Computacional
# Orden: Fácil → Difícil
# ══════════════════════════════════════════════

EJERCICIOS = [
    {
        "titulo": "01_DETECCIÓN_ROSTROS",
        "descripcion": (
            "> Detección de Rostros (Haar Cascade)\n\n"
            "Algoritmo clásico de Viola-Jones que\n"
            "busca patrones faciales en la imagen.\n\n"
            "Convierte a escala de grises y aplica\n"
            "un clasificador en cascada para hallar\n"
            "coordenadas de cada rostro.\n\n"
            "[Modelo: Haar Cascade — incluido en OpenCV]"
        ),
        "imagen_default": "imagenes_ejemplo/rostros_deteccion.png",
        "codigo": [
            {"texto": "import cv2",                                  "tipo": "import",     "delay": 400,  "log": "[INFO] Importando OpenCV..."},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar detector Haar Cascade preentrenado", "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "# Viene incluido con OpenCV, no descarga nada","tipo": "comentario","delay": 500,  "log": None},
            {"texto": "haarcascades = cv2.data.haarcascades",        "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": "detector = cv2.CascadeClassifier(",           "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": '    haarcascades + "haarcascade_frontalface_default.xml"', "tipo": "codigo", "delay": 500, "log": "[OK]  Detector cargado", "accion": "cargar_modelo"},
            {"texto": ")",                                           "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar imagen",                             "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": 'img = cv2.imread("imagen.jpg")',              "tipo": "codigo",     "delay": 600,  "log": "[OK]  Imagen cargada"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Convertir a escala de grises",              "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "# El detector trabaja mejor en grises",       "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)","tipo": "codigo",     "delay": 700,  "log": "[INFO] Convirtiendo a grises..."},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Inferencia: detectar rostros",              "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "rostros = detector.detectMultiScale(",        "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": "    gray, scaleFactor=1.1, minNeighbors=4",   "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": ")",                                           "tipo": "codigo",     "delay": 1500, "log": "[INFO] Escaneando rostros...", "accion": "procesar"},
            {"texto": 'print("Rostros detectados:", len(rostros))',  "tipo": "codigo",     "delay": 500,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Dibujar cajas delimitadoras",               "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "for x, y, w, h in rostros:",                  "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)", "tipo": "codigo", "delay": 500, "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": 'cv2.imshow("Detección de rostros", img)',     "tipo": "codigo",     "delay": 800,  "log": "[OK]  Resultado listo", "accion": "mostrar"},
            {"texto": "cv2.waitKey(0)",                              "tipo": "codigo",     "delay": 300,  "log": None},
        ],
    },
    {
        "titulo": "02_DETECCIÓN_YOLO",
        "descripcion": (
            "> Detección de Objetos con YOLOv8\n\n"
            "YOLO (You Only Look Once) detecta\n"
            "múltiples objetos en una sola pasada.\n\n"
            "Identifica: personas, autos, animales,\n"
            "objetos cotidianos con bounding boxes\n"
            "y porcentaje de confianza.\n\n"
            "[Modelo: yolov8n — 3.2M parámetros]"
        ),
        "imagen_default": "imagenes_ejemplo/ciudad_yolo.png",
        "codigo": [
            {"texto": "from ultralytics import YOLO",              "tipo": "import",     "delay": 500,  "log": "[INFO] Importando YOLOv8..."},
            {"texto": "import cv2",                                  "tipo": "import",     "delay": 300,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar modelo YOLOv8 nano preentrenado",   "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "# Es el más rápido de la familia YOLO",      "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": 'modelo = YOLO("yolov8n.pt")',                "tipo": "codigo",     "delay": 1200, "log": "[INFO] Cargando modelo YOLOv8n...", "accion": "cargar_modelo"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar la imagen a analizar",              "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": 'img = cv2.imread("imagen.jpg")',             "tipo": "codigo",     "delay": 600,  "log": "[OK]  Imagen cargada correctamente"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Ejecutar inferencia (detección)",           "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "# YOLO analiza toda la imagen de una vez",    "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "resultados = modelo(img)",                    "tipo": "codigo",     "delay": 2000, "log": "[INFO] Ejecutando inferencia...", "accion": "procesar"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Dibujar detecciones sobre la imagen",      "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "for r in resultados:",                        "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    for box in r.boxes:",                     "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "        x1,y1,x2,y2 = map(int, box.xyxy[0])","tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": "        clase = modelo.names[int(box.cls[0])]","tipo": "codigo",    "delay": 400,  "log": None},
            {"texto": "        conf = float(box.conf[0])",           "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": '        cv2.rectangle(img, ...)',             "tipo": "codigo",     "delay": 500,  "log": None},
            {"texto": '        cv2.putText(img, f"{clase} {conf:.0%}", ...)', "tipo": "codigo", "delay": 500, "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Mostrar resultado final",                  "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": 'cv2.imshow("Detección YOLO", img)',          "tipo": "codigo",     "delay": 800,  "log": "[OK]  Resultado listo", "accion": "mostrar"},
            {"texto": "cv2.waitKey(0)",                              "tipo": "codigo",     "delay": 300,  "log": None},
        ],
    },
    {
        "titulo": "03_CLASIFICACIÓN_CNN",
        "descripcion": (
            "> Clasificación con CNN (ResNet18)\n\n"
            "Red Neuronal Convolucional que clasifica\n"
            "una imagen en 1000 categorías posibles.\n\n"
            "ResNet18 aprende patrones jerárquicos:\n"
            "bordes → texturas → partes → objeto.\n\n"
            "[Modelo: ResNet18 — 11.7M parámetros]"
        ),
        "imagen_default": "imagenes_ejemplo/animal_cnn.png",
        "codigo": [
            {"texto": "import torch",                               "tipo": "import",     "delay": 400,  "log": "[INFO] Importando PyTorch..."},
            {"texto": "import torchvision.transforms as transforms", "tipo": "import",     "delay": 300,  "log": None},
            {"texto": "from torchvision import models",              "tipo": "import",     "delay": 300,  "log": None},
            {"texto": "from PIL import Image",                       "tipo": "import",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar ResNet18 preentrenado en ImageNet",  "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "modelo = models.resnet18(weights='DEFAULT')", "tipo": "codigo",     "delay": 1500, "log": "[INFO] Cargando ResNet18...", "accion": "cargar_modelo"},
            {"texto": "modelo.eval()  # Modo evaluación",           "tipo": "codigo",     "delay": 400,  "log": "[OK]  Modelo en modo eval"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Pipeline de preprocesamiento",             "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "# La imagen debe ser 224x224, normalizada",   "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "transform = transforms.Compose([",            "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    transforms.Resize(256),",                 "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.CenterCrop(224),",             "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.ToTensor(),",                  "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.Normalize(mean, std)",         "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "])",                                          "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar y transformar imagen",               "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": 'img = Image.open("imagen.jpg")',              "tipo": "codigo",     "delay": 500,  "log": "[OK]  Imagen cargada"},
            {"texto": "tensor = transform(img).unsqueeze(0)",        "tipo": "codigo",     "delay": 600,  "log": "[INFO] Preprocesando tensor..."},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Inferencia: obtener predicción",            "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "with torch.no_grad():",                       "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    salida = modelo(tensor)",                 "tipo": "codigo",     "delay": 1500, "log": "[INFO] Ejecutando inferencia...", "accion": "procesar"},
            {"texto": "    probs = F.softmax(salida[0], dim=0)",     "tipo": "codigo",     "delay": 500,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Obtener Top-5 predicciones",               "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "top5 = torch.topk(probs, 5)",                "tipo": "codigo",     "delay": 500,  "log": None, "accion": "mostrar"},
            {"texto": "for i in range(5):",                          "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": '    print(f"{clases[idx]}: {prob:.1%}")',     "tipo": "codigo",     "delay": 600,  "log": "[OK]  Clasificación completada"},
        ],
    },
    {
        "titulo": "04_VISION_TRANSFORMER",
        "descripcion": (
            "> Vision Transformer (ViT)\n\n"
            "A diferencia de las CNN, los Transformers\n"
            "dividen la imagen en parches (patches)\n"
            "y los analizan todos al mismo tiempo.\n\n"
            "Capturan relaciones a larga distancia\n"
            "para entender el contexto global.\n\n"
            "[Modelo: ViT-B/16 — 86M parámetros]"
        ),
        "imagen_default": "imagenes_ejemplo/machu_picchu.png",
        "codigo": [
            {"texto": "import torch",                               "tipo": "import",     "delay": 400,  "log": "[INFO] Importando PyTorch..."},
            {"texto": "from torchvision import models, transforms",  "tipo": "import",     "delay": 300,  "log": None},
            {"texto": "from PIL import Image",                       "tipo": "import",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar Vision Transformer preentrenado",    "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "# ViT divide la imagen en parches de 16x16", "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "modelo = models.vit_b_16(weights='DEFAULT')", "tipo": "codigo",     "delay": 1500, "log": "[INFO] Cargando ViT-B/16...", "accion": "cargar_modelo"},
            {"texto": "modelo.eval()",                               "tipo": "codigo",     "delay": 400,  "log": "[OK]  Modelo listo"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Preprocesar: resize a 224x224",             "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "transform = transforms.Compose([",            "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    transforms.Resize(224),",                 "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.CenterCrop(224),",             "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.ToTensor(),",                  "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.Normalize(mean, std)",         "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "])",                                          "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Dividir imagen en 196 parches (14x14 grid)","tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "# Cada parche = un 'token' para el Transformer","tipo": "comentario","delay": 600, "log": None},
            {"texto": 'img = Image.open("imagen.jpg")',              "tipo": "codigo",     "delay": 500,  "log": "[OK]  Imagen cargada"},
            {"texto": "tensor = transform(img).unsqueeze(0)",        "tipo": "codigo",     "delay": 500,  "log": "[INFO] Generando parches...", "accion": "parches"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Inferencia con atención global",            "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "with torch.no_grad():",                       "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    salida = modelo(tensor)",                 "tipo": "codigo",     "delay": 2000, "log": "[INFO] Atención global...", "accion": "procesar"},
            {"texto": "    probs = torch.softmax(salida[0], dim=0)", "tipo": "codigo",     "delay": 500,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Predicción del Transformer",                "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "top5 = torch.topk(probs, 5)",                "tipo": "codigo",     "delay": 500,  "log": None, "accion": "mostrar"},
            {"texto": "for i in range(5):",                          "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": '    print(f"{clases[idx]}: {prob:.1%}")',     "tipo": "codigo",     "delay": 600,  "log": "[OK]  Clasificación ViT completada"},
        ],
    },
    {
        "titulo": "05_SEGMENTACIÓN",
        "descripcion": (
            "> Segmentación Semántica (DeepLabV3)\n\n"
            "Clasifica CADA PÍXEL de la imagen\n"
            "en una categoría (calle, persona,\n"
            "auto, árbol, cielo, edificio...).\n\n"
            "A diferencia de YOLO (cajas), aquí\n"
            "se obtiene el contorno exacto de\n"
            "cada objeto en la escena.\n\n"
            "[Modelo: DeepLabV3 — ResNet50 backbone]"
        ),
        "imagen_default": "imagenes_ejemplo/segmentacion_ciudad.png",
        "codigo": [
            {"texto": "import torch",                               "tipo": "import",     "delay": 400,  "log": "[INFO] Importando PyTorch..."},
            {"texto": "from torchvision import models, transforms",  "tipo": "import",     "delay": 300,  "log": None},
            {"texto": "from PIL import Image",                       "tipo": "import",     "delay": 200,  "log": None},
            {"texto": "import numpy as np",                          "tipo": "import",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar DeepLabV3 preentrenado",             "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "# Backbone: ResNet50 entrenado en COCO",      "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "modelo = models.segmentation.deeplabv3_resnet50(", "tipo": "codigo", "delay": 400, "log": None},
            {"texto": "    weights='DEFAULT'",                       "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": ")",                                           "tipo": "codigo",     "delay": 1500, "log": "[INFO] Cargando DeepLabV3...", "accion": "cargar_modelo"},
            {"texto": "modelo.eval()",                               "tipo": "codigo",     "delay": 400,  "log": "[OK]  Modelo segmentación listo"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Preprocesar imagen",                       "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "transform = transforms.Compose([",            "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    transforms.Resize(520),",                 "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.ToTensor(),",                  "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    transforms.Normalize(mean, std)",         "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "])",                                          "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar imagen de la escena urbana",         "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": 'img = Image.open("ciudad.jpg")',              "tipo": "codigo",     "delay": 500,  "log": "[OK]  Imagen cargada"},
            {"texto": "tensor = transform(img).unsqueeze(0)",        "tipo": "codigo",     "delay": 500,  "log": "[INFO] Preprocesando..."},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Inferencia: segmentar cada píxel",          "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "# El modelo clasifica 21 categorías por píxel","tipo": "comentario","delay": 500,  "log": None},
            {"texto": "with torch.no_grad():",                       "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    salida = modelo(tensor)['out']",          "tipo": "codigo",     "delay": 2000, "log": "[INFO] Segmentando píxeles...", "accion": "procesar"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Obtener mapa de segmentación",              "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "mapa = salida.argmax(1).squeeze()",           "tipo": "codigo",     "delay": 500,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Colorear cada clase con un color único",    "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "colores = crear_paleta(21)",                  "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": "segmentada = colores[mapa]",                  "tipo": "codigo",     "delay": 500,  "log": None, "accion": "mostrar"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": 'cv2.imshow("Segmentación", segmentada)',      "tipo": "codigo",     "delay": 800,  "log": "[OK]  Segmentación completa"},
        ],
    },
    {
        "titulo": "06_GEMMA_4_LLM",
        "descripcion": (
            "> Análisis Multimodal (Gemma 4)\n\n"
            "Modelo de lenguaje con visión de Google.\n"
            "Gemma 4 26B entiende imágenes y genera\n"
            "descripciones detalladas en español.\n\n"
            "A diferencia de CNN/ViT que solo\n"
            "clasifican, un LLM multimodal puede\n"
            "RAZONAR sobre el contenido visual.\n\n"
            "[Modelo: Gemma 4 26B — API Gemini]"
        ),
        "imagen_default": "imagenes_ejemplo/mercado_peru.png",
        "codigo": [
            {"texto": "from google import genai",                    "tipo": "import",     "delay": 400,  "log": "[INFO] Importando SDK Gemini..."},
            {"texto": "from google.genai import types",              "tipo": "import",     "delay": 300,  "log": None},
            {"texto": "from PIL import Image",                       "tipo": "import",     "delay": 200,  "log": None},
            {"texto": "import os",                                   "tipo": "import",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Conectar con Gemini API",                   "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "# Usa Gemma 4 26B multimodal",                "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "client = genai.Client(",                      "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": '    api_key=os.environ["GEMINI_API_KEY"]',    "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": ")",                                           "tipo": "codigo",     "delay": 500,  "log": "[OK]  Cliente API conectado", "accion": "cargar_modelo"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Cargar imagen para análisis",               "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": 'img = Image.open("imagen.jpg")',              "tipo": "codigo",     "delay": 500,  "log": "[OK]  Imagen cargada"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Crear prompt multimodal",                   "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "# El modelo recibe imagen + texto",           "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": 'prompt = "Describe qué ves en la imagen"',    "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "contenido = types.Content(",                  "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": "    role='user',",                            "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "    parts=[img_bytes, prompt]",               "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": ")",                                           "tipo": "codigo",     "delay": 200,  "log": None},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Enviar a Gemma 4 para inferencia",          "tipo": "comentario", "delay": 600,  "log": None},
            {"texto": "# El LLM razona sobre el contenido",          "tipo": "comentario", "delay": 500,  "log": None},
            {"texto": "respuesta = client.models.generate_content(",  "tipo": "codigo",    "delay": 400,  "log": None},
            {"texto": '    model="gemma-4-26b-a4b-it",',             "tipo": "codigo",     "delay": 400,  "log": None},
            {"texto": "    contents=contenido",                      "tipo": "codigo",     "delay": 300,  "log": None},
            {"texto": ")",                                           "tipo": "codigo",     "delay": 3000, "log": "[INFO] Gemma 4 analizando imagen...", "accion": "procesar"},
            {"texto": "",                                            "tipo": "vacio",      "delay": 100,  "log": None},
            {"texto": "# Mostrar descripción generada",              "tipo": "comentario", "delay": 400,  "log": None},
            {"texto": "print(respuesta.text)",                       "tipo": "codigo",     "delay": 800,  "log": "[OK]  Análisis completado", "accion": "mostrar"},
        ],
    },
]
