import http.client
import base64


KEY_LENGTH = 16  # AES128



def is_padding_ok(data):
  url = 'project-2.csec.chatzi.org'
  port = 8000

  string="admin:"+data.hex()

  bstring=base64.b64encode(string.encode()).decode()

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
      print("retrying")


if __name__ == '__main__':
	#print("decrypted message:", _decrypt( ciphertext ) )
	print("USE attack.py!!")