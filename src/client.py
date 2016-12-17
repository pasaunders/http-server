"""Create a client to interact with a server at localhost:5353."""

import socket


def client(message):
    """Send message to server and get reply."""
    send_msg = message + '\r\n\r\n'
    infos = socket.getaddrinfo('127.0.0.1', 5354)
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
    return reply
    client.close()

if __name__ == "__main__":

    client('GET /webroot/make_time.py HTTP/1.1\r\nHost: www.example.com\r\n\r\nwords words words')
