import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.0.6", 5500))

server.listen()

client, addr = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
        done = True
    else:
        print(f"client: {msg}")
    client.send(input("Message: ").encode('utf-8'))

client.close()
server.close()
exit()