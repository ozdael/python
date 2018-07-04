def search4vowels(phrase: str) -> set:
    """ Display any vowels found in supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ Retrun a set of the 'letters' founbd in 'phrase'."""
    return set(letters).intersection(set(phrase))
