# this is a client for our microservices server. All interactions happen over http(s)
import socket
import sys

def client():
    '''This client will send a rwquest to the miroservice server'''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_t = ('localhost', 9876)
    client.connect(port_t)
    # send a request to the server
    msg = 'quit'.encode() # we need ot encode all communication over http(s)
    client.send(msg)
    client.close() # tidy up


if __name__ == '__main__':
    client()