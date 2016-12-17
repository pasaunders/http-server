"""Test client and response server."""
# encoding:utf-8

import pytest

# def test_one():
#     """Test if a string of less than one buffer echoes."""
#     from client import client
#     assert client(u'less') == u'less'


# def test_multiple():
#     """Test if a string of multiple buffer lengths echoes."""
#     from client import client
#     lots_of_words = u'this long string uses multiple buffer lengths'
#     assert client(lots_of_words) == lots_of_words


# def test_exact():
#     """Test if a string that is an exact multiple of buffer length echoes."""
#     from client import client
#     assert client(u'exactlyoneexactly') == u'exactlyoneexactly'


# def test_nonascii():
#     """Test if a string of non-ascii characters echoes."""
#     from client import client
#     assert client(u'') == u''

PARAMS_TABLE = [
    ['GET /webroot/sample.txt HTTP/1.1\r\nHost www.example.com\r\n\r\n', b'This is a very simple text file.\nJust to show that we can serve it up.\nIt is three lines long.'],
    ['GET /webroot/images HTTP/1.1\r\nHost www.example.com\r\n\r\n', b'HTTP/1.1 200 OK\r\n\r\n<html><a href="JPEG_example.jpg"><a href="sample_1.png"><a href="Sample_Scene_Balls.jpg"></html>'],
]


def test_ok():
    """Test that the server returns 200 OK."""
    from concurrent_http import response_ok
    assert response_ok() == 'HTTP/1.1 200 OK\r\n\r\n'


def test_error():
    """Test that the server retruns 500 on error."""
    from concurrent_http import response_error
    assert response_error(ValueError, "Something happened.") == 'HTTP/1.1 500 Internal Server Error\r\n'


def test_final():
    """Test that sending a message from client returns messge & header."""
    from client import client
    response = client('GET /webroot/sample.txt HTTP/1.1\r\nHost www.example.com\r\n\r\n')
    print('response: ', response)
    assert response == b'HTTP/1.1 200 OK\r\n\r\n'


def test_sending_put_fails():
    """Test that server doesn't take PUT request."""
    from client import client
    assert client() == "HTTP/1.1 500 Internal Server Error\r\n"


@pytest.mark.parametrize("given, expected", PARAMS_TABLE)
def test_requested_file_returns(given, expected):
    """Test that requested file received on client."""
    from client import client
    assert client(given) == expected
