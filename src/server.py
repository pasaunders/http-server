"""Set up a simple HTTP server."""

import socket
import os
import io


def server():
    """Start a server at localhost:5354."""
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
            print(parsed[1], type(parsed))
            print(parsed)
            status_message = parsed[0]
            print(status_message)
            print(parsed[1])
            reply = status_message + parsed[1]
            conn.sendall(reply.encode('utf8'))
            # conn.sendall(parsed[1].encode('utf8'))
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
    try:
        print(msg_head, type(msg_head))
        if msg_head == 'GET /webroot/ HTTP/1.1\r\nHost: www.example.com':
            uri = request_bits[1]
            return [response_ok(), resolve_uri(uri)]
        if request_bits[0] != 'GET':
            raise ValueError
        elif request_bits[1] != '/webroot/':
            print('path is wrong:', request_bits[1])
            raise ValueError
        elif request_bits[2] != 'HTTP/1.1':
            print('HTTP version is wrong: ', request_bits[2])
            raise ValueError
        elif request_bits[4] != 'www.example.com':
            print('URI is wrong: ', request_bits[4])
            raise ValueError
    except ValueError:
        return [response_error(ValueError, 'Improper header recieved.')]


def response_ok():
    """Send back a 200 code for OK."""
    return "HTTP/1.1 200 OK\r\n\r\n"


def response_error(error_type, error_message):
    """Send back a 500 code internal server error."""
    if error_type is ValueError:
        return "HTTP/1.1 500 Internal Server Error\r\n"


def resolve_uri(uri):
    """Find and return requested resource."""
    uri_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', uri[1:])
    if os.path.isfile(uri_path):
        return io.open(uri_path)
    elif os.path.isdir(uri_path):
        return " ".join(os.listdir(uri_path))
    else:
        pass


def return_webpage():
    webdir = (os.listdir('../webroot'))
    for i in webdir:
        html = """
        <html>
        <head></head>
        <body>
        <h2>Directory listing:</h2>
        """

    for i in webdir:
        html += '<li><a href="'  + i + '>' + i + '</a> </li>'

    html += """
    </body>
    </http>
    """
    print(html)

if __name__ == "__main__":
    server()
