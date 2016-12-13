"""Something client-y."""

import sys
import socket


def client(message):

    message += 'EOF'
    print('message to send is: ' + message)
    infos = socket.getaddrinfo('127.0.0.1', 5001)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

    client.sendall(message.encode('utf8'))

    reply = ""
    buffer_length = 10
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        reply += (part.decode('utf8'))
        if len(part) < buffer_length:
            break
    return reply[:-3]
    client.close()
