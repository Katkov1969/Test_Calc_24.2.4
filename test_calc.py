import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_sucsess(self):
        assert self.calc.adding(self,2, 3) == 5

    def test_adding_unsucsess(self):
        assert self.calc.adding(self,2, 3) == 8

    def test_multiply_sucsess(self):
        assert self.calc.multiply(self,2, 3) == 6

    def test_multply_unsucsess(self):
        assert  self.calc.multiply(self,2, 3) == 8

    def test_division_sucsess(self):
        assert self.calc.division(self,6, 2) == 3

    def test_division_unsucsess(self):
        assert self.calc.division(self, 6, 2) == 4

    def test_substraction_sucsess(self):
        assert self.calc.subtraction(self,6, 2) == 4

    def test_substraction_unsucsess(self):
        assert self.calc.subtraction(self,6, 2) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1,0)

    def teardown(self):
        print("Dыполнение метода Teardown")
