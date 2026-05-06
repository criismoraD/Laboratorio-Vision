# 👁️ Laboratorio Interactivo de Visión Computacional (SENATI)

Una herramienta educativa de escritorio desarrollada en Python (`customtkinter`) diseñada para demostraciones en vivo sobre algoritmos de inteligencia artificial aplicados a la Visión Computacional.

## 🚀 Características Principales

Esta aplicación permite explicar paso a paso cómo funcionan diferentes modelos de IA dividiendo la interfaz en un panel visual y un emulador de terminal interactivo. 

Cuenta con 6 ejercicios demostrativos:
1. **Detección de Rostros:** Uso de Haar Cascades clásico (OpenCV).
2. **Detección de Objetos (YOLOv8):** Detección en tiempo real con bounding boxes y conteo automático de elementos en la escena.
3. **Clasificación CNN (ResNet18):** Clasificación tradicional de imágenes basada en redes neuronales convolucionales.
4. **Vision Transformer (ViT):** Clasificación basada en atención global utilizando la novedosa arquitectura Transformer aplicada a parches de imagen.
5. **Segmentación Semántica (DeepLabV3):** Identificación precisa de contornos píxel por píxel.
6. **Análisis Multimodal (Gemma 4):** Integración con Google Gemini API para razonamiento avanzado e interpretación detallada de imágenes mediante un Gran Modelo de Lenguaje Multimodal (LLM).

Además incluye:
- **Resaltado de Sintaxis:** Panel de código estilo *VS Code Dark+* que muestra la línea actual en ejecución.
- **Voz TTS Automática:** Narrador de voz integrado para decir en alto los resultados (Ej. "Se detectaron 3 personas").

## 🛠️ Requisitos de Instalación

1. Clona el repositorio:
   ```bash
   git clone <url-de-tu-repo>
   cd EJEMPLO
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install customtkinter pillow opencv-python torch torchvision ultralytics google-genai python-dotenv
   ```

3. Configura las credenciales:
   Crea un archivo llamado `.env` en la raíz del proyecto y añade tu API KEY de Google Gemini (necesario para el ejercicio 6):
   ```
   GEMINI_API_KEY=tu_clave_api_aqui
   ```

## 🎮 Uso

Para iniciar el laboratorio interactivo, simplemente ejecuta:
```bash
python main.py
```

## 📂 Estructura del Proyecto

- `main.py`: Punto de entrada principal y gestor de eventos/hilos.
- `procesador.py`: Contiene toda la lógica de Inferencia (Torch, YOLO, OpenCV, Gemini).
- `gui_codigo.py`: Renderizador de la interfaz derecha (Editor de código y terminal).
- `gui_imagen.py`: Renderizador de la interfaz izquierda (Visor de imágenes).
- `ejercicios.py`: Archivo de configuración con los códigos y textos mostrados en cada ejercicio.
- `config.py`: Definición global de paletas de colores, fuentes y medidas de interfaz.

---
*Proyecto desarrollado para uso pedagógico.*
