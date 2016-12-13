"""Something client-y."""

import sys
import socket


def client(message):
    """Something."""
    # infos = socket.getaddrinfo('127.0.0.1', 5008)
    # stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    # client = socket.socket(*stream_info[:3])
    # client.sendall(message.encode('utf8'))

    # buffer_length = 10
    # reply_complete = False
    # while not reply_complete:
    #     part = client.recv(buffer_length)
    #     print(part.decode('utf8'))
    #     if len(part) < buffer_length:
    #         break
    infos = socket.getaddrinfo('127.0.0.1', 5200)
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
    return reply
