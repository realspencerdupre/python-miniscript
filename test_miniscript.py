#!/usr/bin/env python3
from miniscript import (
    time,
    Miniscript,
    _and,
    pk,
)
from dummy import C


def test_time():
    t = time(1000)
    assert type(t) == Miniscript
    assert t.name == 'time'
    assert len(t.args) == 1
    assert t.get_script() == '1000 CHECKSEQUENCEVERIFY'


def test_and():
    s = _and(time(1000), pk(C))
    assert s.get_script() == (
        f'1000 CHECKSEQUENCEVERIFY {C} CHECKSIGVERIFY'
        )
