import requests
import time

url = "https://yourwebsite"
req_count = 100
sleep_time = 0.01

for i in range(req_count):
	response = requests.get(url)
	print(f"Request {1+i}: Status Code {response.status_code}")
	time.sleep(sleep_time)