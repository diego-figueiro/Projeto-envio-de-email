import os
import smtplib
from email.message import EmailMessage
from segredos import senha

# Configurar email, senha
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = senha

# Criar um e-mail
msg = EmailMessage()
msg["Subject"] = "Teste: Enviando email via Python"
msg["From"] = ""
msg["To"] = ""
msg.set_content(
    "Este email foi enviado através do Python, guia de como reproduzir pode ser encontrado aqui: https://www.youtube.com/watch?v=pJP6ruTiKX4")

# Enviar um e-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
