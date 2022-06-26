import socket
import sys
import time
import errno
import math
from multiprocessing import Process

def process_start(s_sock):
    while True:
      s_sock.send(str.encode('\n\n    *****Welcome to Hazim Calculator**** \n Choose an operation [1-Exp | 2-Sqrt | 3-Log]\n\n Choose your number:'))
      
      while True:
        data = s_sock.recv(2048)
        data = data.decode('utf-8')
        print(data)
        if not data:
             break

        elif data == '1':
            
             s_sock.send(str.encode(' Enter a number:'))
             number = s_sock.recv(2048)
             number = int(number)
             number = str(math.exp(number))
             print(number)
             s_sock.send(str.encode('\n Answer:'+ number + '\n Press ENTER to continue.'))

        elif data == '2':
             s_sock.send(str.encode(' Enter a number:'))
             number = s_sock.recv(2048)
             number = int(number)
             number = str(math.sqrt(number))
             print(number)
             s_sock.send(str.encode('\n Answer:'+ number + '\n Press ENTER to continue'))

        elif data == '3':
             s_sock.send(str.encode(' Enter a number:'))
             number = s_sock.recv(2048)
             number = int(number)
             number = str(math.log(number))
             print(number)
             s_sock.send(str.encode('\n Answer:'+ number + '\n Press ENTER to continue'))

        else:
             s_sock.send(str.encode('\n Failed! The operation is not available.\n Press ENTER to continue.')) 
        break
       
    s_sock.close()
      

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('Socket error')

    except Exception as e:        
                print('An exception occurred!')
                print(e)
                sys.exit(1)
    finally:
     	   s.close()
