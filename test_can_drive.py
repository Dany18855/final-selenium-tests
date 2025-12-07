import pytest

def can_drive(age):
    driving_age = 16
    return age >= driving_age


def test_age_below_driving_age():
    assert can_drive(15) is False


def test_age_equal_to_driving_age():
    assert can_drive(16) is True


def test_age_above_driving_age():
    assert can_drive(20) is True


def test_age_zero():
    assert can_drive(0) is False


def test_negative_age():
    assert can_drive(-10) is False
