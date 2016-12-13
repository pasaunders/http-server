"""Something server-y."""

import socket


def server():
    """Start a server at localhost:9999."""
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
    )
    address = ('127.0.0.1', 5175)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()

    # import pdb; pdb.set_trace()

    # message = ""
    # buffer_length = 10
    # message_complete = False
    # while not message_complete:
    #     part = " "
    #     part = conn.recv(buffer_length)
    #     print(part)
    #     message += part.decode('utf8')
    #     if len(part) < buffer_length:
    #         print('loop broke')
    #         break
    # print(message)
    # conn.sendall(message.encode('utf8'))
    # conn.close()



    message = ""
    buffer_length = 10
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        message += part.decode('utf8')
        if message[-3:] == 'EOF':
            return_message = message[:-3]
            print('eof broke')
            break
        print(part)
        # if len(part) < buffer_length:
        #     print('loop broke')
        #     break
    conn.sendall(return_message.encode('utf8'))
    conn.close()
