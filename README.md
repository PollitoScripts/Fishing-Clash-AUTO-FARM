# 🎣 Fish-Control-Pro (BlueStacks 5 Edition)

Script de automatización de alta precisión para minijuegos de pesca, optimizado para entornos de emulación y diseñado para sobrevivir a los peces más agresivos mediante un sistema de control de inercia.

---

## 🚀 Requisitos de Ejecución (Configuración Probada)

Para que las coordenadas y la detección funcionen correctamente, el entorno debe cumplir estrictamente con:

* **Emulador:** [BlueStacks 5](https://www.bluestacks.com/es/bluestacks-5.html).
* **Resolución de Pantalla:** 1920x1080 (FHD).
* **Modo de Visualización:** Pantalla Completa (**F11**).
* **Permisos:** Es **obligatorio** ejecutar tanto el script de Python como el emulador **como Administrador**.

---

## ✨ Características Técnicas

* **Control de Inercia Adaptativo:** El bot aplica un frenado predictivo antes del objetivo para compensar la física del juego.
* **Detección de Bajo Nivel:** Optimizado para ignorar cambios de iluminación (funciona con indicadores azules, rojos y oscuros).
* **Escaneo Inverso:** Analiza la barra de derecha a izquierda para detectar el peligro de rotura antes que cualquier otra cosa.
* **Muro de Seguridad:** Bloqueo automático de tensión al alcanzar el límite crítico (980px).

---

## 🛠️ Instalación y Uso

1. **Instalar dependencias:**
   ```bash
   pip install pyautogui keyboard pynput pillow
* Abrir BlueStacks 5 en 1080p.

* Pulsar F11 (Pantalla completa).

* Ejecutar el script (VSCode o Terminal) como Administrador.

* Usar F6 para encender/apagar el bot.

## 💡 Nota sobre las Coordenadas
El script utiliza coordenadas fijas para 1920x1080. Si cambias la resolución, ajusta estas variables, y sacas nuevas fotos:

* LIMITE_IZQUIERDO_X

* LIMITE_DERECHO_X

ALTURA_BARRA_Y
