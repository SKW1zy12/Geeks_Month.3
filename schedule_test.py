import schedule
import time 
import requests

def job():
    print("Working....", time.ctime())

def  notification_lesson_12_2b():
    print("Здраствуйте, сеодня у вас урок в 16:40")

def current_btc_price():
    url = 'https://www.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    response = requests.get(url=url).json()
    print(response)

    with open('btc_log.txt', 'a') as file:
            file.write(f"{time.ctime()}: BTC Price - {response['price']}\n")


schedule.every(1).minutes.do(current_btc_price)




# schedule.every(2).seconds.do(job)
# schedule.every(1).minutes.do(job)
# schedule.every().saturday.at("16:24").do(job)
# schedule.every().saturday.at("16:27").do(notification_lesson_12_2b)
# schedule.every().saturday.at("16:29", 'Asia/Bishkek').do(notification_lesson_12_2b)
# schedule.every(4).saturday.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)