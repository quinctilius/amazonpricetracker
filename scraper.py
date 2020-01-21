import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/AMD-Ryzen-3600-Processor-Cache/dp/B07STGGQ18/ref=sr_1_1?crid=38SX72ROF3Q12&keywords=ryzen+5+3600&qid=1579581916&sprefix=ryzen+5+%2Caps%2C226&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:7])

    if(converted_price < 160.00):
        send_mail()

    print(converted_price)

    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('EMAIL LOGIN HERE', 'APP PASSWORD HERE')
    subject = 'Ryzen 3500 Price update'
    body = 'The Ryzen 3500 Price has fallen, click https://www.amazon.co.uk/AMD-Ryzen-3600-Processor-Cache/dp/B07STGGQ18/ref=sr_1_1?crid=38SX72ROF3Q12&keywords=ryzen+5+3600&qid=1579581916&sprefix=ryzen+5+%2Caps%2C226&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'SENDER EMAIL',
        'RECEIVING EMAIL',
        msg
    )
    print('Email has been sent')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)    #Checking every day

