def cipher(text, shift, encrypt=True):
    """Uses a basic shift (Caesar) cipher to encrypt text input.

    Parameters
    ----------
    text : str
        Text to be encrypted
    shift : int
        How many positions down the alphabet should the text be shifted?
    encrypt: bool
        Default: True
        If true, cipher shifts text positionally down the alphabet
        If false, cipher shifts text positionally up the alphabet

    Returns
    -------
    new_text : str
        Encrypted (or decrypted) text

    Examples
    --------
    >>> cipher("I have the best words", 3)
    'L kdyh wkh ehvw zrugv'
    >>> cipher("L kdyh wkh ehvw zrugv", 3, encrypt=False)
    'I have the best words'
    """
    assert isinstance(shift, (int, float)) #part e
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text




##

