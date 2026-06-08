import argparse

import qrcode


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url",
        required=True,
        help="URL fija del endpoint/página (ej: https://tu-dominio.com/app-descarga)",
    )
    parser.add_argument(
        "--out",
        default="qr_descarga_app.png",
        help="Archivo de salida PNG",
    )
    args = parser.parse_args()

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(args.url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(args.out)


if __name__ == "__main__":
    main()
