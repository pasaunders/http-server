#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test client and echo server."""
from __future__ import unicode_literals

def test_one():
    """Test if a string of less than one buffer echoes."""
    from client import client
    assert client('less') == 'less'


def test_multiple():
    """Test if a string of multiple buffer lengths echoes."""
    from client import client
    lots_of_words = 'this long string uses multiple buffer lengths'
    assert client(lots_of_words) == lots_of_words


def test_exact():
    """Test if a string that is an exact multiple of buffer length echoes."""
    from client import client
    assert client('exactlyoneexactly') == 'exactlyoneexactly'


def test_nonascii():
    """Test if a string of non-ascii characters echoes."""
    from client import client
    assert client('ΞΞΞΞΞΞΞ') == 'ΞΞΞΞΞΞΞ'
