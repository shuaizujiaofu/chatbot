import json
import requests

headers = {'Content-Type': 'application/json'}
datas = json.dumps({"param1": "Detector", "param2": "cnblogs"})
r = requests.post("http://httpbin.org/post", data=datas, headers=headers)
print(r.text)