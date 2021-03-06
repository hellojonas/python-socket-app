from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
import server 
from kivy.clock import Clock
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.label import Label
from threading import Thread

server_socket = server.Server()

class ListenScreen(MDScreen):
    chat = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "listen"

        self.chat_msg = None

        self.layout = MDGridLayout(cols=1, size_hint_y = None)
        self.add_widget(self.layout)

        self.chat_history = Label(size_hint_y = None, markup = True)
        self.scroll_to_point = Label()
        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_to_point)

        def on_messsage(msg):
            self.chat_history.text += "\n" + msg

        MainScreen.register_cb(on_messsage)



class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = "login_server"

        self.ip = None
        self.port = None
        self.server = None

    def server_listen(self):
        self.ip = self.ids.ip.text
        self.port = int(self.ids.port.text)

        server_socket.config(self.ip, self.port).start()
        
class MainScreen(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    @staticmethod
    def register_cb(cb):
        server_socket.register_cb(cb)


class ServerKv(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"


if __name__=="__main__":
    server_terminal = ServerKv()
    server_terminal.run()
