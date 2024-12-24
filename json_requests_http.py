#JSON, Requests, and HTTP methods
import requests

url = 'https://httpbin.org/get'

response = requests.get(url)

print(response) #print http response (200 means OK)

params = response.json() #json parses/converts parameters into dictionary

# params = {
#     'key1': 'val1',
#     'key2': {'embedded_key1': 'embedded val1', 'embedded_key2': 'embedded val2'}
#     }

for index, (key, value) in enumerate(params.items()):
    print(f"Index: {index} -- Key: {key} -- Value: {value}")
    
    if isinstance(value, dict): #checks if value is a dict
        print(f"Embedded Dictionary ---> {value}")
        for i, (k, v) in enumerate(value.items()):
            print(f"INNER | Index: {i} -- Key: {k} -- Value: {v}")


