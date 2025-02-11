import socket
import sys
import os
from datetime import datetime

UDP_IP = "127.0.0.1" # localhost
UDP_PORT = 8080 # port number

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM for UDP

print("Enter number of megabytes to send (25-200): ")

while(True):
  x = input()
  if(int(x) < 25 or int(x) > 200):
    print("Choose a number between 25 and 200")
  else:
    break

datasize = int(x)*1024*1024
payload = os.urandom(int(x) * 1024*1024)

bytes_sent = 0
byte_chunk = 4096

while(bytes_sent < datasize):
  chunk = payload[bytes_sent:bytes_sent + byte_chunk]
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
  client.sendto(chunk, (UDP_IP, UDP_PORT))
  bytes_sent += len(chunk)

  if bytes_sent % (1024 * 1024) < byte_chunk:
            print(f"Sent: {bytes_sent / (1024 * 1024):.2f} MB at {timestamp}")

stop_signal = b"STOP_SIGNAL"
client.sendto(stop_signal, (UDP_IP, UDP_PORT))
print(f"Total sent: {bytes_sent / (1024 * 1024):.2f} MB")
statistics, _ = client.recvfrom(1024)
client.close()
print(statistics.decode())




  
