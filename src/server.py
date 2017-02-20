"""Set up a simple HTTP server."""

from __future__ import unicode_literals
import socket


def server():
    """Start a server at localhost:5353."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5353)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(1)

    while True:
        conn, addr = server.accept()
        try:
            total_message = ""
            buffer_length = 1024
            while total_message.count("\r\n\r\n") != 2:
                part = conn.recv(buffer_length)
                total_message += part.decode('utf8')
            total_message = total_message.split("\r\n\r\n")
            msg_body = total_message[1]
            try:
                final_message = response_ok() + "".join(msg_body)
                print(final_message, type(final_message))
                conn.sendall(final_message.encode('utf8'))
            except:
                conn.sendall(response_error().encode('utf8'))
                total_message += part
            conn.sendall(total_message)
        except KeyboardInterrupt:
            break
        conn.close()
    import pdb; pdb.set_trace()
    server.shutdown(2)
    server.close()


def response_ok():
    """Send back a 200 code for OK."""
    return "HTTP/1.1 200 OK\r\n\r\n"


def response_error():
    """Send back a 500 code internal server error."""
    return "HTTP/1.1 500 Internal Server Error\r\n"


if __name__ == "__main__":
    server()
