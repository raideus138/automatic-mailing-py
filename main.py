#contraseña = 'foaa vysy lsgp zekj'  
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

emails = []
total = 0
def ece(archivo_excel, nombre_columna):
    try:
        df = pd.read_excel(archivo_excel)
        columna = df[nombre_columna].tolist()
        return columna
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return None

servidor_smtp = 'smtp.gmail.com'
puerto_smtp = 587
remitente = 'raivicuna@gmail.com'
contraseña = 'foaa vysy lsgp zekj'

archivo_excel = 'C:/Users/raivi/OneDrive/Desktop/4554/LIBROGMAILS.xlsx'
nombre_columna = 'GMAILS'

contenido_columna = ece(archivo_excel, nombre_columna)

if contenido_columna:
    print(f"Contenido de la columna '{nombre_columna}':")
    for elemento in contenido_columna:
        emails.append(elemento)
else:
    print("No se pudo extraer el contenido de la columna.")

mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['Subject'] = 'correo automático prueba 1, 2 remitentes'

cuerpo = 'Contenido del correo'
mensaje.attach(MIMEText(cuerpo, 'plain'))

destinatarios = emails

with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
    servidor.starttls()
    servidor.login(remitente, contraseña)

    mensaje['To'] = destinatarios[0]
    for destinatario in destinatarios:
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        print(f"Correo enviado a {destinatario}")
        total=+1
print(f"Todos los correos han sido enviados correctamente. Se enviaron {total} correos.")