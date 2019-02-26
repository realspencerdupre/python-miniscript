#!/usr/local/bin/python3
from codemap import map as M


class Miniscript:
    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def get_script(self):
        ''' Returns this miniscript and all it's children
            Returns:
                str - a Bitcoin Script
        '''
        args = [a.get_script() if type(a) == Miniscript else a for a in self.args]
        return M[self.name].format(*args)


def time(t):
    assert type(t) == int
    return Miniscript('time', t)


def _and(ms1, ms2):
    return Miniscript('and', ms1, ms2)


def pk(k):
    return Miniscript('pk', k)
