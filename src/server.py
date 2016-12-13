"""Something server-y."""

import socket


def server():
    """Start a server at localhost:9999."""
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5001)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(address)

    server.listen(1)

    while True:

        conn, addr = server.accept()

        try:
            message = ""
            buffer_length = 10
            while message[-3:] != 'EOF':
                part = conn.recv(buffer_length)
                message += part.decode('utf8')
            conn.sendall(message.encode('utf8'))
        except KeyboardInterrupt:
            break
    conn.close()
    server.close()

server()
