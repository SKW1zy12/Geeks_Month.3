import requests
import schedule
import time

def perform_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('url_log.txt', 'a+', encoding='utf-8') as file:
            file.write(response.text + '\n')
    else:
        pass

def main():
    url = 'https://www.cybersport.ru/matches?date=future'
    schedule.every(1).minutes.do(perform_request, url)
    schedule.every(1).minutes.do(perform_request, url)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
        main()

