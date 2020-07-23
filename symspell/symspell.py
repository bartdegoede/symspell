class Symspell(object):
    def __init__(self, tokenizer=lambda x: x.split()):
        self.dictionary = {}
        self.longest_word_length = 0
        self.tokenizer = tokenizer

    def _deletions(self, word):
        splits = [(word[:i], word[i:]) for i in range(len(word))]
        return [l + r[1:] for l, r in splits if r]

    def deletions(self, word):
        """
        Given a word, derive strings with up to 2 characters deleted
        """
        deletions = self._deletions(word)
        return set(deletions + [e2 for e1 in deletions for e2 in self._deletions(e1)])

    def create_dictionary_entry(self, word):
        """
        Add a word and its derived values to the dictionary.

        The dictionary is formatted as follows: ([list of suggestions], frequency)
        {
            'word': (['wodr', 'owrd'], 123)
        }
        """
        new_word_added = False
        if word in self.dictionary:
            # if we've already seen the word, increase the word count
            self.dictionary[word] = (self.dictionary[word][0], self.dictionary[word][1] + 1)
        else:
            # otherwise, initialize its entry
            self.dictionary[word] = ([], 1)
            self.longest_word_length = max(self.longest_word_length, len(word))

        if self.dictionary[word][1] == 1:
            # First time we've seen the word in the corpus. It may be already in
            # the dictionary as a deletion, but then we don't want to increment
            # the frequency count.
            new_word_added = True
            deletions = self.deletions(word)
            for deletion in deletions:
                if deletion in self.dictionary:
                    # add the correct word to the deletion's suggestion list
                    self.dictionary[deletion][0].append(word)
                else:
                    # add the deletion, but don't increment frequency
                    self.dictionary[deletion] = ([word], 0)

        return new_word_added
