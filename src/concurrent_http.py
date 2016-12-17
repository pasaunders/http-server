"""Set up a simple HTTP server."""

from __future__ import unicode_literals
import os


def server(socket, address):
    """Start a server at localhost:5354."""
    total_message = ""
    buffer_length = 1024
    while total_message.count("\r\n\r\n") != 2:
        part = socket.recv(buffer_length)
        total_message += part.decode('utf8')
    print('Total message: ', total_message)
    parsed = parse_request(total_message)
    print(parsed)
    status_message = parsed[0]
    print(status_message)
    if len(parsed) > 1:
        reply = status_message + parsed[1]
    else:
        reply = status_message
    socket.sendall(reply.encode('utf8'))
    print('we sent response to client.')
    socket.close()


def parse_request(total_message):
    """Parse user reqest, return error or request URI."""
    total_message = total_message.split("\r\n\r\n")
    msg_head = total_message[0]
    request_bits = msg_head.split()
    try:
        print(msg_head, type(msg_head))
        if request_bits[0] != 'GET':
            raise ValueError
        elif request_bits[2] != 'HTTP/1.1':
            print('HTTP version is wrong: ', request_bits[2])
            raise ValueError
        elif request_bits[4] != 'www.example.com':
            print('URI is wrong: ', request_bits[4])
            raise ValueError
        else:
            uri = request_bits[1]
            print('this is the uri: ', uri)
            return [response_ok(), resolve_uri(uri)]
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
    if uri[0] == '/':
        uri = uri[1:]
    uri_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', uri)
    print('uri_path: ', uri_path)
    # kind_of_file = mimetypes.guess_type(uri_path) - use later for content-type header.
    if os.path.isfile(uri_path):
        print('in isfile statement')
        with open(uri_path, 'rb') as file_record:
            file = file_record.read()
            print('file: ', file)
            file_record.close()
            return str(file)
    elif os.path.isdir(uri_path):
        print('dirstatment detected')
        return "<html>" + return_webpage(os.listdir(uri_path)) + "</html>"
    else:
        pass


def return_webpage(file_list):
    """Return list of directory contents as html."""
    links = ''
    for entry in file_list:
        links += '<a href="' + entry + '">'
    return links


if __name__ == "__main__":
    try:
        from gevent.server import StreamServer
        from gevent.monkey import patch_all

    patch_all()
    server = StreamServer(('127.0.0.1', 5678), server)
    print('Starting concurrency server test.')
    server.serve_forever()
