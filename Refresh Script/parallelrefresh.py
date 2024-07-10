import requests

import time

import threading



url = "https://yourwebsite"  #Replace this URL with your own site 

requests_count = 100  # Specifies how many requests will be made

sleep_time = 0.01  # Wait time (in seconds)



def send_request():

    for i in range(requests_count):

        response = requests.get(url)

        print(f"Request {i+1}: Status Code {response.status_code}")

        time.sleep(sleep_time)



# Use threading to send requests in parallel

threads = []

for _ in range(10):  # For example use 10 parallel threads

    thread = threading.Thread(target=send_request)

    threads.append(thread)

    thread.start()



# Wait for all threads to complete

for thread in threads:

    thread.join()