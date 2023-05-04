"""
    CISC-121 2023W
    Name:   Jun Park
    Student Number: 20351229
    Email:  21sp111@queensu.ca
    Date: 2023-03-15

    I confirm that this assignment solution is my own work and conforms to
    Queen’s standards of Academic Integrity
"""


def char_prime(my_char):
    """
    -------------------------------------------------------
    Converts an uppercase letter to a unique prime number
    Based on the conversion given in the footnote
    -------------------------------------------------------
    Parameters:
        my_char - a char in ABCDEFGHIJKLMNOPQRSTUVWXYZ (char)
    Returns:
        prime_int = a prime number unique to the letter
    -------------------------------------------------------
    """

    prime_dict = {'A': 2, 'B': 3, 'C': 5, 'D': 7, 'E': 11, 'F': 13, 'G': 17, 'H': 19,
                  'I': 23, 'J': 29, 'K': 31, 'L': 37, 'M': 41, 'N': 43, 'O': 47, 'P': 53, 'Q': 59,
                  'R': 61, 'S': 67, 'T': 71, 'U': 73, 'V': 79, 'W': 83, 'X': 89, 'Y': 97, 'Z': 101}

    for i in prime_dict:
        if my_char == i:
            return prime_dict[i]    # returning the corresponding integer


def primeify(my_string):
    """
    -------------------------------------------------------
    RECURSIVELY gives the product of primes corresponding to
    the letters in the string
    -------------------------------------------------------
    Parameters:
        my_string - any string (str)
    Returns:
        prime_product = the product of all primes for each letter
    -------------------------------------------------------
    """

    if len(my_string) == 0:

        return 1

    else:
        rn_prime = char_prime(my_string[0])    # turn first character to prime number
        prime_product = primeify(my_string[1:])  # primeify function called so we can do this with next character
        prime_product *= rn_prime
        return prime_product


def is_anagram(string1, string2):
    """
    -------------------------------------------------------
    Determines if two strings are anagrams of each other
    -------------------------------------------------------
    Parameters:
        string1, string2 - any two strings (str)
    Returns:
        is_anagram = whether or not they are anagrams (Boolean)
    -------------------------------------------------------
    """

    # 'BAD' and 'DAB'

    primeify_str_one = primeify(string1)
    primeify_str_two = primeify(string2)

    if primeify_str_one == primeify_str_two:    # if the products equal each other they are anagrams
        return True

    else:
        return False


def counting_sort(sort_list, pen):
    """
    -------------------------------------------------------
    This function sorts the list of prime numbers given the
    original list and the highest number from the list
    -------------------------------------------------------
    Parameters:
        list of prime numbers
    Returns:
        highest number from the prime number list
    -------------------------------------------------------
    """

    output = [0] * len(sort_list)     # this will be used to store the sorted list
    count = [0] * 10

    for x in range(len(sort_list)):
        num = (sort_list[x] // pen) % 10  # extract digit in the current place value (pen)
        count[num] += 1      # count of each digit is incremented in the count list

    for y in range(1, 10):
        count[y] += count[y - 1]    # cumulative count of elements up to each index

    z = len(sort_list) - 1
    while z >= 0:
        num = (sort_list[z] // pen) % 10
        p = count[num] - 1   # calculates index where current element should be placed
        output[p] = sort_list[z]
        count[num] -= 1    # decrement after each element is placed in 'output' list
        z -= 1      # decrements loop counter z

    for i in range(len(sort_list)):
        sort_list[i] = output[i]


def radix_sort(sort_list):
    """
    -------------------------------------------------------
    This function provides the parameters for the counting_sort
    function and then returns the new sorted list of prime
    numbers
    -------------------------------------------------------
    Parameters:
        list of prime numbers
    Returns:
        sorted list of prime numbers
    -------------------------------------------------------
    """

    max_num = max(sort_list)
    # need the highest number so the program knows the number with
    # the highest place value

    for pen in range(1, 10 ** (max_num - 1)):
        counting_sort(sort_list, pen)

    return sort_list
