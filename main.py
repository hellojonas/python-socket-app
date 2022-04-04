from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from client import Client


class HistoryScreen(MDScreen):
   pass 


class ChatScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MenuScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ip_addr = None
        self.port_num = None
        self.clients = Client()


    def setup_acc(self):
        self.ip_addr = self.ids.ip.text
        self.port_num = self.ids.port.text
        # self.client = Client(self.ip_addr, int(self.port_num))
        self.clients.connect(self.ip_addr, int(self.port_num))
        print(self.ip_addr, self.port_num)

    def send_msg(self, msg):
        self.clients.send(msg.text)


class MainScreen(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"


if __name__=="__main__":
    clients = MainApp()
    clients.run()
