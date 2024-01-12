import requests
import time


# Create decoration function which counts duration of "get request"
def request_time_counter(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Your request was processed in {end-start} seconds')
    return wrapper


# Dcorate function which makes "get request"
@request_time_counter
def youtube_request():
    response = requests.get('https://www.youtube.com')
    return response.text


youtube_request()
