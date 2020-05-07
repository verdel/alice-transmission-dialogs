# -*- coding: utf-8 -*-
import logging


def humanize_bytes(bytes, precision=2):
    """Return a humanized string representation of a number of bytes.

    Assumes `from __future__ import division`.

    >>> humanize_bytes(1)
    '1 byte'
    >>> humanize_bytes(1024)
    '1.0 kB'
    >>> humanize_bytes(1024*123)
    '123.0 kB'
    >>> humanize_bytes(1024*12342)
    '12.1 MB'
    >>> humanize_bytes(1024*12342,2)
    '12.05 MB'
    >>> humanize_bytes(1024*1234,2)
    '1.21 MB'
    >>> humanize_bytes(1024*1234*1111,2)
    '1.31 GB'
    >>> humanize_bytes(1024*1234*1111,1)
    '1.3 GB'
    """
    abbrevs = (
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'kB'),
        (1, 'bytes')
    )
    if bytes == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f %s' % (precision, bytes / factor, suffix)


def init_log(debug=None):
    if debug:
        consolelog_level = logging.DEBUG
    else:
        consolelog_level = logging.INFO

    logger = logging.getLogger('alice-transmission-dialogs')
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    consolelog = logging.StreamHandler()
    consolelog.setLevel(consolelog_level)

    # create formatter and add it to the handlers
    formatter = logging.Formatter(u'%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s')
    consolelog.setFormatter(formatter)

    # add the handlers to logger
    logger.addHandler(consolelog)

    return logger
