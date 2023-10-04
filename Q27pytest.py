import math

def test_grade():
    grade = 60
    assert grade >= 50

def test_temp():
    celcius = 40
    fahrenheit = 50
    assert celcius / fahrenheit == 2

def test_square():
    l = 15
    w = 10
    h = 10
    assert l * w * h  == 1000