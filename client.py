import sys
import time
import psutil
import requests
import daemonize


def add_information_cpu(url, cpu_percent):
    requests.post(url, data={'load_cpu': cpu_percent})


def main():
    url = 'http://127.0.0.1:'
    if len(sys.argv) == 2:
        url += sys.argv[1]
    else:
        url += '8001'
    url += '/information_cpu/add_information_cpu'
    limit = 10
    while True:
        add_information_cpu(url, psutil.cpu_percent())
        time.sleep(limit)


if __name__ == "__main__":
    daemon = daemonize.Daemonize(app='collection_system', pid='pid_file.pid', action=main)
    daemon.start()

