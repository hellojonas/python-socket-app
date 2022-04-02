import socket
import sys

# HOST = socket.gethostbyname(socket.gethostname())
# PORT = 9191
CHUNK = 1024
host=None
port=None
server = None

# Add ovserver
def broadcast(msg):
    print(f"{msg}\n")

def run(host, port, max_conn = 1):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(max_conn)
    if server == None:
        raise Exception("Server not initialized")
    print(f"Server running on {host}:{port}")
    while True:
        conn, addr = server.accept()
        print(f'client with ip {addr} connected')
        msg = conn.recv(CHUNK).decode('utf-8')
        broadcast(msg)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try: 
            host, port = str(sys.argv[1]), int(sys.argv[2])    
        except TypeError:
            print("Error parsing connection info")
            print("Host must be IP4 format & Port must be an integer")
    else:
        print("Error runing server\nUsage: python server.py <host> <port>")
        exit(1)
    run(host, port)

