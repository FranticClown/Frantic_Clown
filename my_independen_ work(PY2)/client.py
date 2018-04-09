import socket
import select
from subprocess import Popen, CREATE_NEW_CONSOLE
from type_msg import *
from config import *

class CClient():
    def __init__(self):
        self.server = None

    def sock_client(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(('localhost', 7777))
        self.server = server

    def mainloop(self):
        send_msg(self.server, encode_data(f_presence()))
        encoded_data = (self.server)
        print(encoded_data)


cl = CClient()
cl.sock_client()
cl.mainloop()