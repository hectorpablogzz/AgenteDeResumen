from bs4 import BeautifulSoup
import requests

def leerPagina():
    page_to_scrape = requests.get("https://finance.yahoo.com/")

    print(page_to_scrape)

    soup = BeautifulSoup(page_to_scrape.content, "html.parser")

    # Extraer noticias
    news = soup.find('article', class_='gridLayout yf-cfn520')

    fNews = open("./files/news.txt", "w")
    fNews.write(news.text)
    fNews.close()

    #Extraer Stocks
    stocks = soup.find('div', class_='body yf-1s23uaf')

    fStocks = open("./files/stocks.txt", "w")
    fStocks.write(stocks.text)
    fStocks.close()

