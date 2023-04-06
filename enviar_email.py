import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'seu-email@exemplo.com'
smtp_password = 'sua-senha'

# Cria uma mensagem de email
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = 'destinatario@exemplo.com'
msg['Subject'] = 'Assunto do email'

# Adiciona o conteúdo do email
texto = 'Olá, este é um email de teste enviado através de Python!'
msg.attach(MIMEText(texto, 'plain'))

# Conecta ao servidor SMTP e envia o email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'destinatario@exemplo.com', msg.as_string())

print('Email enviado com sucesso!')
