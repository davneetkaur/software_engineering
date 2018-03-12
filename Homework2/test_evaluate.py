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

#feature to convert string to lowewr case
def test_parse_string():
    assert parse_string('HUMAN') == 'human'
    assert parse_string('snow') == 'snow'
    assert parse_string('purPLE') == 'purple'
    assert parse_string('leARn') == 'learn'
    assert parse_string('CREDIT') == 'credit'
    assert parse_string('Journal') == 'journal'
    assert parse_string('HaPpY') == 'happy'

#feature to find if a string has vowels
def test_evaluate_string():
    assert evaluate_string('sync') == False
    assert evaluate_string('CAT') == True
    assert evaluate_string('Myth') == False
    assert evaluate_string('laUgh') == True
    assert evaluate_string('Acquire') == True
    assert evaluate_string('Shy') == False
    assert evaluate_string('wYns') == False
    assert evaluate_string('THYMM') == False
    assert evaluate_string('Project') == True
    assert evaluate_string('lyMPH') == False
    assert evaluate_string('mothER') == True
    
    