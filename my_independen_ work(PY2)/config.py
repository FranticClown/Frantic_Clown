import json
from type_msg import *



def client_accept(server):
    client_sock, addr = server.accept()
    print("запрос на соединение от {}".format(str(addr)))
    return client_sock

def recv_msg(server_sock):
    result = server_sock.recv(1024)
    return result

def decode_msg(encoded_data):
    json_data = encoded_data.decode('utf-8')
    data = json.loads(json_data)
    return data

def encode_data(decoded_msg):
    msg = decoded_msg
    jmsg = json.dumps(msg)
    bjmsg = jmsg.encode('utf-8')
    return bjmsg

def send_msg(client_sock, bjmsg):
    client_sock.send(bjmsg)

def prepare_msg(data):
    if data['action'] == 'presence':
        return 200
    else:
        400

def finaly_msg(kod):
    if kod >= 400:
        error_data = f_error(kod, code[kod])
        return error_data
    elif 200 <= kod < 400:
        alert_data = f_alert(kod, code[kod])
        return alert_data

