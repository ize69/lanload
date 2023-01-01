import time
import requests

def test_network_speed():
    # start the timer
    start_time = time.time()

    # make a request to a large file on a server
    r = requests.get('http://ipv4.download.thinkbroadband.com/1GB.zip')

    # calculate the elapsed time
    elapsed_time = time.time() - start_time

    # calculate the download speed in megabits per second
    speed = len(r.content) * 8 / elapsed_time / 1e6

    # print the download speed
    print(f'Download speed: {speed:.2f} Mbps')