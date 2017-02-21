"""Something server-y."""

import socket


def server():
    """Start a server at localhost:9999."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5001)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(address)

    server.listen(1)

    while True:

        conn, addr = server.accept()

        try:
            message = b""
            buffer_length = 1024
            start = conn.recv(buffer_length)
            message_length = ""
            count = 0
            while True:
                if start[count] == '.':
                    break
                message_length += start[count]
                count += 1
                if count == buffer_length:
                    count = 0
                    start = conn.recv(buffer_length)
            message += start[count + 1:]
            message_length = int(message_length)
            while len(message) < message_length:
                part = conn.recv(buffer_length)
                message += part
            conn.sendall(message)
        except KeyboardInterrupt:
            break
        conn.close()
    server.shutdown(2)
    server.close()

if __name__ == "__main__":
    server()
