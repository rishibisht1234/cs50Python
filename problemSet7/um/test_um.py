from um import count

def test_sc_at_end():
    assert count('um,') == 1
    assert count('hello um... my name is um...') == 2

def test_with_0():
    assert count('') == 0
    assert count('umr') == 0
    assert count('rum') == 0

def test_different_case():
    assert count('i am um.. i can do this but Um...UM..')==3
