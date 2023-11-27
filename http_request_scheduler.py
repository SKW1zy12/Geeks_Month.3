import schedule
import time
import requests
import argparse

def perform_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Request to {url} successful. Response: {response.text}")

    except:
        pass

def job(url):
    perform_request(url)

def main():
    parser = argparse.ArgumentParser(description='HTTP Request Scheduler')
    parser.add_argument('url', type=str, help='URL for HTTP request')
    parser.add_argument('initial_delay', type=int, help='Initial delay in seconds')
    parser.add_argument('interval', type=int, help='Interval between requests in seconds')
    args = parser.parse_args()

    schedule.every(args.initial_delay).seconds.do(job, args.url).tag('initial_delay_request')
    schedule.every(args.interval).seconds.do(job, args.url).tag('interval_request')

    print(f"HTTP Request Scheduler started for {args.url}. Press Ctrl+C to exit.")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped by the user.")

if __name__ == "__main__":
    main()
