import sys
import time
import psutil
import requests


def add_information_cpu(url, cpu_percent):
    requests.post(url, data={'load_cpu': cpu_percent})


def main():
    url = 'http://127.0.0.1:'
    limit = 10
    if len(sys.argv) == 2:
        url += sys.argv[1]
    else:
        url += '8001'
    url += '/information_cpu/add_information_cpu'
    while True:
        add_information_cpu(url, psutil.cpu_percent())
        print('save')
        time.sleep(limit)


if __name__ == "__main__":
    main()
