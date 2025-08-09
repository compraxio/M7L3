import pyttsx3

def habla(texto: str):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Introducción
habla("""Hola, hoy te hablaré un poco sobre la biblioteca pyttsx3.
Escoge una opción para aprender más.""")

# Menú
escogido = int(input(
    "Elige una opción:\n"
    "1. ¿Qué es pyttsx3?\n"
    "2. Características principales\n"
    "3. Motor (Engine)\n"
    "4. DriverProxy\n"
    "5. Instalación y uso básico\n"
    "6. Personalización de voz\n"
    "7. Ventajas y limitaciones\n"
    "8. Ejemplo práctico\n> "
))

if escogido == 1:
    habla("""pyttsx3 es una biblioteca de Python que convierte texto en voz.
A diferencia de otros servicios de texto a voz, funciona sin conexión a internet y se adapta a diferentes sistemas operativos.
Es muy útil en asistentes virtuales, programas de accesibilidad y narradores automáticos.""")

elif escogido == 2:
    habla("""Características principales:
1. Funciona sin conexión a internet.
2. Compatible con Windows, macOS y Linux.
3. Permite cambiar la voz, velocidad y volumen.
4. Puede guardar el audio generado en un archivo.
5. Fácil de integrar en cualquier proyecto de Python.
6. Soporta múltiples idiomas según las voces instaladas.""")

elif escogido == 3:
    habla("""La clase Engine es la interfaz principal entre la aplicación y el motor de voz.
Gestiona:
- La cola de comandos de voz.
- La configuración como velocidad y volumen.
- El envío de eventos para saber cuándo empieza o termina de hablar.
Se obtiene con pyttsx3.init().""")

elif escogido == 4:
    habla("""DriverProxy es un intermediario entre tu código y el motor de voz real del sistema.
Es como un traductor que convierte tus instrucciones en comandos que el motor entiende.
Normalmente no necesitas manipularlo directamente, pero está detrás de todo el proceso.""")

elif escogido == 5:
    habla("""Para instalar pyttsx3:
Escribe en la terminal: pip install pyttsx3
Uso básico:
import pyttsx3
engine = pyttsx3.init()
engine.say('Hola mundo')
engine.runAndWait()""")

elif escogido == 6:
    habla("""Puedes personalizar la voz con engine.setProperty('voice', id_de_voz)
También puedes cambiar la velocidad con engine.setProperty('rate', valor) y el volumen con engine.setProperty('volume', valor de 0 a 1).
Las voces disponibles dependen de tu sistema.""")

elif escogido == 7:
    habla("""Ventajas:
- Funciona sin internet.
- Multiplataforma.
- Fácil de usar.
Limitaciones:
- Las voces dependen de lo que esté instalado en tu sistema.
- No soporta efectos avanzados como algunos servicios en línea.
- La calidad de voz puede variar según el sistema.""")

elif escogido == 8:
    habla("""Ejemplo práctico:
Puedes usar pyttsx3 para hacer un asistente que lea tus notificaciones, narre un texto o convierta documentos en audio para escucharlos mientras viajas.""")

else:
    habla("Opción no válida.")
