from openai import OpenAI
import re

def resumir():
    # Inicializar LM Studio
    client = OpenAI(
        base_url="http://127.0.0.1:1234/v1",
        api_key="lm-studio"
    )
    MODEL = "deepseek-r1-distill-qwen-7b"

    # Preparar prompt
    fNews = open("./files/news.txt", "r")
    fStocks = open("./files/stocks.txt", "r")
    prompt = "news = " + fNews.read() + "; stocks = " + fStocks.read()

    fNews.close()
    fStocks.close()

    # Preparar conversación
    conversation = [
        {"role": "system", "content":"You will summarize the financial news and stock market updates the user gives you. Don't say that you are doing a summary. Be fast in your response, only delve into each idea for 1 sentence in your thoughts. Do it in a list format."},
        {"role": "user", "content":prompt}
    ]

    # OpenAI
    completion = client.chat.completions.create(
        model=MODEL,
        messages=conversation,
    )

    # Guardar texto generado
    generation = completion.choices[0].message.content
    cleaned_generation = re.sub(r'<think>.*?</think>', '', generation, flags=re.DOTALL)

    fAI = open("./files/ai.txt", 'w')
    fAI.write(cleaned_generation.strip())
    fAI.close()