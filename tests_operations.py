from operations import (
    addition,
    subtraction,
    multiplication,
    division,
    exponentiation,
    modulo,
)


def test_addition():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function addition
    THEN:  the resulting is the addition of the two numbers
    """
    assert addition(1,2) == 3
    assert addition(0,1) == 1
    assert addition(100,23) == 123


def test_subtraction():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function subtraction
    THEN:  the resulting is the subtraction of the two numbers
    """
    assert subtraction(7, 10) == -3, "Wrong, should be -3"
    assert subtraction(10, 5) == 5, "Wrong, should be 5"
    assert subtraction(0, 0) == 0, "Wrong, should be 0"
    assert subtraction(1, 0) == 1, "Wrong, should be 1"
    assert subtraction(-5, -3) == -2, "Wrong, should be -2"


def test_multiplication():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function multiplication
    THEN:  the resulting is the multiplication of the two numbers
    """
    assert multiplication(3, 5) == 15
    pass


def test_division():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number
    """
    # assert division(8, 4) == 2
    pass


def test_division_exception_on_zero():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function division
    THEN:  the resulting is the division of the two number

    Hint: https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
    """
    pass


def test_exponentiation():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function exponentiation
    THEN:  the resulting is the exponentiation of the two number
    """
    pass


def test_modulo():
    """
    GIVEN: Two numbers
    WHEN:  passed in to the function modulo
    THEN:  the resulting is the modulo of the two number
    """
    pass
