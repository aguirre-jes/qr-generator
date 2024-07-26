import qrcode

# URL que quieres convertir en un código QR
url = "https://jeaguirre-web.vercel.app/"

# Crear una instancia de QRCode
qr = qrcode.QRCode(
    version=1,  # Controla el tamaño del código QR (1 es el más pequeño)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controla el nivel de corrección de errores
    box_size=5,  # Controla el tamaño de cada cuadro del código QR
    border=1,  # Controla el tamaño del borde (número de cuadros)
)

# Añadir la URL al QRCode
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del QRCode
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en un archivo
img.save("images/qrcode.png")