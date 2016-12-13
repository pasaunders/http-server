"""Test client and echo server."""


def test_one():
    """Test if a string of less than one buffer echoes."""
    from client.py import client
    assert client('less') == 'less'


def test_multiple():
    """Test if a string of multiple buffer lengths echoes."""
    from client.py import client
    lots_of_words = 'this long string uses multiple buffer lengths'
    assert client(lots_of_words) == lots_of_words


def test_exact():
    """Test if a string that is an exact multiple of buffer length echoes."""
    from client.py import client
    assert client('exactlyone') == 'exactlyone'


def test_nonascii():
    """Test if a string of non-ascii characters echoes."""
    from client.py import client
    assert client('ΞΞΞΞΞΞΞ') == 'ΞΞΞΞΞΞΞ'
