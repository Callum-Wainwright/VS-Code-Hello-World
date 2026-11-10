import pytest
import datetime
from calculator2 import calculateFine



def test_CalculateFine():
    assert calculateFine(4,"DVD","Adult")==8.00
