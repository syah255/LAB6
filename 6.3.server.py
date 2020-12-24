import socket
import math
import errno
import sys
from multiprocessing import Process


def CALCULATOR(server):
     while True:
            ch = server.recv(1024).decode()
            if ch == '1':
                #add
                a, b = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = float(a) + float(b)

            elif ch == '2':
                #minus
                a, b = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = float(a) - float(b)

            elif ch == '3':
                #times
                a, b = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = float(a) * float(b)

            elif ch == '4':
                #divide
                a, b = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = (float(a)/float(b))

            elif ch == '5':
                #log calculation
                a, b = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = math.log(float(a),float(b))
            elif ch  == '6':
                #SquareRoot calculation
                a = server.recv(1024).decode()
                calc = math.sqrt(float(a))
            elif ch == '7':
                #exponential Calculation
                a, p = [float(i) for i in server.recv(2048).decode('utf-8').split('\n')]
                calc = math.pow(a,p)
            elif ch == '8':
                server.close()
                break
            server.sendall(str(calc).encode())

if __name__ == '__main__':

    S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 55555

    try:
        S.bind((host,port))
    except socket.error as e:
        print (str(e))
        sys.exit()
    S.listen(5)
    while True:
        try:
            server, addr = S.accept()
            print ('\n Sucessfully Connected !! ')

            p = Process(target = CALCULATOR, args=(server,))
            p.start()

        except socket.error:
            print ('an error occurred!')
            print ('an error has occurred!')

    S.close()

