import pytest

from pythoncode.calc import Calculator


class TestCal:
    def setup(self):
        self.calc = Calculator()

    def test_add(self):
        # 加法 - 正整数与正整数
        assert 3 == self.calc.add(1, 2)

    def test_add1(self):
        # 加法 - 正整数与负整数
        assert 20 == self.calc.add(30, -10)

    def test_add2(self):
        # 加法 - 正整数与0
        assert 30 == self.calc.add(30, 0)

    def test_add3(self):
        # 加法 - 正整数与浮点数
        assert 31.5 == self.calc.add(30, 1.5)

    def test_add4(self):
        # 加法 - 正整数与复数
        assert 31 + 5j == self.calc.add(30, 1 + 5j)

    def test_add5(self):
        # 加法 - 负整数与0
        assert -29 + 5j == self.calc.add(-30, 1 + 5j)

    def test_add6(self):
        # 加法 - 浮点数与浮点数
        assert 3 == self.calc.add(1.5, 1.5)

    def test_add7(self):
        # 加法 - 浮点数与0
        assert 1.5 == self.calc.add(1.5, 0)

    def test_add8(self):
        # 加法 - 复数与复数
        assert -29 + 5j == self.calc.add(-30 + 2j, 1 + 3j)

    def test_add9(self):
        # 加法 - 复数与浮点数
        assert -29.5 + 5j == self.calc.add(-30.5 + 2j, 1 + 3j)

    def test_add10(self):
        # 加法 - 结果错误
        assert -29.5 + 5j != self.calc.add(-40.5 + 2j, 1 + 3j)

    def test_div(self):
        # 除法-整数与整数
        assert 3 == self.calc.div(6, 2)

    @pytest.mark.xfail
    def test_div1(self):
        # 除法-整数与0
        assert 1 != self.calc.div(6, 0)

    def test_div2(self):
        # 除法-整数与浮点数
        assert 4 == self.calc.div(6, 1.5)

    def test_div3(self):
        # 除法-正数与负数
        assert -3 == self.calc.div(6, -2)

    def test_div4(self):
        # 除法-整数与复数
        assert 4 != self.calc.div(6, 1.5 + 5j)
