from symspell import edit_distance


def test_substitution():
    assert edit_distance.damerau_levenshtein('bulthaup', 'bolthaup') == 1
    assert edit_distance.damerau_levenshtein('bla', ['b', 'l', 'b']) == 1
    assert edit_distance.damerau_levenshtein('bulthaup', 'bolthaip') == 2
    assert edit_distance.damerau_levenshtein('bulthaup', '') == 8


def test_addition():
    assert edit_distance.damerau_levenshtein('bulthaup', 'bulthaupi') == 1
    assert edit_distance.damerau_levenshtein('bla', ['b', 'l', 'a', 'b']) == 1
    assert edit_distance.damerau_levenshtein('bulthaup', 'bulthaupij') == 2


def test_deletion():
    assert edit_distance.damerau_levenshtein('bulthaup', 'bulthap') == 1
    assert edit_distance.damerau_levenshtein('bla', ['b', 'l']) == 1
    assert edit_distance.damerau_levenshtein('bulthaup', 'bulthp') == 2


def test_transposition():
    assert edit_distance.damerau_levenshtein('bulthaup', 'bulthuap') == 1
    assert edit_distance.damerau_levenshtein('bla', ['b', 'a', 'l']) == 1
    assert edit_distance.damerau_levenshtein('bulthaup', 'bultuhap') == 2
