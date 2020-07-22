def damerau_levenshtein(seq1, seq2):
    """
    Calculate the Damerau-Levenshtein distance between two sequences.

    https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance

    The Damerau-Levenshtein distance between two words is the minimum number
    of operations (consisting of insertions, deletions or substitutions of a
    single character, or transposition of two adjacent characters) required
    to change one word into the other.

    It differs from plain Levenshtein
    distance by allowing transpositions in addition to deletions, additions
    and substitutions. A transposition is an exchange of **consecutive**
    characters.

    Taken from https://www.kaggle.com/rumbok/ridge-lb-0-41944
    """
    previous_row = None
    current_row = list(range(1, len(seq2) + 1)) + [0]
    for i in range(len(seq1)):
        previous_previous_row = previous_row
        previous_row = current_row
        current_row = [0] * len(seq2) + [i + 1]
        for j in range(len(seq2)):
            deletion_cost = previous_row[j] + 1
            addition_cost = current_row[j-1] + 1
            substitution_cost = previous_row[j-1] + (seq1[i] != seq2[j])
            current_row[j] = min(deletion_cost, addition_cost, substitution_cost)
            # transpositions
            if (i > 0 and j > 0 and seq1[i] == seq2[j-1]
                and seq1[i-1] == seq2[j] and seq1[i] != seq2[j]):
                current_row[j] = min(current_row[j], previous_previous_row[j-2] + 1)
    return current_row[len(seq2) - 1]
