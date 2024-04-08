import socket
host=socket.gethostbyname(socket.gethostname())
port=12345
server=socket.socket(socket.AF_INET,socket.SOCK)
server.bind((host,port))
server.listen(5)
while True:
    comm_socket,address=server.accept()
    print(f"Connection from {address} has been established")
    comm_socket.send("hello world".encode('ascii'))
    comm_socket.recv(1024).decode('ascii')
    comm_socket.close()
