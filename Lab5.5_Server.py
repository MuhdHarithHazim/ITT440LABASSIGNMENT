import socket
import os
import sys
  
ServerSocket = socket.socket()
host = '192.168.56.106'
port = 8888
buffer = 1024
SEPARATOR = "<SEPARATOR>"


try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)
print('File Server')
print('-----------')

while True:

    client, addr = ServerSocket.accept()
    print ('Connection from ' + str(addr))
    received=client.recv(buffer).decode()
	
    filename,filesize= received.split(SEPARATOR)
    filesize=int(filesize)

    progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename,"wb") as f:
      for _ in progress:

        data=client.recv(buffer)
        f.write(data)

        progress.update(len(data))
    f.close()
    print('File have been store')

client.close()
