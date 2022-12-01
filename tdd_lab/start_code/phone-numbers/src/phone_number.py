import unittest
from src.phone_number import *

def phone_number_formatter(input_int):
    istr = str(input_int)
    return f"({istr[0:3]}) {istr[3:6]}-{istr[6:10]}"
