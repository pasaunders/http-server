#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test client and response server."""

from __future__ import unicode_literals

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


def test_ok():
    """Test that the server returns 200 OK."""
    from server import response_ok
    assert response_ok() == 'HTTP/1.1 200 OK\r\n\r\n'


def test_error():
    """Test that the server retruns 500 on error."""
    from server import response_error
    assert response_error() == 'HTTP/1.1 500 Internal Server Error\r\n'


def test_unicode():
    """Test if a string of unicode characters returns message."""
    from client import client
    response = client(u'©2017 Pat and Rick')
    assert response == 'HTTP/1.1 200 OK\r\n\r\n©2017 Pat and Rick'


def test_final():
    """Test that sending a message from client returns messge & header."""
    from client import client
    response = client('these are words')
    print('response: ', response)
    assert response == 'HTTP/1.1 200 OK\r\n\r\nthese are words'
