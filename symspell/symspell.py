import logging
import re

class Symspell(object):
    def __init__(self, tokenizer=lambda x: re.findall('[a-z]+', x)):
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

    def create_dictionary(self, fname):
        """
        Create a dictionary from a file with text. It will read a file line by
        line, lower case it, and tokenize the words using self.tokenizer
        """
        total_words = 0
        unique_words = 0

        with open(fname, 'r') as f:
            for line in f:
                for word in self.tokenizer(line.lower()):
                    total_words += 1
                    if self.create_dictionary_entry(word):
                        unique_words += 1
                        if unique_words % 1000 == 0:
                            logging.debug(f'Processed {unique_words} unique words')
        logging.info(f'Total words processed: {total_words}')
        logging.info(f'Total unique words in corpus: {unique_words}')
        logging.info(f'Dictionary size (corpus words and deletions): {len(self.dictionary)}')
        logging.info(f'  edit distance for deletions: 2')
        logging.info(f'  length of longest word in corpus: {self.longest_word_length}')

    # def suggest(self, query):
    #     """
    #     Return a list of suggested corrections for potentially incorrectly spelled words
    #     """
    #     if len(query) - self.longest_word_length > 2:
    #         logging.warning('There are no items in the dictionary within the maximum edit distance')
    #         return []

    #     suggestions = {}
    #     queue = [query]

    #     while len(queue) > 0:
    #         q = queue.pop()

    #         if q in self.dictionary and q not in suggestions:
    #             if self.dictionary[q][1] > 1:
    #                 # The query is in the dictionary, and it is a word from the
    #                 # correctly spelled corpus (>1). It is also not in the
    #                 # suggestions list yet, so add it with the frequency in the
    #                 # corpus and the edit distance
    #                 suggestions[q] = (self.dictionary[q][1], len(query) - len(q))
    #                 # if len(query) == len(q):
    #                 #     break
    #                 if (len(query) - len(q)) < min
