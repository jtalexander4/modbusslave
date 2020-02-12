import requests
import json
from pprint import pprint
import threading
import random

config_file = "IPC.json"

with open(config_file) as json_file:
    data = json.load(json_file)
    registers = data["slaves"]["1"]["registers"]
    register_list = list(registers.keys())
        

def post_request():
    threading.Timer(5.0, post_request).start()
    for register in register_list:
        register_number = int(register[2:])
        new_register_number = register_number - 1
        new_register_string = "HR" + str(new_register_number)
        new_value = random.randint(1, 10)

        ## POST Request Actions
        url = "http://localhost:9000/slaves/1/registers/{}".format(new_register_string)
        payload = "{\n    \"value\": " + "{}".format(new_value) + "\n}"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data = payload)
        # print(response.text.encode('utf8'))
    

post_request()
