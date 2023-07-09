from Crypto.Cipher import AES
from Crypto import Random
mode = AES.MODE_CBC
import http.client
import base64


KEY_LENGTH = 16  # AES128
BLOCK_SIZE = AES.block_size


def is_padding_ok(data):
  url = 'project-2.csec.chatzi.org'
  port = 8000

  string="admin:"+data.hex()

  bstring=base64.b64encode(string.encode()).decode()
  print(bstring)

  while True:
    try:
      conn = http.client.HTTPConnection(url, port)

      headers = {
          'Authorization': 'Basic '+ bstring,
          'Content-Type': 'application/json'
      }

      body = {}
      conn.request('POST', '/', headers=headers, body=body)
      response = conn.getresponse()
      if response.status == 500:
        return False
      else:
        return True
    except:
      time.sleep(1)


if __name__ == '__main__':
	#print("decrypted message:", _decrypt( ciphertext ) )
	print("USE attack.py!!")