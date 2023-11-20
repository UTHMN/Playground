import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.0.6", 5500))

done = False

while not done:
    client.send(input("Message: ").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
        done = True
    else:
        print(f"server: {msg}")

client.close()
exit()