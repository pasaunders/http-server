"""Set up a simple HTTP server."""

import socket


def server():
    """Start a server at localhost:5353."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5354)
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
            parsed = parse_request(total_message)
            print(parsed)
            final_message = parsed[0]
            print(final_message, type(final_message))
            if len(parsed) > 1:
                print(parsed[1])
            conn.sendall(final_message.encode('utf8'))
        except KeyboardInterrupt:
            break
    conn.close()
    server.shutdown()
    server.close()


def parse_request(total_message):
    """Parse user reqest, return error or request URI."""
    total_message = total_message.split("\r\n\r\n")
    msg_head = total_message[0]
    request_bits = msg_head.split()
    print(request_bits[0])
    print('GET')
    print(request_bits[0] == 'GET')
    print('request bits: ', request_bits)
    try:
        if request_bits[0] != 'GET':
            print('request is wrong: ', request_bits[0])
            raise ValueError
        elif request_bits[1] != '/index.html':
            print('path is wrong:', request_bits[1])
            raise ValueError
        elif request_bits[2] != 'HTTP/1.1':
            print('HTTP version is wrong: ', request_bits[2])
            raise ValueError
        elif request_bits[4] != 'www.example.com':
            print('URI is wrong: ', request_bits[4])
            raise ValueError
        elif b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n' != msg_head:
            print('request_form is wrong')
            raise ValueError
    except ValueError:
        return [response_error(ValueError, 'Improper header recieved.')]
    else:
        return [response_ok(), request_bits[4]]


def response_ok():
    """Send back a 200 code for OK."""
    return "HTTP/1.1 200 OK\r\n\r\n"


def response_error(error_type, error_message):
    """Send back a 500 code internal server error."""
    if error_type is ValueError:
        return "HTTP/1.1 500 Internal Server Error\r\n"

if __name__ == "__main__":
    server()
