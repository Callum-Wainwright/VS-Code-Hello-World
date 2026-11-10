import pytest
from datetime import date
from calculator2 import calculateDays, calculateFine

def test_calculateDays_same_month():
    assert calculateDays(1, 10, 2026, 5, 10, 2026) == 4

def test_calculateDays_using_datetime_objects():
    d1 = date(2026, 10, 1)
    d2 = date(2026, 10, 5)
    assert calculateDays(d1.day, d1.month, d1.year, d2.day, d2.month, d2.year) == 4

def test_calculateDays_across_month_boundary():
    assert calculateDays(28, 2, 2026, 5, 3, 2026) == 5

def test_calculateFine_adult_dvd():
    assert calculateFine(4, "DVD", "Adult") == 8.00

def test_calculateFine_senior_discount():
    assert calculateFine(4, "DVD", "Senior") == 4.00

def test_calculateFine_student_discount():
    assert calculateFine(4, "DVD", "Student") == 6.40

def test_calculateFine_standard_book():
    assert calculateFine(10, "Standard", "Adult") == 5.00

def test_calculateFine_max_cap():
    assert calculateFine(30, "DVD", "Adult") == 15.00
