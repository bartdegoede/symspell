from symspell import Symspell


class TestSymspell(object):
    def test_create_dictionary(self):
        symspell = Symspell()

        # creates a new entry
        created = symspell.create_dictionary_entry('bulthaup')
        assert created
        assert symspell.dictionary == {'bulthaup': ([], 1)}
        assert symspell.longest_word_length == len('bulthaup')

        # doesn't create a new entry for the same term
        created = symspell.create_dictionary_entry('bulthaup')
        assert not created
        assert symspell.dictionary == {'bulthaup': ([], 2)}
        assert symspell.longest_word_length == len('bulthaup')

        # updates longest word length
        symspell.create_dictionary_entry('bulthaupbulthaup')
        assert symspell.dictionary == {
            'bulthaup': ([], 2),
            'bulthaupbulthaup': ([], 1)
        }
        assert symspell.longest_word_length == len('bulthaupbulthaup')
