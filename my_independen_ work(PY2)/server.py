import socket
from type_msg import *
import select
from config import *

class CServer():
    def __init__(self):
        self.server = None

    def new_listen_sock(self, address):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(address)
        server.listen(10)
        server.settimout(0.2)
        self.server = server

    def mainloop(self):
        address = ('', 7777)
        clients = []
        server = self.new_listen_sock(address)

        while True:
            try:
                conn, addr = server.accept()
            except OSError as e:
                pass
            else:
                print('получен запрос на соединение с %s' % str(addr))
                clients.append(conn)
            finally:
                w = []
                try:
                    r, w, e = select.select([], clients, [], 0)
                except Exception as e:
                    pass

                for s_clients in w:
                    timestr = time.ctime(time.time()) + '\n'
                try:
                    s_clients.send(timestr.encode('utf-8'))
                except:
                    clients.remove(s_clients)
    print('Эхо сервер запущен')

            # первый работающий вариант. простенький
            # client_sock = client_accept(self.server)
            # result = recv_msg(client_sock)
            # data = decode_msg(result)
            # code_data = prepare_msg(data)
            # result_data = encode_data(code_data)
            # send_msg(client_sock, result_data)

serv = CServer()
serv.new_listen_sock(address)
serv.mainloop()