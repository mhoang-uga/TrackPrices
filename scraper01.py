import requests #get data from URL
from  bs4 import BeautifulSoup
import smtplib #sending email
import time

isOn = True
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
URL = input("Input Amazon Link: ")
checkPrice = float(input("Input price you want to get: "))
timeDone = float(input("Input time you want to check (in hour): "))

def check_price():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    title = soup2.find(id="productTitle").get_text();
    price = soup2.find(id="priceblock_ourprice").get_text();
    converted_price = float(price[1]+price[3:6])
    print(converted_price)
    print(title.strip())

    if (converted_price < checkPrice):
        send_mail()
        isOn = False;

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #command send by an email server to send email
    server.starttls() #encrypr connection
    server.ehlo()

    server.login('minhhoang040597@gmail.com','tfvtiqfnznqrkhdy')

    subject = 'Price fell down!'
    body = 'Check Amazon Link: ' + URL

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('minhhoang040597@gmail.com', 'minhhoang040597@gmail.com', msg)
    print('EMAIL SENT')

    server.quit()

#Call the function
count =0;
while (isOn & count < timeDone):
    check_price()
    time.sleep(60*60) #check per hour
    count+=1