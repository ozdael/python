def search4vowels(phrase:str) -> set:
    """ Display any vowels found in supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
    
