import socket
import os
import sys

clientSocket = socket.socket()
host = '192.168.56.108'
port = 8888
buffer = 1024
SEPARATOR='<SEPARATOR>'

try:
    clientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

print("Enter a file to upload")
filename = input('Filename:')

try:
   f= open (filename,"aa")
except FileNotFoundError:
   print("File not found!") 

filesize = os.path.getsize(filename)
print('File size:',filesize,'bytes')
clientSocket.send(f'{filename}{SEPARATOR}{filesize}'.encode())
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

for _ in progress:

 data=f.read(buffer)
 clientSocket.sendall(data)
 progress.update(len(data))

print('Upload File Finished')
f.close()
clientSocket.close()
