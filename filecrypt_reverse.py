import base64
from Crypto.Cipher import ARC4

msg = 'MzU5OThmZGI3ZmUzYjc5NDBiOTM3NWE2OGE2NTRmZjk0OWM1OGRjYjliMWFlYmIwNDhkNmFhNzRkOTA1YjdiMGM2ZTA0YjQwNGViNjExMjlmOTJhZDkxMjcwMzg1MDIwMTU4MmNlMzllNzdiZmU3MzlmZWM1Mjg3NDFiMjAyZjg5MjNhOWY4ZDYzMDM2MTdkOGU2ZTM1YTBkNjQ0MTE1ZTIzODUyMmM2ZDBjYWNkMWFmZGFlMjMwNTA0NTJjOTk4ZTM5YQ=='
msg = base64.b64decode(msg)
khash = msg[:40]
msg = msg[40:]
cipher = ARC4.new(khash.decode('hex'))
msg = cipher.decrypt(msg.decode('hex'))

#print msg

msgarr = msg.split('&')

id = msgarr[0].split('=')[1]
key = msgarr[1].split('=')[1]
iv = msgarr[2].split('=')[1]

id = id.decode('hex')
key = key.decode('hex')
iv = iv.decode('hex')

n = hex(ord(id) + 16)
iv = ('').join((chr(ord(y) ^ int(n, 16)) for y in iv))
key = ('').join((chr(ord(x) ^ int(n, 16)) for x in key))

print key + iv