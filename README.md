# 🎣 Fish-Control-Pro (BlueStacks 5 Edition)

Script de automatización de alta precisión para minijuegos de pesca, optimizado para entornos de emulación y diseñado para sobrevivir a los peces más agresivos mediante un sistema de control de inercia.

---

## 🚀 Requisitos de Ejecución (Configuración Probada)

Para que las coordenadas y la detección funcionen correctamente, el entorno debe cumplir estrictamente con:

* **Emulador:** [BlueStacks 5]([https://www.bluestacks.com/es/bluestacks-5.html](https://cloud.bluestacks.com/api/getdownloadnow?platform=win&win_version=10&mac_version=&client_uuid=d7232e59-2796-4c29-a270-da49a4319c4c&app_pkg=&platform_cloud=%257B%2522description%2522%253A%2522Opera%2520129.0.0.0%2520(like%2520Chrome%2520145.0.0.0)%2520on%2520Windows%252010%252064-bit%2522%252C%2522layout%2522%253A%2522Blink%2522%252C%2522manufacturer%2522%253Anull%252C%2522name%2522%253A%2522Opera%2522%252C%2522prerelease%2522%253Anull%252C%2522product%2522%253Anull%252C%2522ua%2522%253A%2522Mozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F145.0.0.0%2520Safari%252F537.36%2520OPR%252F129.0.0.0%2520(Edition%2520std-1)%2522%252C%2522version%2522%253A%2522129.0.0.0%2522%252C%2522os%2522%253A%257B%2522architecture%2522%253A64%252C%2522family%2522%253A%2522Windows%2522%252C%2522version%2522%253A%252210%2522%257D%257D&preferred_lang=es&utm_source=&utm_medium=&gaCookie=GA1.1.1693913854.1776197243&gclid=&clickid=&msclkid=&affiliateId=&offerId=&transaction_id=&aff_sub=&first_landing_page=https%253A%252F%252Fwww.bluestacks.com%252Fes%252Fbluestacks-5.html&referrer=&download_page_referrer=https%3A%2F%2Fwww.bluestacks.com%2Fes%2Findex.html&utm_campaign=homepage-dl-button-es&user_id=experiment_variant&exit_utm_campaign=bsx-install-button-home-es&incompatible=false&bluestacks_version=bs5&device_memory=8&device_cpu_cores=12&extra_data=%7B%22campainId%22%3A%226994a31d90096b001b1653cf%22%2C%22deviceDetails%22%3A%22windows%22%2C%22renderer%22%3A%22ANGLE%20(Microsoft%2C%20Microsoft%20Basic%20Render%20Driver%20(0x0000008C)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%7D)).
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

* ALTURA_BARRA_Y
