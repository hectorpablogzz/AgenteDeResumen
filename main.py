import schedule
import time
# archivos locales
import ai
import mail
import scraper

def instrucciones():
    print("Leyendo página web...")
    scraper.leerPagina()

    print("Resumiendo con IA...")
    #ai.resumir()

    print("Enviando correo...")
    mail.enviar()

    print("Terminado.")

instrucciones()

# repetir despues de intervalo
schedule.every(60).minutes.do(instrucciones)

while True:
    schedule.run_pending()
    time.sleep(1)

