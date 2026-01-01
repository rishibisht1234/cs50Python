from plates import is_valid

def test_length():
    assert is_valid('ab') == True
    assert is_valid('ab1234') == True
    assert is_valid('a') == False
    assert is_valid('abcd12345') == False

def test_start_with_alphabet():
    assert is_valid('ab12')==True
    assert is_valid('12345')==False
    assert is_valid('1a2345')==False

def test_number_in_middle():
    assert is_valid('ab12ab')==False

def test_punctuation():
    assert is_valid('ab,12') == False
    assert is_valid('ab?') == False
    assert is_valid('ab 23')== False
    assert is_valid('ab23.')== False

def test_number_start_with_0():
    assert is_valid('ab012')== False
