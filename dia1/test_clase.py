import pytest

class Calculadora:

    def sumar(self,n1,n2):
        return n1 + n2

class TestCalculadora:

    def test_sumar(self):
        cal = Calculadora()
        assert  cal.sumar(10,10) == 20,'error'