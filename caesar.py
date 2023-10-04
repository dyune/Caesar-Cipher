

import string
from string import *

def read_word_list(file_name):
    '''
    file_name (str): the name of the file containing the list of words to load.
    Returns: a set of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    '''
    in_file = open(file_name, 'r') # in_file: file
    line = in_file.readline()      # line: str
    word_list = line.split()       # word_list: list of str
    in_file.close()
    return frozenset(word_list)    # creates an immutable set.

N_LETTERS = len(string.ascii_lowercase)
VALID_WORDS = read_word_list('words.txt')

#print((dict(zip(dict.fromkeys(ascii_lowercase+ascii_uppercase,0),list(range(26)) + list(range(26))))))
def create_shift_table(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a character shifted down the alphabet by the input shift. 
    The dictionary should have 52 keys of all the uppercase letters and all the lowercase letters only.          
    shift (int): the amount by which to shift every letter of the alphabet, 0 <= shift < N_LETTERS. 
    If shift is less than zero or greater than or equal to N_LETTERS, this function should return None.
    Returns: a dictionary mapping a letter (str) to another letter (str), for all lower and upper case letters.
    '''
    if 0<= shift < N_LETTERS: # As required. [0, 26)
        encrypted={} 
        encryptionindexes=(dict(zip(dict.fromkeys(ascii_lowercase+ascii_uppercase,0),list(range(26)) + list(range(26)))))
        
        for char in list(ascii_lowercase+ascii_uppercase):
            newindex=encryptionindexes.get(char) + shift 
        
            if newindex<(N_LETTERS-1): 
    
                if char.isupper():
                    encrypted[char]=ascii_uppercase[newindex]

                else:
                    encrypted[char]=ascii_lowercase[newindex]
                    
                newindex=newindex-(N_LETTERS)
 
                if char.isupper():
                    encrypted[char]=ascii_uppercase[newindex]
                else:
                    encrypted[char]=ascii_lowercase[newindex]
            newindex=0
        return encrypted
    
    else:
        return None

def apply_shift(original_text, shift):
    '''
    Applies the Caesar Cipher to original_text with the input shift.
    Creates a new string that is original_text shifted down the alphabet by some number of characters determined by the input shift 
    shift (int): the shift with which to encrypt the message.
    0 <= shift < N_LETTERS
    Returns: the message text (str) in which every character is shifted
             down the alphabet by the input shift
    '''
    encrypted=create_shift_table(shift)
    # Obtain a dictionary with shifts for each original letter and their new encrypted version.
    encrypted_word=''
    for char_index in range(len(original_text)):
        if original_text[char_index].isalpha():
            encrypted_word+=encrypted[original_text[char_index]]
            # Encrypted[letter] returns the encrypted version of it.
        else:
            encrypted_word+=original_text[char_index]
            # Preserve non-alphanumeric elements since we have no shifting assigned for them.
    return encrypted_word

def encrypt_message(original_text, shift):
    '''
    Used to encrypt the message using the given shift value.  
    Returns: The encrypted string.
    '''
    return apply_shift(original_text, shift)


def all_strip(x):
    new_str=''
    for char in x:
        if char.isalnum():
            new_str+=char
    return new_str

def is_word(word):
    '''
    Determines if word is a valid word, ignoring capitalization, punctuation, and possible spaces.  
    word (str): a possible word.
    Returns: True if word is in word_list, False otherwise
    '''
    if all_strip(word.lower()) in VALID_WORDS:
        return True
    else:
        return False

def decrypt_message(cipher_text):
    '''
    Decrypt cipher_text by trying every possible shift value and find the "best" one. We will define "best" as the shift that
    creates the maximum number of real words when we use apply_shift(shift) on the text. If s is the original shift value used to encrypt
    the message, then we would expect N_LETTERS - s to be the best shift value for decrypting it.
    Note: if multiple shifts are equally good such that they all create the maximum number of words, you may choose any of those shifts (and 
    their corresponding decrypted messages) to return
    Returns: a tuple of the best shift value used to decrypt the message
    and the decrypted message text using that shift value.
    '''
    attempt_logs={}
    for shift_try in range(0,N_LETTERS):
        attempt=apply_shift(cipher_text, shift_try).split()
        # So we can iterate over each word in the attempted decryption.
        valid_count=0
        for word in attempt:
            if is_word(word):
                valid_count+=1
        attempt_logs[' '.join(attempt)]=(valid_count, shift_try)
        # Key = string of decryption, value = tuple(number of words, shift number)
    result=(attempt_logs.get(max(attempt_logs, key=lambda nbr: attempt_logs[nbr]))[1],max(attempt_logs, key=lambda nbr: attempt_logs[nbr]))
 
    return result


