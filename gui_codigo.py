# ══════════════════════════════════════════════
# Panel de Código - VS Code Dark+ highlighting
# ══════════════════════════════════════════════

import tkinter as tk
import customtkinter as ctk
import re
from config import *

FUENTE_CODE = ("Consolas", 20)
FUENTE_CODE_BOLD = ("Consolas", 20, "bold")
FUENTE_TERM = ("Consolas", 15)


class Panel_Codigo(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=COLOR_PANEL, corner_radius=0, **kwargs)
        self.linea_actual = -1
        self._crear_widgets()

    def _crear_widgets(self):
        # ── Header ──
        header = ctk.CTkFrame(self, fg_color="#2d2d30", height=36, corner_radius=0)
        header.pack(fill="x")
        header.pack_propagate(False)
        dots = ctk.CTkFrame(header, fg_color="transparent")
        dots.pack(side="left", padx=10)
        for color in ["#ff5f56", "#ffbd2e", "#27c93f"]:
            ctk.CTkLabel(dots, text="●", text_color=color, font=("Arial", 10), width=16).pack(side="left")
        self.lbl_nombre_proyecto = ctk.CTkLabel(
            header, text="codigo.py", text_color="#cccccc",
            font=("Consolas", 15, "bold"),
        )
        self.lbl_nombre_proyecto.pack(side="left", padx=20)

        # ── Grid: código (50%) | terminal (50%) ──
        contenedor = ctk.CTkFrame(self, fg_color=COLOR_FONDO, corner_radius=0)
        contenedor.pack(fill="both", expand=True, padx=0, pady=0)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=80)
        contenedor.grid_columnconfigure(1, weight=0)
        contenedor.grid_columnconfigure(2, weight=20)

        # ── Panel código ──
        code_frame = ctk.CTkFrame(contenedor, fg_color=COLOR_FONDO, corner_radius=0)
        code_frame.grid(row=0, column=0, sticky="nsew")

        scroll = tk.Scrollbar(code_frame, orient="vertical",
                              bg=COLOR_FONDO, troughcolor=COLOR_FONDO,
                              activebackground="#444")

        self.txt_codigo = tk.Text(
            code_frame,
            bg=COLOR_FONDO, fg=COLOR_TEXTO,
            font=FUENTE_CODE,
            insertbackground=COLOR_VERDE,
            selectbackground="#264f78",
            wrap="none", padx=12, pady=10,
            borderwidth=0, highlightthickness=0, width=1,
            state="disabled",
            yscrollcommand=scroll.set,
        )
        scroll.config(command=self.txt_codigo.yview)
        # scroll.pack(side="right", fill="y")  # Ocultar barra de scroll
        self.txt_codigo.pack(fill="both", expand=True)

        # Tags VS Code Dark+
        self.txt_codigo.tag_config("keyword", foreground=COLOR_KEYWORD, font=FUENTE_CODE)
        self.txt_codigo.tag_config("constant", foreground=COLOR_SELF, font=FUENTE_CODE)
        self.txt_codigo.tag_config("builtin", foreground=COLOR_BUILTIN, font=FUENTE_CODE)
        self.txt_codigo.tag_config("builtin_func", foreground=COLOR_FUNCION, font=FUENTE_CODE)
        self.txt_codigo.tag_config("string", foreground=COLOR_STRING)
        self.txt_codigo.tag_config("comment", foreground=COLOR_COMENTARIO, font=("Consolas", 20, "italic"))
        self.txt_codigo.tag_config("number", foreground=COLOR_NUMERO)
        self.txt_codigo.tag_config("lineno", foreground="#858585", font=("Consolas", 17))
        self.txt_codigo.tag_config("current_line", background=COLOR_LINEA_ACTUAL)
        self.txt_codigo.tag_config("marker", foreground=COLOR_VERDE, font=FUENTE_CODE_BOLD)

        # ── Separador ──
        sep = ctk.CTkFrame(contenedor, fg_color="#3e3e42", width=1, corner_radius=0)
        sep.grid(row=0, column=1, sticky="ns")

        # ── Terminal (derecha — compacta) ──
        term_frame = ctk.CTkFrame(contenedor, fg_color="#1a1a1a", corner_radius=0)
        term_frame.grid(row=0, column=2, sticky="nsew")

        term_header = ctk.CTkFrame(term_frame, fg_color="#2d2d30", height=28, corner_radius=0)
        term_header.pack(fill="x")
        term_header.pack_propagate(False)
        ctk.CTkLabel(term_header, text="> Terminal", text_color=COLOR_VERDE,
                     font=("Consolas", 12, "bold")).pack(side="left", padx=6)

        self.txt_terminal = tk.Text(
            term_frame,
            bg="#1a1a1a", fg=COLOR_VERDE,
            font=FUENTE_TERM,
            wrap="word", padx=6, pady=4,
            borderwidth=0, highlightthickness=0, width=1,
            state="disabled",
        )
        self.txt_terminal.pack(fill="both", expand=True)
        self.txt_terminal.tag_config("info", foreground=COLOR_VERDE)
        self.txt_terminal.tag_config("ok", foreground="#27c93f")
        self.txt_terminal.tag_config("error", foreground=COLOR_ERROR)
        self.txt_terminal.tag_config("warn", foreground=COLOR_STRING)
        self.txt_terminal.tag_config("result", foreground="#aaffaa", font=("Consolas", 15, "bold"))

    def Cargar_Codigo(self, lineas_data, nombre_proyecto="codigo.py"):
        self.lineas_data = lineas_data
        self.linea_actual = -1
        self.lbl_nombre_proyecto.configure(text=f"{nombre_proyecto}.py")

        self.txt_codigo.config(state="normal")
        self.txt_codigo.delete("1.0", "end")

        for i, linea in enumerate(lineas_data):
            num = f" {i+1:>3}  "
            texto = linea["texto"]
            self.txt_codigo.insert("end", num, "lineno")
            self._insertar_con_highlighting(texto, i + 1)
            if i < len(lineas_data) - 1:
                self.txt_codigo.insert("end", "\n")

        self.txt_codigo.config(state="disabled")
        self.Limpiar_Terminal()

    def _insertar_con_highlighting(self, texto, lineno):
        if not texto.strip():
            self.txt_codigo.insert("end", texto)
            return

        # Indice de inicio en Tkinter ("linea.columna")
        # lineno es base 1. Al insertar num línea, ya hay " N  " (7 caracteres)
        start_col = 7 
        
        self.txt_codigo.insert("end", texto)

        # Comentarios → verde itálico
        if texto.strip().startswith("#"):
            idx_sharp = texto.find("#")
            self.txt_codigo.tag_add("comment", f"{lineno}.{start_col + idx_sharp}", f"{lineno}.end")
            return

        # Helper para aplicar tags usando re.finditer
        def aplicar_tag(patron, tag_name):
            for m in re.finditer(patron, texto):
                s, e = m.start(), m.end()
                self.txt_codigo.tag_add(tag_name, f"{lineno}.{start_col + s}", f"{lineno}.{start_col + e}")

        # Strings → naranja (hacer esto antes para no sobreescribir con keywords)
        aplicar_tag(r'"[^"]*"', "string")
        aplicar_tag(r"'[^']*'", "string")

        # Numbers → verde claro
        aplicar_tag(r'\b\d+\.?\d*\b', "number")

        # Keywords, Constantes, Builtins
        for kw in PYTHON_KEYWORDS:
            aplicar_tag(rf'\b{re.escape(kw)}\b', "keyword")

        for c in PYTHON_CONSTANTS:
            aplicar_tag(rf'\b{re.escape(c)}\b', "constant")

        for bi in PYTHON_BUILTINS:
            aplicar_tag(rf'\b{re.escape(bi)}\b', "builtin")

        for bf in PYTHON_BUILTINS_FUNC:
            aplicar_tag(rf'\b{re.escape(bf)}\b', "builtin_func")

    def Resaltar_Linea(self, num_linea):
        self.txt_codigo.config(state="normal")
        self.txt_codigo.tag_remove("current_line", "1.0", "end")
        if num_linea >= 0:
            line_idx = num_linea + 1
            start = f"{line_idx}.0"
            end = f"{line_idx}.end"
            self.txt_codigo.tag_add("current_line", start, end)
            self.txt_codigo.see(start)
        self.linea_actual = num_linea
        self.txt_codigo.config(state="disabled")

    def Log_Terminal(self, mensaje, tipo="info"):
        self.txt_terminal.config(state="normal")
        tag = tipo
        if "[OK]" in mensaje:
            tag = "ok"
        elif "[ERROR]" in mensaje:
            tag = "error"
        elif "[WARN]" in mensaje:
            tag = "warn"
        elif mensaje.startswith("  "):
            tag = "result"
        self.txt_terminal.insert("end", mensaje + "\n", tag)
        self.txt_terminal.see("end")
        self.txt_terminal.config(state="disabled")

    def Limpiar_Terminal(self):
        self.txt_terminal.config(state="normal")
        self.txt_terminal.delete("1.0", "end")
        self.txt_terminal.insert("1.0", "> Sistema listo...\n", "info")
        self.txt_terminal.config(state="disabled")
