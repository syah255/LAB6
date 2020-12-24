import socket
import sys

Client = socket.socket()
host = '192.168.1.20'
port = 55555

try:
    Client.connect((host,port))
    print (' Successfull Connect! ')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n Welcome to math calculator python ')
    print (' *Number can be in decimal* ')
    print (' 1. Addtion ')
    print (' 2. Substraction ')
    print (' 3. multiplication ')
    print (' 4. division ')
    print (' 5. Logarithmic expression ')
    print (' 6. Square Root ')
    print (' 7. Exponential expression ')
    print (' 8. Exit ')
    
    ans = input ('\n Enter your choice : ' )
    Client.send(ans.encode())

    if ans == '1':
        #addtion
        print ('\n  add Function ')
        a = input('\n Enter First Number : ')
        b = input('\n Enter Second Number : ')
        Client.sendall(str.encode('\n'.join([str(a), str(b)])))
        total = Client.recv(1024)
        print ( ' Answer for addition  ' + a + ' and ' + b + ' : ' + str(total.decode()))

    elif ans == '2':
        # Substraction
        print ('\n  Minus Function ')
        a = input('\n Enter First Number : ')
        b = input('\n Enter Second Number : ')
        Client.sendall(str.encode('\n'.join([str(a), str(b)])))
        total = Client.recv(1024)
        print ( ' Answer for substraction ' + a + ' base ' + b + ' : ' + str(total.decode()))

    elif ans == '3':
        # multiplication
        print ('\n  multiplication  Function ')
        a = input('\n Enter First  Number : ')
        b = input('\n Enter Second Number : ')
        Client.sendall(str.encode('\n'.join([str(a), str(b)])))
        total = Client.recv(1024)
        print ( ' Answer for  multiplication ' + a + ' base ' + b + ' : ' + str(total.decode()))

    elif ans == '4':
        #division
        print ('\n  Division  Function ')
        a = input('\n Enter Number : ')
        b = input('\n Divide by : ')
        Client.sendall(str.encode('\n'.join([str(a), str(b)])))
        total = Client.recv(1024)
        print ( ' Answer for division ' + a + ' base ' + b + ' : ' + str(total.decode()))

    elif ans == '5':
        #log
        print ('\n  Log Function ')
        a = input('\n Enter Log Number : ')
        b = input('\n Enter base : ')
        Client.sendall(str.encode('\n'.join([str(a), str(b)])))
        total = Client.recv(1024)
        print ( ' Answer for log ' + a + ' base ' + b + ' : ' + str(total.decode()))

    elif ans == '6':
        #Square Root
        root = True
        while root:
            print ('\n  Square Root Function ')
            a = input ('\n Enter Number : ')
            if float(a) <  0:
                print('\n Negative Number Cant Be Square Root')
            else:
                root = False
                Client.send(a.encode())
                total = Client.recv(1024)

        print ( ' Answer for sqrt ' + a +' : ' + str(total.decode()))

    elif ans == '7':
        #Exponent
        print ('\n   Exponential Function ')
        a = input('\n Enter Base Number : ')
        p = input('\n Enter Power Number : ')
        Client.sendall(str.encode('\n'.join([str(a), str(p)])))
        total = Client.recv(1024)
        print ( ' Answer for ' + a + ' pow of ' + p + ' : ' + str(total.decode()))

    elif ans == '8':
        #exit
        Client.close()
        sys.exit()
    else:
        print ('\n Invalid input please try again !')

    input ( '\n Press Enter to Continue .. ')
