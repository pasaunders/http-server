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
            part = conn.recv(buffer_length)
            total_message += part.decode('utf8')
            conn.sendall(total_message.encode('utf8'))

            total_message = "\r\n\r\n".split(total_message)

            crlf_tally = 0
            if total_message.count("\r\n\r\n") == 2:
                header = total_message[0]
                msg_body = total_message[1]

            print(msg_body)

        except KeyboardInterrupt:
            break
    conn.close()
    server.close()

def response_ok():
    pass

server()