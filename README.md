# QR dinámico (gratis) para descargar app iOS/Android

## Qué hace

- El QR apunta a **una URL fija** (tu página `index.html` desplegada).
- Esa página detecta el dispositivo y redirige a:
  - iOS → App Store
  - Android → Google Play
  - Otros → web fallback

## 1) Configurar las URLs

Edita `index.html` y cambia estas 3 variables:

- `APP_STORE_URL`
- `PLAY_STORE_URL`
- `WEB_FALLBACK_URL`

Puedes dejarlo así por ahora aunque aún no tengas las URLs reales.

## 2) Despliegue gratis (elige una)

### Opción A: Netlify (recomendado)

1. Crea una cuenta en Netlify.
2. Arrastra y suelta la carpeta del proyecto.
3. Netlify te dará una URL tipo `https://xxxx.netlify.app`.

Esa URL es la que usas para generar el QR.

### Opción B: GitHub Pages

1. Sube este proyecto a un repositorio.
2. Activa GitHub Pages.
3. Usa la URL pública que te genere.

## 3) Generar el QR

Instala dependencias:

```bash
pip install -r requirements.txt
```

Genera el QR apuntando a tu URL (la del despliegue):

```bash
python generate_qr.py --url "https://TU-URL-FIJA" --out qr.png
```

Imprime `qr.png`.

## 4) Probar

- Abre la URL fija desde un iPhone → debería ir a App Store.
- Abre la URL fija desde Android → debería ir a Google Play.

Cuando tengas las URLs definitivas, actualizas `index.html` y vuelves a desplegar. El QR impreso no cambia.
