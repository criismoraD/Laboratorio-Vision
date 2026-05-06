# ══════════════════════════════════════════════════════════════
# INTERFAZ INTERACTIVA - EJERCICIOS VISIÓN COMPUTACIONAL
# SENATI - Machine Learning y Deep Learning
# Expositores: Leticia Ivett Carlos Rojas, Christian Mora Damian
# ══════════════════════════════════════════════════════════════

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
import threading
import queue
import time
import os
import sys
import subprocess

# Módulos propios
from config import *
from ejercicios import EJERCICIOS
from gui_codigo import Panel_Codigo
from gui_imagen import Panel_Imagen
from procesador import (
    Procesar_Yolo, Procesar_Cnn, Procesar_Rostros,
    Procesar_Vit, Procesar_Segmentacion, Procesar_Gemma,
    Generar_Parches_Visual, Generar_Overlay_Clasificacion,
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Cola_Tts:
    """Cola TTS — evita sobreposición de voces."""

    def __init__(self):
        self.cola = queue.Queue()
        self.hilo = threading.Thread(target=self._worker, daemon=True)
        self.hilo.start()

    def _worker(self):
        while True:
            texto = self.cola.get()
            try:
                # SAPI via PowerShell (más confiable que pyttsx3)
                safe = texto.replace('"', "'").replace('\n', ' ')
                cmd = (
                    f'Add-Type -AssemblyName System.Speech; '
                    f'$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
                    f'$s.Rate = 3; '
                    f'$s.Speak("{safe}")'
                )
                subprocess.run(
                    ["powershell", "-Command", cmd],
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    creationflags=0x08000000, timeout=45,
                )
            except Exception:
                pass
            self.cola.task_done()

    def Hablar(self, texto):
        # Limpiar cola (solo último mensaje)
        while not self.cola.empty():
            try:
                self.cola.get_nowait()
                self.cola.task_done()
            except queue.Empty:
                break
        self.cola.put(texto)


class App_Vision(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("  >_ Visión Computacional — SENATI")
        self.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.configure(fg_color=COLOR_FONDO)
        self.minsize(1300, 750)

        self.ejercicio_actual = 0
        self.img_pil_actual = None
        self.img_cv_actual = None
        self.ejecutando = False
        self.hilo_ejecucion = None
        self._path_custom = None
        self.tts = Cola_Tts()
        self.tts_activo = True  # TTS encendido por defecto

        self._crear_interfaz()
        self._cambiar_ejercicio(0)

    # ─────────────────────────────────────────
    # INTERFAZ
    # ─────────────────────────────────────────
    def _crear_interfaz(self):
        # ── HEADER ──
        header = ctk.CTkFrame(self, fg_color=COLOR_BORDE, height=50, corner_radius=0)
        header.pack(fill="x")
        header.pack_propagate(False)

        ctk.CTkLabel(
            header, text=">_ Visión_Computacional",
            text_color=COLOR_VERDE, font=FUENTE_TITULO,
        ).pack(side="left", padx=20)

        ctk.CTkLabel(
            header, text="SENATI",
            text_color=COLOR_VERDE_DIM, font=FUENTE_TAB,
        ).pack(side="right", padx=20)

        tabs_frame = ctk.CTkFrame(header, fg_color="transparent")
        tabs_frame.pack(side="right", padx=10)

        # Botón TTS toggle
        self.btn_tts = ctk.CTkButton(
            header, text="🔊 TTS", width=80, height=28,
            font=("Consolas", 11, "bold"),
            fg_color="#0f2f0f", hover_color=COLOR_BOTON_HOVER,
            border_width=1, border_color=COLOR_VERDE,
            text_color=COLOR_VERDE, corner_radius=4,
            command=self._toggle_tts,
        )
        self.btn_tts.pack(side="right", padx=5)

        self.tabs = []
        for i, ej in enumerate(EJERCICIOS):
            btn = ctk.CTkButton(
                tabs_frame, text=ej["titulo"],
                font=FUENTE_TAB, width=160, height=32,
                fg_color="transparent",
                hover_color=COLOR_BOTON_HOVER,
                border_width=1, border_color=COLOR_BORDE,
                text_color=COLOR_TEXTO, corner_radius=4,
                command=lambda idx=i: self._cambiar_ejercicio(idx),
            )
            btn.pack(side="left", padx=2)
            self.tabs.append(btn)

        ctk.CTkFrame(self, fg_color=COLOR_VERDE, height=1, corner_radius=0).pack(fill="x")

        # ── CONTENIDO ──
        contenido = ctk.CTkFrame(self, fg_color=COLOR_FONDO, corner_radius=0)
        contenido.pack(fill="both", expand=True)

        # Panel izquierdo (imagen) — MÁS ANCHO
        self.panel_imagen = Panel_Imagen(
            contenido,
            callback_procesar=self._iniciar_ejecucion,
            callback_cargar=self._cargar_imagen_externa,
        )
        self.panel_imagen.pack(side="left", fill="both", expand=False)
        self.panel_imagen.configure(width=480)
        self.panel_imagen.pack_propagate(False)

        ctk.CTkFrame(contenido, fg_color=COLOR_VERDE, width=1, corner_radius=0).pack(side="left", fill="y")

        # Panel derecho (código + terminal)
        panel_derecho = ctk.CTkFrame(contenido, fg_color=COLOR_FONDO, corner_radius=0)
        panel_derecho.pack(side="right", fill="both", expand=True)
        self.panel_codigo = Panel_Codigo(panel_derecho)
        self.panel_codigo.pack(fill="both", expand=True)

        # ── FOOTER ──
        footer = ctk.CTkFrame(self, fg_color=COLOR_BORDE, height=25, corner_radius=0)
        footer.pack(fill="x")
        footer.pack_propagate(False)
        ctk.CTkLabel(
            footer,
            text=">_ Machine Learning y Deep Learning | Instructor: Javier Arturo Urbina Bravo",
            text_color="#3a5a3a", font=("Consolas", 10),
        ).pack(side="left", padx=10)

    # ─────────────────────────────────────────
    # TTS CONTROL
    # ─────────────────────────────────────────
    def _toggle_tts(self):
        """Activa/desactiva TTS."""
        self.tts_activo = not self.tts_activo
        if self.tts_activo:
            self.btn_tts.configure(
                text="🔊 TTS", fg_color="#0f2f0f",
                border_color=COLOR_VERDE, text_color=COLOR_VERDE,
            )
        else:
            self.btn_tts.configure(
                text="🔇 TTS", fg_color="#1a1a1a",
                border_color="#333", text_color="#666",
            )

    def _hablar(self, texto):
        """Habla solo si TTS activo."""
        if self.tts_activo:
            self.tts.Hablar(texto)

    # ─────────────────────────────────────────
    # LÓGICA EJERCICIOS
    # ─────────────────────────────────────────
    def _cambiar_ejercicio(self, idx):
        if self.ejecutando:
            return
        self.ejercicio_actual = idx
        self._path_custom = None
        ej = EJERCICIOS[idx]

        for i, tab in enumerate(self.tabs):
            if i == idx:
                tab.configure(fg_color=COLOR_VERDE_DIM, border_color=COLOR_VERDE, text_color=COLOR_VERDE)
            else:
                tab.configure(fg_color="transparent", border_color=COLOR_BORDE, text_color=COLOR_TEXTO)

        self.panel_codigo.Cargar_Codigo(ej["codigo"], ej["titulo"])
        self.panel_imagen.Cargar_Descripcion(ej["descripcion"])

        img_path = os.path.join(BASE_DIR, ej["imagen_default"])
        if os.path.exists(img_path):
            self._cargar_imagen(img_path)
        else:
            self.panel_imagen.Actualizar_Estado(f"> [WARN] No encontrada: {ej['imagen_default']}", COLOR_ERROR)

    def _cargar_imagen(self, path):
        try:
            self.img_pil_actual = Image.open(path).convert("RGB")
            self.img_cv_actual = cv2.imread(path)
            if self.img_cv_actual is None:
                self.img_cv_actual = cv2.cvtColor(np.array(self.img_pil_actual), cv2.COLOR_RGB2BGR)
            self.panel_imagen.Mostrar_Imagen(self.img_pil_actual)
        except Exception as e:
            self.panel_imagen.Actualizar_Estado(f"> [ERROR] {e}", COLOR_ERROR)

    def _cargar_imagen_externa(self, path):
        self._path_custom = path
        self._cargar_imagen(path)
        self.panel_codigo.Log_Terminal(f"[OK]  Imagen cargada: {os.path.basename(path)}")

    # ─────────────────────────────────────────
    # EJECUCIÓN
    # ─────────────────────────────────────────
    def _iniciar_ejecucion(self):
        if self.ejecutando or self.img_pil_actual is None:
            if self.img_pil_actual is None:
                self.panel_imagen.Actualizar_Estado("> [ERROR] Cargar imagen primero", COLOR_ERROR)
            return

        self.ejecutando = True
        self.panel_imagen.Bloquear_Botones(True)
        self.panel_codigo.Limpiar_Terminal()
        self.panel_codigo.Log_Terminal("[INFO] Iniciando ejecución...")

        self.hilo_ejecucion = threading.Thread(target=self._ejecutar_lineas, daemon=True)
        self.hilo_ejecucion.start()

    def _ejecutar_lineas(self):
        ej = EJERCICIOS[self.ejercicio_actual]
        lineas = ej["codigo"]
        resultado_img = None
        resultado_texto = []

        for i, linea in enumerate(lineas):
            if not self.ejecutando:
                break

            self.after(0, self.panel_codigo.Resaltar_Linea, i)

            if linea.get("log"):
                self.after(0, self.panel_codigo.Log_Terminal, linea["log"])

            self.after(0, self.panel_imagen.Actualizar_Estado, f"> ejecutando línea {i+1}...")

            accion = linea.get("accion")
            if accion == "procesar":
                self.after(0, self.panel_imagen.Actualizar_Estado, "> procesando imagen...", COLOR_STRING)
                resultado_img, resultado_texto = self._ejecutar_procesamiento()
            elif accion == "parches":
                if self.img_pil_actual:
                    img_parches = Generar_Parches_Visual(self.img_pil_actual)
                    self.after(0, self.panel_imagen.Mostrar_Imagen, img_parches)
            elif accion == "mostrar":
                if resultado_img is not None:
                    self.after(0, self._mostrar_resultado, resultado_img, resultado_texto)

            time.sleep(linea["delay"] / 1000.0)

        self.after(0, self._finalizar_ejecucion)

    def _ejecutar_procesamiento(self):
        """0=Rostros, 1=YOLO, 2=CNN, 3=ViT, 4=Segmentación, 5=Gemma"""
        idx = self.ejercicio_actual
        try:
            if idx == 0:  # Rostros
                img_cv = self.img_cv_actual.copy()
                img_resultado, num = Procesar_Rostros(img_cv)
                img_pil = Image.fromarray(cv2.cvtColor(img_resultado, cv2.COLOR_BGR2RGB))
                return img_pil, [f"  Rostros detectados: {num}"]

            elif idx == 1:  # YOLO
                img_cv = self.img_cv_actual.copy()
                img_resultado, detecciones = Procesar_Yolo(img_cv)
                img_pil = Image.fromarray(cv2.cvtColor(img_resultado, cv2.COLOR_BGR2RGB))
                return img_pil, detecciones

            elif idx == 2:  # CNN
                resultados = Procesar_Cnn(self.img_pil_actual)
                img_overlay = Generar_Overlay_Clasificacion(self.img_pil_actual, resultados)
                textos = [f"  {n}: {p:.1%}," for n, p in resultados]
                return img_overlay, textos

            elif idx == 3:  # ViT
                resultados = Procesar_Vit(self.img_pil_actual)
                img_overlay = Generar_Overlay_Clasificacion(self.img_pil_actual, resultados)
                textos = [f"  {n}: {p:.1%}," for n, p in resultados]
                return img_overlay, textos

            elif idx == 4:  # Segmentación
                img_resultado = Procesar_Segmentacion(self.img_pil_actual)
                return img_resultado, ["  Segmentación semántica completa"]

            elif idx == 5:  # Gemma 4 LLM
                img_r, texto = Procesar_Gemma(self.img_pil_actual)
                if img_r is None:
                    return self.img_pil_actual, [f"  {texto}"]
                # Partir texto largo en líneas
                lineas_resp = [f"  {l.strip()}" for l in texto.split('.') if l.strip()]
                return img_r, lineas_resp[:8]

        except Exception as e:
            self.after(0, self.panel_codigo.Log_Terminal, f"[ERROR] {str(e)}", "error")
            return self.img_pil_actual, [f"  Error: {e}"]
        return None, []

    def _mostrar_resultado(self, img_pil, textos):
        if img_pil:
            self.panel_imagen.Mostrar_Imagen(img_pil, es_resultado=True)
        for txt in textos:
            self.panel_codigo.Log_Terminal(txt)
        
        texto_hablar = " ".join([t.replace("  ", "") for t in textos])
        if texto_hablar:
            self._hablar(texto_hablar)
        # Abrir ventana flotante con resultado a tamaño completo
        if img_pil:
            self._abrir_ventana_resultado(img_pil)

    def _abrir_ventana_resultado(self, img_pil):
        """Ventana flotante con imagen resultado a tamaño completo."""
        ventana = ctk.CTkToplevel(self)
        ventana.title(">_ Resultado Procesado")
        ventana.configure(fg_color=COLOR_FONDO)
        ventana.attributes("-topmost", True)

        # Escalar imagen para caber en pantalla
        screen_w = self.winfo_screenwidth() - 100
        screen_h = self.winfo_screenheight() - 150
        ratio = min(screen_w / img_pil.width, screen_h / img_pil.height, 1.0)
        new_w = int(img_pil.width * ratio)
        new_h = int(img_pil.height * ratio)
        img_resized = img_pil.resize((new_w, new_h), Image.LANCZOS)

        ventana.geometry(f"{new_w + 20}x{new_h + 60}")

        # Header
        ctk.CTkLabel(
            ventana, text=f"> {EJERCICIOS[self.ejercicio_actual]['titulo']} — Resultado",
            text_color=COLOR_VERDE, font=("Consolas", 16, "bold"),
        ).pack(pady=(10, 5))

        # Imagen
        img_ctk = ctk.CTkImage(light_image=img_resized, size=(new_w, new_h))
        lbl = ctk.CTkLabel(ventana, text="", image=img_ctk, fg_color="transparent")
        lbl.pack(padx=10, pady=(0, 10))
        # Mantener referencia
        ventana._img_ref = img_ctk

    def _finalizar_ejecucion(self):
        self.ejecutando = False
        self.panel_imagen.Bloquear_Botones(False)
        self.panel_codigo.Log_Terminal("[OK]  Ejecución completada ✓")
        self.panel_codigo.Resaltar_Linea(-1)


if __name__ == "__main__":
    app = App_Vision()
    app.mainloop()
