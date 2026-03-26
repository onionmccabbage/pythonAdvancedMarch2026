# we may create a microservices server to handle specific functionality over http(s)

import socket

def server():
    '''this microservice will listen for client requests and respond'''
    # here are sensible defaults for most use cases
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_tuple = ('localhost', 9876) # 127.0.0.1
    server.bind(port_tuple) # the server will work over localhost port 9876
    # we may listen for any client request
    server.listen(16) # backlog defaults to one
    print(f'server is running on {port_tuple[0]}:{port_tuple[1]}')
    running = True
    while running == True: # this is a run-loop
        '''this loop will run endlessly'''
        # accept any request from a client
        (client, addr) = server.accept()
        print(f'Server received a request from {addr}')
        buf = client.recv(1024) # only the first 1024 bytes
        print(f'Server received {buf}') # NB the buffer is url-encoded
        if buf == b'quit':
            running = False
            # or...
            # break # end this whiles loop
        

if __name__ == '__main__':
    server() # here we invoke the server