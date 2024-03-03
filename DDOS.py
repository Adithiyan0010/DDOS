import requests
import time

def send_request(url, num_requests):
    requests_sent = 0
    start_time = time.time()
    while requests_sent < num_requests:
        try:
            response = requests.get(url)
            print(f"Request sent to {url}. Status code: {response.status_code}")
            requests_sent += 1
        except Exception as e:
            print(f"Error sending request to {url}: {e}")
    end_time = time.time()
    print(f"Sent {requests_sent} requests to {url} in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    num_requests = int(input("Enter the number of requests: "))
    send_request(url, num_requests)