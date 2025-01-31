import smtplib

def enviar():
    # Datos
    sender = "lawyernews.avm@gmail.com"
    password = "ydqexjkllgdcxvcx"
    receiver = "hepagoes@gmail.com"

    # Configurar SMTP
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender, password)

    # Abrir respuesta de IA
    fAI = open("./files/ai.txt", 'r')
    message = fAI.read().encode("UTF-8")
    fAI.close()

    # Enviar Correo
    s.sendmail(sender, receiver, message)

    s.quit()