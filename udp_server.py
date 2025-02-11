import socket
from datetime import datetime
import time

UDP_IP = "127.0.0.1" # server address
UDP_PORT = 8080 # port number

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # DGRAM for UDP
server.bind((UDP_IP, UDP_PORT)) # bind socket to the port and ip address

print("Server started")
print("Waiting for client request..")

total_received = 0
client_addr = None # to send calculated stats

start_time = datetime.now()
while True:
    data, addr = server.recvfrom(4096)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    client_addr = addr
    if data == b"STOP_SIGNAL":
      break # to stop listening for more data

    total_received += len(data)

    if total_received % (1024 * 1024) < 4096:
        print(f"Received: {total_received / (1024 * 1024):.2f} MB at {timestamp}")
end_time = datetime.now()

time_elapsed = (end_time - start_time).total_seconds()
throughput = total_received / time_elapsed
throughput_kb = throughput/1000

statistics = f"""
--- Transmission Summary ---
Received STOP_SIGNAL from {addr[0]}:{addr[1]} at {timestamp}
Client IP: {client_addr[0]}, Client Port: {client_addr[1]}
Server IP: {UDP_IP}, Server Port: {UDP_PORT}
Total time elapsed: {time_elapsed:.2f} seconds
Total data received: {total_received} bytes ({total_received / (1024 * 1024):.2f} MB)
Throughput: {throughput_kb:.2f} kilobytes/sec
"""
server.sendto(statistics.encode(), client_addr)
server.close()



                       
                      