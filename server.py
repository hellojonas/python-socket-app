import socket
import threading
from time import sleep

CHUNK = 1024

class StopServerException(Exception):
    def __init__(self):
        self.message = "Server has been stopped"
        super().__init__(self.message)
 
class Server:
    _server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self, host="localhost", port=8000, max_conn=1):
        self._callback = None
        self._client = None 
        self._host = host
        self._port = port
        self._max_conn = max_conn
        self._server.bind((host, port))
        self._server.listen(max_conn)
        self._t_server = None
        self._t_message = None
        self._running = False

    def config(self, host, port):
        self.host = host
        self.port = port
        return self

    def _accept(self):
        while True:
            conn, addr = self._server.accept()
            # _watch_client(conn)
            print(f'client with ip {addr} connected')
            self._client = conn

    def start(self):
        print(f"Server running on {self._host}:{self._port}")
        self._t_server = threading.Thread(target=self._accept)
        self._t_server.start()
        self._running = True
        self._t_message = threading.Thread(target=self._watch_client)
        self._t_message.start()
        if not self._running:
            raise StopServerException()
        return self._t_server

    def stop(self):
        self._running = False
        self._server.close()

    def register_cb(self, cb):
        self._callback = cb

    
    def _watch_client(self):
        def on_message():
            print("[watch_cliet]: loop----\n")
            try:
                msg = self._client.recv(CHUNK).decode("utf-8")
                if not msg or msg == "":
                    return
                self._callback(msg)
            except:
                pass
        while True:
            on_message()
            sleep(1)

def init(host, port, conn_num=1):
    return Server(host, port, max_conn=conn_num)

if __name__ == "__main__":
    def print_cb(msg):
        print(f"[print_cb]: {msg}")
    myserver = Server()
    myserver.register_cb(print_cb)
    myserver.start()
    myserver.stop()
    print("server running")

