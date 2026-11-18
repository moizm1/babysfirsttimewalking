#!/usr/bin/env python
# coding: utf-8

# In[3]:


def are_u_string(text):
    '''
    (str) --> bool

    A function that checks if an input is a string or not and prints a message if it is not.

    >>> are_u_string("idk")
    True
    >>> are_u_string(im not)
    "Invalid input, text is not a string")
    False
    '''
    if type(text) is not str:
        print("Invalid input, text is not a string")
        return False

#are_u_string(12345678)
#are_u_string('of course')


# In[13]:


def first_and_last(text):
    '''
    (str) --> str

    A function that reutrns a string made of the first and last characters the input string. If the string is empty returns an empty string.

    >>> first_and_last("Python")
    "Pn"
    >>> first_and_last("A")
    "AA"
    >>> first_and_last("")
    ""
    '''
    if are_u_string(text) == False:
        return None

    elif text == "":
        return text
    else:
        return text[0] + text[-1]

#first_and_last("Python")
#first_and_last("A")
#first_and_last("")
#first_and_last(True)



# In[5]:


def reverse_text(text):
    '''
    (str) --> str

    A function that returns a string written backwards

    >>> reverse_text("hello")
    "olleh"
    '''
    if are_u_string(text) == False:
        return None
    else:
        return text[::-1]

#reverse_text("hello")
#reverse_text('123456789')
#reverse_text("")


# In[6]:


def is_palindrome(text):
    '''
    (str) --> (bool)

    A function that determines whether a strings reads the same fowards and backwards, igrnoring case and spaces. Reutrns True if it does and false if not.

    >>> is_palindrome("Race car")
    True
    >>> is_palindrome("Python")
    False
    '''
    if are_u_string(text) == False:
        return None

    #Remove the spaces and normalize the case to evaluate if it is a palindrome
    clean_text = text.strip().lower().replace(" ", "")

    if clean_text == clean_text[::-1]:
        return True
    else:
        return False

#is_palindrome("Race car")
#is_palindrome("Python")
#is_palindrome(3.0)
#is_palindrome("")


# In[7]:


def swap_case_halves(text):
    '''
    (str) --> str

    A function that reutrns a new string where the first half of the input is uppercase and the second half is lowercase leaves non-alphabetic characters remain unchanged although they are counted. If the length is odd, the middle character belongs to the first half.

    >>> swap_case_halves("abcdef")
    "ABCdef"
    >>> swap_case_halves("abcde")
    "ABCde"
    '''
    if are_u_string(text) == False:
        return None

    #Determine the halfway point of the string to simplify the return, add one to account for odd numbers and floor division for even numbers which will have had one added
    halfway_index = (len(text) + 1) // 2

    #Slice the string into its components and apply the appropiate case then return the combined result
    return text[:halfway_index].upper() + text[halfway_index:].lower()

#swap_case_halves("abcdef")
#swap_case_halves("abcde")
#swap_case_halves("I really hope this works 100%")



# In[11]:


def censor_word(text, word):
    '''
    (str, str) --> str

    A function that returns a copy of the input text with every occurence of word replaced by asteriks (*), one asterik per letter of word. Case senstive.

    >>> censor_word("the cat sat with the cat", "cat")
    "the *** sat with the ***"
    '''
    if are_u_string(text) == False or are_u_string(word) == False:
        return None

    return text.replace(word, "*" * len(word))

#censor_word("the cat sat with the cat", "cat")
#censor_word("Hello World", "world")
#censor_word("", "cat")


# In[9]:


def count_occurrences(text, char):
    '''
    (str, str) --> int

    A function that counts the number of times char appears in the text, not case sensitive.

    >>> count_occurrences("Mississippi", "s")
    4
    '''
    if are_u_string(text) == False:
        return None

    #Normalize the case
    text = text.lower()
    char = char.lower()

    return text.count(char)

#count_occurrences("Mississippi", "s")
#count_occurrences("Banana", "A")
#count_occurrences("", "a")


# In[12]:


#TEST
sentence = input("Enter a sentence: ")
print("First and last:", first_and_last(sentence))
print("Reversed:", reverse_text(sentence))
print("Is palindrome:", is_palindrome(sentence))
print("Half-case swap:", swap_case_halves(sentence))

word_to_censor = input("Word to censor: ")
print("After censoring:", censor_word(sentence, word_to_censor))

char_to_count = input("Character to count: ")
print(f"Occurrences of '{char_to_count}':", count_occurrences(sentence, char_to_count))


# In[ ]:




