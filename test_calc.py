import pytest

from app.calc2 import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiplay_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_success(self):
        assert self.calc.division(self, 6, 3) == 2

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 2, 1) == 1

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_degree_success(self):
        assert self.calc.degree(self, 2, 3) == 8

    def test_zero_division(self):
         with pytest.raises(ZeroDivisionError):
             self.calc.division(self, 1, 0)

    def teardown(self):
        print("Выполнение метода Teardown")




