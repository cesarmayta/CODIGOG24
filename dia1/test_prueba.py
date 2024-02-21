import pytest

def inc(x):
    return x + 1

def test_prueba():
    assert 1 == 1

def test_inc():
    assert inc(3) == 4,'error en función'