import pytest
from programs import vowel


def test_vowel2():
    assert vowel.vowels('zake') == 2
def test_vowel3():
    assert vowel.vowels('houses') == 3
def test_vowel12():
    assert vowel.vowels('aaaeeeiiiooo') == 12
def test_vowel4():
    assert vowel.vowels('the whole world') == 4