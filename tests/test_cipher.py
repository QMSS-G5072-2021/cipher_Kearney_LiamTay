import pytest
from cipher_ltk2118.cipher_func import cipher

## Parts A-E

def test_cipher_a():
    """ Testing if the cipher works on a single word """
    actual = cipher("Tom Hanks is great", 5)
    assert actual == "Ytr Mfspx nx lwjfy", "Fails on single word"

def test_cipher_b():
    """ Testing if cipher works w/ negative shift"""
    actual = cipher("Tom Hanks is great", -1)
    assert actual == "Snl GZmjr hr fqdZs", "Fails on negative shift"

def test_cipher_c():
    """ Testing if cipher works on symbols"""
    actual = cipher("T0m H&nk$ !s gr#@T", -6)
    assert actual == "N0g B&he$ !m al#@N", "Fails on symbols"

def test_cipher_d():
    """ Testing if cipher raises AssertionError if shift is not numeric"""
    with pytest.raises(AssertionError):
        cipher("T0m H&nk$ !s gr#@T", "BlahdiBlah7")

## Part F

@pytest.mark.parametrize("example_test, shift_test, expected", [
    ('Liam', 5, "Qnfr"),
    ('shiokadoos', -44, "ApqwsilwwA"),
    ("HAWAIIAN PIZZA", 10, "RKgKSSKX ZSjjK"),
    ("The Computer says no.", 3, "Wkh Frpsxwhu vdBv qr.")
])

def test_cipher_f(example_test, shift_test, expected):
    """parametrized test on single word, negative shift, capitals & sentence w/ spaces"""
    result = cipher(example_test, shift_test)
    assert result == expected

def test_cipher_g():
    """integration-like test on shift values 1-10 using for loop"""
    #this will show up as a single test
    decrypted = "The Exp{}rt-Imp*rt B$nk"
    for i in range(1, 11):
        encrypted = cipher(decrypted, i)
        assert decrypted == cipher(encrypted, i, encrypt=False)

## Alternative to g, tested on shift only
@pytest.mark.parametrize("shift_test", list(range(1,11)))
def test_cipher_g2(shift_test):
    """integration-like test on shift values 1-10 using mark.parametrize"""
    #this will show up as 10 separate tests
    decrypted = "The Exp{}rt-Imp*rt B$nk"
    encrypted = cipher(decrypted, shift_test)
    assert decrypted == cipher(encrypted, shift_test, encrypt=False)
