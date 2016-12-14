"""Test client and response server."""


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
#     assert client(u'ΞΞΞΞΞΞΞ') == u'ΞΞΞΞΞΞΞ'


def test_ok():
    """Test that the server returns 200 OK."""
    from server import response_ok
    assert response_ok() == 'HTTP/1.1 200 OK<CRLF>'


def test_error():
    """Test that the server retruns 500 on error."""
    from server import response_error
    assert response_error() == 'HTTP/1.1 500 Internal Server Error<CRLF>'


def test_final():
    """Test that sending a message from client returns messge & header."""
    from client import client
    assert client('these are words') == 'HTTP/1.1 200 OK\n\rthes are words'
