from pydsa.euclid import gcd, modular_linear_solver, extended_euclid, linear_diophantine

def test_gcd():
    assert gcd(4, 10) == 2
    assert gcd(89, 23) == 1
    assert gcd(1024, 512) == 512
    assert gcd(116127, 15433) == 253

def test_extended_euclid():
    assert extended_euclid(4, 10) == (2, -2, 1)
    assert extended_euclid(89, 23) == (1, -8, 31)
    assert extended_euclid(1024, 512) == (512, 0, 1)
    assert extended_euclid(116127, 15433) == (253, 21, -158)

def test_modular_linear_solver():
    assert modular_linear_solver(54, 21, 4) == []
    assert modular_linear_solver(89, 63, 123) == [9]
    assert modular_linear_solver(16, 24, 22) == [7, 18]
    assert modular_linear_solver(51, 54, 99) == [3, 36, 69]
    assert modular_linear_solver(20, 68, 12) == [1, 4, 7, 10]
    assert modular_linear_solver(40, 15, 95) == [17, 36, 55, 74,93]

def test_linear_diophantine():
    assert linear_diophantine(26, 13, 65) == (-5, 15)
    assert linear_diophantine(7, 8, 15) == (105, -90)
    assert linear_diophantine(12, 13, 125) == (1500, -1375)
    assert linear_diophantine(12, 16, 20) == (15, -10)

