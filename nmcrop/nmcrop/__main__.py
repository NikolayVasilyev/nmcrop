#!/usr/bin/python3
"""
run with python command: `python3 -m nmcrop`
"""

from . import main, LOG


if __name__ == "__main__":

    import sys
    from logging import StreamHandler, Formatter

    handler = StreamHandler(sys.stderr)
    formatter = Formatter()
    handler.setFormatter(formatter)
    LOG.addHandler(handler)
    LOG.setLevel(20)
    main()
