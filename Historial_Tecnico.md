# Historial Técnico

## Estado
- App v10 (Release Final)
- Panel izquierdo de imagen más compacto (ancho 480).
- YOLO: Grosor de cajas reducido al mínimo (`line_width=1`) y output resumido por conteo.
- TTS: Límite de tiempo ampliado a 45s (soporta respuestas largas de Gemma) y sintaxis hablada optimizada con pausas (,).
- Terminal ultra compacta y sin scrollbar.

## Completado
- [x] Reducido en 20% el ancho del panel izquierdo (de 600px a 480px), ajustando también el `wraplength` de los textos.
- [x] Modificado `Procesar_Yolo()` para dibujar cajas más finas y retornar un conteo resumido (ej. "2 auto(s), 3 persona(s)") en vez de la lista cruda de probabilidades por cada objeto.
- [x] Aumentado el `timeout` de PowerShell SAPI de 10s a 45s para que la voz no se corte a medio camino en descripciones largas (Gemma).
- [x] Agregadas comas `,` a los arrays de salida de CNN, ViT y YOLO para que el sintetizador de voz haga pausas naturales al leer los resultados.

## Pendiente
- [ ] Exposición final
