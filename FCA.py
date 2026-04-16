import pyautogui
import time
import keyboard
import os
from pynput.mouse import Button, Controller as MouseController
from PIL import ImageGrab

mouse = MouseController()
CONFIDENCE = 0.7
HOTKEY_ACTIVACION = 'f6'
TECLA_ESPACIO = 'space'

LIMITE_IZQUIERDO_X = 850
LIMITE_DERECHO_X = 1060
OBJETIVO_X = 957
ALTURA_BARRA_Y = 130

# --- ZONAS DE COMPORTAMIENTO ---
# Si la barra está aquí, actuamos agresivamente
ZONA_PELIGRO_IZQ = OBJETIVO_X - 80   # < 877 → pulsar fuerte
ZONA_PELIGRO_DER = OBJETIVO_X + 60   # > 1017 → soltar inmediato
# Zona de confort: no hacer nada brusco, solo tapping suave
ZONA_CONFORT_IZQ = OBJETIVO_X - 25   # 932
ZONA_CONFORT_DER = OBJETIVO_X + 20   # 977

# Duración del tap cerca del objetivo (ms)
TAP_CERCA_MS = 0.055
TAP_LEJOS_MS = 0.12

def obtener_ruta(nombre_archivo):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), nombre_archivo)

def localizar(nombre_imagen):
    try:
        return pyautogui.locateCenterOnScreen(obtener_ruta(nombre_imagen), confidence=CONFIDENCE)
    except:
        return None

def escanear_barra():
    """Devuelve la posición X absoluta del marcador, o 0 si no lo encuentra."""
    ancho = LIMITE_DERECHO_X - LIMITE_IZQUIERDO_X
    try:
        img = ImageGrab.grab(bbox=(LIMITE_IZQUIERDO_X, ALTURA_BARRA_Y, LIMITE_DERECHO_X, ALTURA_BARRA_Y + 1))
        for x in range(0, ancho, 2):
            r, g, b = img.getpixel((x, 0))
            if r < 120 and g < 120:
                return LIMITE_IZQUIERDO_X + x
    except:
        pass
    return 0

def minijuego_tension():
    print(">>> PELEANDO PEZ...")
    presionado = False
    pos_anterior = 0
    velocidad = 0
    t_fin = time.time() + 20
    fallo_deteccion = 0

    while time.time() < t_fin:
        pos = escanear_barra()

        # --- DETECCIÓN FALLIDA ---
        if pos == 0:
            fallo_deteccion += 1
            # Tras 5 fallos seguidos, tap corto para evitar que se hunda
            if fallo_deteccion >= 5:
                if not presionado:
                    keyboard.press(TECLA_ESPACIO)
                    time.sleep(0.04)
                    keyboard.release(TECLA_ESPACIO)
                fallo_deteccion = 0
            time.sleep(0.02)
            continue

        fallo_deteccion = 0

        # --- VELOCIDAD (positiva = va a la derecha) ---
        if pos_anterior != 0:
            velocidad = pos - pos_anterior
        pos_anterior = pos

        # --- POS PROYECTADA: dónde estará en ~2 frames si sigue así ---
        pos_proyectada = pos + (velocidad * 2)

        # ============================================================
        # LÓGICA DE CONTROL
        # ============================================================

        # 1. PELIGRO DERECHA: soltar YA, sin excepciones
        if pos > ZONA_PELIGRO_DER or pos_proyectada > ZONA_PELIGRO_DER:
            if presionado:
                keyboard.release(TECLA_ESPACIO)
                presionado = False

        # 2. PELIGRO IZQUIERDA: pulsar YA
        elif pos < ZONA_PELIGRO_IZQ or pos_proyectada < ZONA_PELIGRO_IZQ:
            if not presionado:
                keyboard.press(TECLA_ESPACIO)
                presionado = True

        # 3. ZONA DE CONFORT: tapping controlado según velocidad y posición
        else:
            # Siempre soltamos primero para operar en modo tap
            if presionado:
                keyboard.release(TECLA_ESPACIO)
                presionado = False

            # Si está a la izquierda del objetivo O se mueve hacia la izq → tap
            if pos < OBJETIVO_X or velocidad < -1:
                duracion = TAP_CERCA_MS if abs(pos - OBJETIVO_X) < 15 else TAP_LEJOS_MS
                keyboard.press(TECLA_ESPACIO)
                time.sleep(duracion)
                keyboard.release(TECLA_ESPACIO)
                time.sleep(0.03)  # pequeña pausa para no sobre-corregir

            # Si está a la derecha y va hacia la derecha → no hacer nada (dejar caer)
            # (no pulsar es la acción correcta aquí)

        # --- COMPROBAR FIN DEL MINIJUEGO (cada ~10 frames para no perder tiempo) ---
        if int(time.time() * 20) % 10 == 0:
            if localizar('RECOGER.png') or localizar('RECOGER2.png'):
                break

        time.sleep(0.016)  # ~60 lecturas/seg, no quemar CPU

    if presionado:
        keyboard.release(TECLA_ESPACIO)
    print(">>> Minijuego terminado.")


# --- BUCLE PRINCIPAL (sin cambios) ---
bot_encendido = False

def toggle_bot():
    global bot_encendido
    bot_encendido = not bot_encendido
    print(f"\n[!] BOT {'ENCENDIDO' if bot_encendido else 'APAGADO'}")

keyboard.add_hotkey(HOTKEY_ACTIVACION, toggle_bot)

while True:
    if bot_encendido:
        p_lanzar = localizar('LANZAR.png')
        if p_lanzar:
            pyautogui.click(p_lanzar.x, p_lanzar.y)
            time.sleep(1.5)

        p_pescar = localizar('PESCAR.png')
        if p_pescar:
            pyautogui.click(p_pescar.x, p_pescar.y)
            time.sleep(0.2)
            minijuego_tension()

            intentos_limpieza = 0
            while intentos_limpieza < 20:
                if localizar('LANZAR.png'): break
                p_rec = localizar('RECOGER.png') or localizar('RECOGER2.png')
                p_omi = localizar('OMITIR_ANIMACION.png')
                p_tod = localizar('RECOGERLAS_TODAS.png')
                p_cru = localizar('CRUZ.png')
                
                if p_rec:
                    print("¡RECOGER o RECOGER2 Encontrada! Intentando hacer click...")
                    pyautogui.click(p_rec.x, p_rec.y)
                    time.sleep(1.5)
                elif p_omi:
                    print("¡OMITIR_ANIMACION Encontrada! Intentando hacer click...")
                    pyautogui.click(p_omi.x, p_omi.y)
                    time.sleep(1.2)
                elif p_tod:
                    print("¡RECOGERLAS_TODAS Encontrada! Intentando hacer click...")
                    pyautogui.click(p_tod.x, p_tod.y)
                    time.sleep(1.5)
                elif p_cru:
                    print("¡Cruz Encontrada! Intentando hacer click...")
                    pyautogui.click(p_cru.x, p_cru.y)
                    time.sleep(1.5)
               
                intentos_limpieza += 1
                time.sleep(0.5)
    time.sleep(0.2)