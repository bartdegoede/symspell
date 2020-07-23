from symspell import Symspell


class TestSymspell(object):
    def test_create_dictionary(self):
        symspell = Symspell()

        # creates a new entry
        created = symspell.create_dictionary_entry('bulthaup')
        assert created
        assert symspell.dictionary == {
            'bulthaup': ([], 1),
            'bltaup': (['bulthaup'], 0),
            'bulhup': (['bulthaup'], 0),
            'ulthup': (['bulthaup'], 0),
            'bulhap': (['bulthaup'], 0),
            'uthaup': (['bulthaup'], 0),
            'bultaup': (['bulthaup'], 0),
            'bulthu': (['bulthaup'], 0),
            'blthaup': (['bulthaup'], 0),
            'bultup': (['bulthaup'], 0),
            'buthup': (['bulthaup'], 0),
            'bthaup': (['bulthaup'], 0),
            'ultaup': (['bulthaup'], 0),
            'bulthup': (['bulthaup'], 0),
            'lthaup': (['bulthaup'], 0),
            'bulthap': (['bulthaup'], 0),
            'blthau': (['bulthaup'], 0),
            'ulthau': (['bulthaup'], 0),
            'blthup': (['bulthaup'], 0),
            'buthau': (['bulthaup'], 0),
            'ulhaup': (['bulthaup'], 0),
            'bulthp': (['bulthaup'], 0),
            'bulaup': (['bulthaup'], 0),
            'bultau': (['bulthaup'], 0),
            'butaup': (['bulthaup'], 0),
            'buthaup': (['bulthaup'], 0),
            'ulthap': (['bulthaup'], 0),
            'blhaup': (['bulthaup'], 0),
            'bulhaup': (['bulthaup'], 0),
            'ulthaup': (['bulthaup'], 0),
            'bulhau': (['bulthaup'], 0),
            'blthap': (['bulthaup'], 0),
            'bulthau': (['bulthaup'], 0),
            'bultap': (['bulthaup'], 0),
            'buthap': (['bulthaup'], 0),
            'buhaup': (['bulthaup'], 0),
            'bultha': (['bulthaup'], 0)
        }
        assert symspell.longest_word_length == len('bulthaup')

        # doesn't create a new entry for the same term
        created = symspell.create_dictionary_entry('bulthaup')
        assert not created
        assert symspell.dictionary == {
            'bulthaup': ([], 2),
            'bltaup': (['bulthaup'], 0),
            'bulhup': (['bulthaup'], 0),
            'ulthup': (['bulthaup'], 0),
            'bulhap': (['bulthaup'], 0),
            'uthaup': (['bulthaup'], 0),
            'bultaup': (['bulthaup'], 0),
            'bulthu': (['bulthaup'], 0),
            'blthaup': (['bulthaup'], 0),
            'bultup': (['bulthaup'], 0),
            'buthup': (['bulthaup'], 0),
            'bthaup': (['bulthaup'], 0),
            'ultaup': (['bulthaup'], 0),
            'bulthup': (['bulthaup'], 0),
            'lthaup': (['bulthaup'], 0),
            'bulthap': (['bulthaup'], 0),
            'blthau': (['bulthaup'], 0),
            'ulthau': (['bulthaup'], 0),
            'blthup': (['bulthaup'], 0),
            'buthau': (['bulthaup'], 0),
            'ulhaup': (['bulthaup'], 0),
            'bulthp': (['bulthaup'], 0),
            'bulaup': (['bulthaup'], 0),
            'bultau': (['bulthaup'], 0),
            'butaup': (['bulthaup'], 0),
            'buthaup': (['bulthaup'], 0),
            'ulthap': (['bulthaup'], 0),
            'blhaup': (['bulthaup'], 0),
            'bulhaup': (['bulthaup'], 0),
            'ulthaup': (['bulthaup'], 0),
            'bulhau': (['bulthaup'], 0),
            'blthap': (['bulthaup'], 0),
            'bulthau': (['bulthaup'], 0),
            'bultap': (['bulthaup'], 0),
            'buthap': (['bulthaup'], 0),
            'buhaup': (['bulthaup'], 0),
            'bultha': (['bulthaup'], 0)
        }
        assert symspell.longest_word_length == len('bulthaup')

        # updates longest word length
        symspell.create_dictionary_entry('bulthaupbulthaup')
        assert symspell.dictionary['bulthaupbulthaup'] == ([], 1)
        assert symspell.longest_word_length == len('bulthaupbulthaup')

    def test_deletions(self):
        symspell = Symspell()

        assert symspell._deletions('bulthaup') == [
            'ulthaup',
            'blthaup',
            'buthaup',
            'bulhaup',
            'bultaup',
            'bulthup',
            'bulthap',
            'bulthau'
        ]
        assert symspell.deletions('bulthaup') == {
            'blhaup',
            'bltaup',
            'blthap',
            'blthau',
            'blthaup',
            'blthup',
            'bthaup',
            'buhaup',
            'bulaup',
            'bulhap',
            'bulhau',
            'bulhaup',
            'bulhup',
            'bultap',
            'bultau',
            'bultaup',
            'bultha',
            'bulthap',
            'bulthau',
            'bulthp',
            'bulthu',
            'bulthup',
            'bultup',
            'butaup',
            'buthap',
            'buthau',
            'buthaup',
            'buthup',
            'lthaup',
            'ulhaup',
            'ultaup',
            'ulthap',
            'ulthau',
            'ulthaup',
            'ulthup',
            'uthaup'
        }
