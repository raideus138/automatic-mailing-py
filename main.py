#contraseña = 'foaa vysy lsgp zekj'  
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

servidor_smtp = 'smtp.gmail.com'
puerto_smtp = 587
remitente = 'raivicuna@gmail.com'
contraseña = 'foaa vysy lsgp zekj'

mensaje = MIMEMultipart()
mensaje['From'] = remitente
mensaje['Subject'] = 'correo automatico prueba 1\n 2 remitentes'

cuerpo = 'Contenido del correo'
mensaje.attach(MIMEText(cuerpo, 'plain'))

destinatarios = ['raivicuna@gmail.com', 'ivarquitecto@gmail.com']

with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
    servidor.starttls()
    servidor.login(remitente, contraseña)

    mensaje['To'] = destinatarios[0]
    for destinatario in destinatarios:
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        print(f"Correo enviado a {destinatario}")

print("Todos los correos han sido enviados petee")