"""
    CISC-121 2023W
    Name:   Jun Park
    Student Number: 20351229
    Email:  21sp111@queensu.ca
    Date: 2023-03-15

    I confirm that this assignment solution is my own work and conforms to
    Queen’s standards of Academic Integrity
"""

import functions


def main():
    """
    This is the main function, which serves as an execution point for
    all the functions within the program this function also checks if the
    inputted strings follow the directed requirements then shows if the strings
    inputted are anagrams
    """

    print('This program will determine if the strings you have entered are Anagrams')
    print('Enter two strings below that contain ONLY upper-case letters and no spaces: ')

    user_input1 = input('Enter String 1: ')
    user_input2 = input('Enter String 2: ')

    if type(user_input1) == str and type(user_input2) == str and user_input1.isupper() and user_input2.isupper():

        result = functions.is_anagram(user_input1, user_input2)

        if result:

            print('The two strings you have entered are Anagrams! ')

        else:

            print('The two strings you have entered are not Anagrams... ')
    else:

        print('Error. Did not input a string or string was not all upper-case or the string contained spaces...')


main()
