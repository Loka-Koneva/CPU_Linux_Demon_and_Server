import sys
import requests
import time

file_with_data = "./cpu_data.txt"
url_of_server = "http://127.0.0.1:8001/recieve_of_data"

while True:
    try:
        open_file = open (file_with_data, mode="r", encoding="latin-1")
        data_from_file = open_file.read().splitlines()[0]
        print(data_from_file)
        data = {'cpu_data': data_from_file}
        response = requests.get(url_of_server, params = data)
        print (response)
        time.sleep(10)
    except Exception:
        print("Error occuriend during web request")
        print(sys.exc_info()[1])
