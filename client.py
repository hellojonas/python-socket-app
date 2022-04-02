import socket
from sys import argv

class Client:
    client = None
    host = None
    port = None
    active = False

    def __init__(self, host, port):
        self.host = host
        self.port = port
        Client.connect(self, host, port)

    def connect(self, host=None, port=None):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if host == None and port == None:
            self.client.connect((self.host, self.port))
            self.active = True
            return
        self.client.connect((host, port))
        self.active = True

    def close(self):
        if self.client == None:
            return
        self.client.close()
        self.active = False

    def send(self, msg):
        if self.client == None or not self.active:
            return
        self.client.send(msg.encode("utf-8"))

if __name__ == "__main__":
    try:
        host, port = str(argv[1]), int(argv[2])
        newClient = Client(host, port)
        newClient.send("Client message to the server")
        newClient.close()
    except TypeError:
        print("Usage: python client.py <host> <port>")
    except:
        print("Failed connecting to server")
