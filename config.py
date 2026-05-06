# ══════════════════════════════════════════════
# Config - Constantes de diseño (VS Code Dark+)
# SENATI - Visión Computacional
# ══════════════════════════════════════════════

# ── Colores base (oscuro terminal) ──
COLOR_FONDO = "#1e1e1e"
COLOR_PANEL = "#252526"
COLOR_BORDE = "#2d2d30"
COLOR_VERDE = "#39FF14"
COLOR_VERDE_DIM = "#1a5a1a"
COLOR_TEXTO = "#d4d4d4"

# ── Colores syntax (VS Code Dark+) ──
COLOR_KEYWORD = "#c586c0"       # Rosa/púrpura (import, for, if, with)
COLOR_BUILTIN = "#4ec9b0"       # Teal (cv2, torch, YOLO)
COLOR_STRING = "#ce9178"        # Naranja cálido
COLOR_COMENTARIO = "#6a9955"    # Verde suave
COLOR_NUMERO = "#b5cea8"        # Verde claro
COLOR_FUNCION = "#dcdcaa"       # Amarillo (print, len)
COLOR_VARIABLE = "#9cdcfe"      # Azul claro
COLOR_SELF = "#569cd6"          # Azul (self, True, False)
COLOR_OPERADOR = "#d4d4d4"      # Gris claro

# ── Colores UI ──
COLOR_LINEA_ACTUAL = "#264f26"
COLOR_BOTON = "#0f1f0f"
COLOR_BOTON_HOVER = "#1a3a1a"
COLOR_ERROR = "#f44747"
COLOR_EXITO = "#39FF14"

# ── Fuentes (grandes para proyector) ──
FUENTE_MONO = ("Consolas", 16)
FUENTE_MONO_GRANDE = ("Consolas", 17)
FUENTE_TITULO = ("Consolas", 24, "bold")
FUENTE_TAB = ("Consolas", 13, "bold")
FUENTE_DESC = ("Consolas", 20)
FUENTE_TERMINAL = ("Consolas", 14)
FUENTE_BOTON = ("Consolas", 16, "bold")

# ── Dimensiones ──
ANCHO_VENTANA = 1500
ALTO_VENTANA = 850
TAMANO_IMAGEN = (500, 380)

# ── Keywords Python para syntax highlighting ──
PYTHON_KEYWORDS = [
    "import", "from", "as", "def", "class", "return",
    "for", "in", "if", "else", "elif", "with", "try",
    "except", "raise", "not", "and", "or", "is",
    "while", "pass", "break", "continue", "yield",
    "lambda", "global", "del", "assert",
]

PYTHON_CONSTANTS = [
    "True", "False", "None",
]

PYTHON_BUILTINS_FUNC = [
    "print", "len", "int", "float", "map", "range",
    "str", "list", "dict", "tuple", "type", "open",
    "enumerate", "zip", "sorted", "super", "self",
]

PYTHON_BUILTINS = [
    "cv2", "torch", "np", "YOLO", "Image",
    "transforms", "models", "nn", "F",
    "deeplabv3_resnet50", "genai", "types",
]
