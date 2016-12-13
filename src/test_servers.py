"""Test client and echo server."""


def test_one():
    """Test if a string of less than one buffer echoes."""
    from client import client
    assert client(u'less') == u'less'


def test_multiple():
    """Test if a string of multiple buffer lengths echoes."""
    from client import client
    lots_of_words = u'this long string uses multiple buffer lengths'
    assert client(lots_of_words) == lots_of_words


def test_exact():
    """Test if a string that is an exact multiple of buffer length echoes."""
    from client import client
    assert client(u'exactlyoneexactly') == u'exactlyoneexactly'


def test_nonascii():
    """Test if a string of non-ascii characters echoes."""
    from client import client
    assert client(u'ΞΞΞΞΞΞΞ') == u'ΞΞΞΞΞΞΞ'
