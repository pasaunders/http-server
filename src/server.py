"""Something server-y."""

import socket


def server():
    """Start a server at localhost:9999."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5001)
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
            total_message = "\r\n\r\n".split(total_message)
            # header = total_message[0]
            msg_body = total_message[1]
            print(msg_body)
            try:
                final_message = response_ok() + total_message
                conn.sendall(final_message.encode('utf8'))
            except:
                conn.sendall(response_error().encode('utf8'))

        except KeyboardInterrupt:
            break
    conn.close()
    server.close()


def response_ok():
    """Send back a 200 code for OK."""
    return "HTTP/1.1 200 OK\n\r"


def response_error():
    """Send back a 500 code internal server error."""
    return "HTTP/1.1 500 Internal Server Error\n\r"


server()
