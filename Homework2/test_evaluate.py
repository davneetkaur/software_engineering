import numpy as np
from evaluate import *

def setup_module(module):
    print("\nsetup_module\n")
    
def teardown_module(module):
    print("\nteardown_module\n")
    
def test_parse_integer():
    print("\ntest_parse_integer\n")
    for i in range(0,100):
        s = str(i)
        assert parse_integer(s) == i
    
def test_parse_float():
    print("\ntest_parse_float\n")
    for i in np.arange(0.0, 100.0):
        s = str(i)
        assert parse_float(s) == i

def test_parse_string():
    print("\ntest_parse_string\n")
    for i in ('1', '2', '3', '4', '5', '6'):
        s = int(i)
        assert parse_string(s) == i
