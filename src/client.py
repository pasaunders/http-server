"""Create a client to interact with a server at localhost:5353."""

import socket
import sys


def client(message):
    """Send message to server and get reply."""
    if sys.version_info[0] == 2:
        message = message.encode('utf8')

    header = 'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n'
    send_msg = header + message + '\r\n\r\n'
    infos = socket.getaddrinfo('127.0.0.1', 5353)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(send_msg.encode('utf8'))
    reply = ""
    buffer_length = 1024
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        reply += part.decode('utf8')
        if len(part) < buffer_length:
            break
    client.close()
    print(reply)
    return reply


if __name__ == "__main__":
    client("placeholder arg")
