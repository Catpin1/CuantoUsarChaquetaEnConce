import requests
import smtplib
from email.mime.text import MIMEText


api_key = "********clave API openweather"#añade tu clave otorgada por openwather
ciudad = "Concepcion,CL"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"


respuesta = requests.get(url)
datos_clima = respuesta.json()

if datos_clima["cod"] == 200:
    # Extraer datos relevantes
    temperatura = datos_clima['main']['temp']
    descripcion = datos_clima['weather'][0]['description']
    print(f"El clima en {ciudad} es {temperatura}°C con {descripcion}.")

    if temperatura < 12:
        print("Usa chaqueta")
        
    
        sender_email = "**********@gmail.com"  #añade tu correo
        sender_password = "****************" #añade una clave de aplicacion por google
        recipient_email = "********@gmail.com" #correo destinatario de notificacion

        subject = "Recomendación para tropiconce"
        body = f"La temperatura actual en {ciudad} es {temperatura}°C. ¡USA CHAQUETA!"
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        print("Correo enviado con éxito.")
    else:
        print("No uses chaqueta.")
else:
    print("Error al obtener datos del clima:", datos_clima["message"])

    
    
