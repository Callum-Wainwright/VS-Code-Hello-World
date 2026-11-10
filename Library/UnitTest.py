import pytest
from datetime import date
from calculator2 import calculateDays, calculateFine, getInput

def test_calculateDays_same_month():
    assert calculateDays(1, 10, 2026, 5, 10, 2026) == 4

def test_calculateDays_across_month_boundary():
    assert calculateDays(28, 2, 2026, 5, 3, 2026) == 5

def test_calculateFine_dvd_adult():
    assert calculateFine(4, "DVD", "Adult") == 8.00

def test_calculateFine_senior_discount():
    assert calculateFine(4, "DVD", "Senior") == 4.00

def test_calculateFine_student_discount():
    assert calculateFine(4, "DVD", "Student") == 6.40

def test_calculateFine_bestseller_standard():
    assert calculateFine(4, "Best-Seller", "Adult") == 4.00

def test_calculateFine_standard_book():
    assert calculateFine(10, "Standard", "Adult") == 5.00

def test_calculateFine_max_cap():
    assert calculateFine(30, "DVD", "Adult") == 15.00

def test_calculateFine_under_max_cap():
    assert calculateFine(2, "Standard", "Adult") == 1.00

def test_getInput(monkeypatch):
    user_inputs = iter(["1", "10", "2026", "5", "10", "2026", "DVD", "Adult"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    days, book_type, member_type = getInput()
    assert days == 4
    assert book_type == "DVD"
    assert member_type == "Adult"
