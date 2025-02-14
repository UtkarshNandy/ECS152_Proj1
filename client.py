import socket
import json

proxy_ip = ""
proxy_port = 0
server_ip = "127.0.0.1"
server_port = 7000
message = "ping"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((proxy_ip, proxy_port))

transmission = json.dumps({"server_ip": server_ip, "server_port": server_port, "message": message})

client.sendall(transmission.encode())
print("Server Response: " + client.recv(1024).decode())
client.close()

