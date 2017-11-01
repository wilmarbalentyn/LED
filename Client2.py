import socket

host = '145.89.253.222'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter your command: ")
    if command == "EXIT":
        # send EXIT request to other end
        s.send(str.encode(command))
        break
    elif command == "KILL":
        # send KILL command
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('UTF-8'))

s.close()