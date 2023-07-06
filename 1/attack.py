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
    print('Error:', response.headers)
