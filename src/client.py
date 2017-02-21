# coding=utf-8
"""Something client-y."""

import sys
import socket


def client(message):
    """Client side of an echo server."""
    if sys.version_info[0] == 3:
        try:
            message = message.decode('utf8')
        except AttributeError:
            pass
    message = str(len(message)) + '.' + message
    print('message to send is: ' + message)
    infos = socket.getaddrinfo('127.0.0.1', 5001)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    if sys.version_info[0] == 2:
        client.sendall(message)
    else:
        client.sendall(message.encode('utf8'))

    reply = ""
    buffer_length = 1024
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        reply += (part.decode('utf8'))
        if len(part) < buffer_length:
            break
    print(reply)
    return reply
    client.close()


if __name__ == "__main__":
    client(sys.argv[1])
