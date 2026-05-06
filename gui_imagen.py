# ══════════════════════════════════════════════
# Panel Imagen - Visualización + controles
# ══════════════════════════════════════════════

import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from config import *


class Panel_Imagen(ctk.CTkFrame):
    """Panel izquierdo: imagen, descripción, controles."""

    def __init__(self, master, callback_procesar, callback_cargar, callback_rapido, **kwargs):
        super().__init__(master, fg_color=COLOR_PANEL, corner_radius=0, **kwargs)
        self.callback_procesar = callback_procesar
        self.callback_cargar = callback_cargar
        self.callback_rapido = callback_rapido
        self.img_tk = None
        self.img_original_tk = None
        self._crear_widgets()

    def _crear_widgets(self):
        # ── Descripción del ejercicio ──
        self.lbl_descripcion = ctk.CTkLabel(
            self, text="", text_color=COLOR_TEXTO,
            font=FUENTE_DESC, justify="left", anchor="nw",
            wraplength=440,
        )
        self.lbl_descripcion.pack(fill="x", padx=15, pady=(15, 10))

        # ── Frame imagen ──
        img_frame = ctk.CTkFrame(self, fg_color=COLOR_FONDO,
                                  border_width=1, border_color=COLOR_VERDE_DIM,
                                  corner_radius=4)
        img_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # Esquinas decorativas estilo PPT
        self.lbl_imagen = ctk.CTkLabel(img_frame, text="", fg_color="transparent")
        self.lbl_imagen.pack(expand=True, fill="both", padx=5, pady=5)

        # ── Estado / info ──
        self.lbl_estado = ctk.CTkLabel(
            self, text="> estado: listo", text_color=COLOR_VERDE,
            font=FUENTE_TERMINAL, anchor="w",
        )
        self.lbl_estado.pack(fill="x", padx=15, pady=(5, 5))

        # ── Botones ──
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", padx=15, pady=(5, 15))

        self.btn_cargar = ctk.CTkButton(
            btn_frame, text="📁 Cargar Imagen",
            font=FUENTE_BOTON,
            fg_color=COLOR_BOTON, hover_color=COLOR_BOTON_HOVER,
            border_width=1, border_color=COLOR_VERDE_DIM,
            text_color=COLOR_VERDE, corner_radius=4,
            height=50, command=self._cargar_imagen,
        )
        self.btn_cargar.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.btn_rapido = ctk.CTkButton(
            btn_frame, text="⚡ RÁPIDO",
            font=FUENTE_BOTON,
            fg_color="#3a2f0f", hover_color="#4a3f1f",
            border_width=2, border_color="#d4af37",
            text_color="#d4af37", corner_radius=4,
            height=50, command=self.callback_rapido,
        )
        self.btn_rapido.pack(side="left", fill="x", expand=True, padx=5)

        self.btn_procesar = ctk.CTkButton(
            btn_frame, text="▶ PROCESAR",
            font=FUENTE_BOTON,
            fg_color="#0f2f0f", hover_color="#1a4a1a",
            border_width=2, border_color=COLOR_VERDE,
            text_color=COLOR_VERDE, corner_radius=4,
            height=50, command=self.callback_procesar,
        )
        self.btn_procesar.pack(side="right", fill="x", expand=True, padx=(5, 0))

    def Cargar_Descripcion(self, texto):
        """Actualiza descripción del ejercicio."""
        self.lbl_descripcion.configure(text=texto)

    def Mostrar_Imagen(self, img_pil, es_resultado=False):
        """Muestra imagen PIL en el panel."""
        # Redimensionar manteniendo aspecto
        max_w, max_h = 560, 420
        ratio = min(max_w / img_pil.width, max_h / img_pil.height)
        new_size = (int(img_pil.width * ratio), int(img_pil.height * ratio))
        img_resized = img_pil.resize(new_size, Image.LANCZOS)

        self.img_tk = ctk.CTkImage(light_image=img_resized, size=new_size)
        self.lbl_imagen.configure(image=self.img_tk, text="")

        if es_resultado:
            self.Actualizar_Estado("> estado: procesado ✓", COLOR_EXITO)
        else:
            self.Actualizar_Estado("> estado: imagen cargada", COLOR_VERDE)

    def Actualizar_Estado(self, texto, color=COLOR_VERDE):
        """Actualiza label de estado."""
        self.lbl_estado.configure(text=texto, text_color=color)

    def Bloquear_Botones(self, bloqueado=True):
        """Bloquea/desbloquea botones durante procesamiento."""
        estado = "disabled" if bloqueado else "normal"
        self.btn_cargar.configure(state=estado)
        self.btn_procesar.configure(state=estado)
        self.btn_rapido.configure(state=estado)
        if bloqueado:
            self.btn_procesar.configure(text="⏳ Proc...")
            self.btn_rapido.configure(text="⏳...")
        else:
            self.btn_procesar.configure(text="▶ PROCESAR")
            self.btn_rapido.configure(text="⚡ RÁPIDO")

    def _cargar_imagen(self):
        """Abre diálogo para cargar imagen."""
        path = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[
                ("Imágenes", "*.png *.jpg *.jpeg *.bmp *.webp"),
                ("Todos", "*.*"),
            ]
        )
        if path:
            self.callback_cargar(path)
