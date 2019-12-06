import pytest

from version_one import spam_or_ham, compare_to_dict, crate_dict, add_to_spam



@pytest.mark.parametrize('input, output', [
    ('God said! ', ['god', 'said']),
    ('1:2 And the earth was', ['and', 'the', 'earth', 'was']),
    ('without form, and void; and darkness', ['without', 'form', 'and', 'void', 'and', 'darkness']),
    ('was upon the face of the deep. And', ['was', 'upon', 'the', 'face', 'of', 'the', 'deep', 'and']), 
    ('the Spirit of God moved upon the face', ['the', 'spirit', 'of', 'god', 'moved', 'upon', 'the', 'face']),
    ('of the waters.  1:3 And God said', ['of', 'the', 'waters', 'and', 'god', 'said']),
    ('Let there be light: and there was light.', ['let', 'there', 'be', 'light', 'and', 'there', 'was', 'light']),
])
def test_clean_data(input, output):
    assert clean_data(input)[0] == output


def test_create_dict():
    # """
    # The function create_dict recives two values and creates a dictionary and returns that dictionary.
    # The test asserts that when we input 2 lists, our output is a dictionary with those words
    # """
    input_1 = ''
    output =  
    assert create_dict(input_1) ==  output


def test_create_sentence():
    """
    The function create_sentence returns a stirng with 10 random sampled words as our sentence, because
    it is random all the time, we cant test what that return value is but we can test that it works 
    other ways.
    The first test makes sure that our returned sentence is 10 words long.
    The second test asserts that the returned sentence starts with the word the
    """
    test_dict = {'let': ['there'], 'the': ['earth', 'face', 'deep', 'spirit', 'face', 'waters'], 'light': ['and'], 'moved': ['upon'], 'earth': ['was'], 'void': ['and'], 'darkness': ['was'], 'of': ['the', 'god', 'the'], 'was': ['without', 'upon', 'light'], 'god': ['moved', 'said'], 'there': ['be', 'was'], 'said': ['let'], 'deep': ['and'], 'and': ['the', 'void', 'darkness', 'the', 'god', 'there'], 'face': ['of', 'of'], 'spirit': ['of'], 'upon': ['the', 'the'], 'waters': ['and'], 'without': ['form'], 'form': ['and'], 'be': ['light']}

    assert len(create_sentence(test_dict).split()) == 10
    assert create_sentence(test_dict).partition(' ')[0] == 'the'