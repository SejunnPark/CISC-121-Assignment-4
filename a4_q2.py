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
    inputted strings follow the directed requirements then turns them into
    a matching prime number then sorts its
    """

    print('This program will first convert the string the user enters into a matching prime number ')
    print('Then sort it in increasing order using radix sort')
    print('Enter two strings below that contain ONLY upper-case letters and no spaces: ')

    user_input1 = input('Enter String 1: ')
    user_input2 = input('Enter String 2: ')

    if type(user_input1) == str and type(user_input2) == str and user_input1.isupper() and user_input2.isupper():

        string1_list = []
        for i in user_input1:
            num1 = functions.char_prime(i)
            string1_list.append(num1)

        string2_list = []
        for j in user_input2:
            num2 = functions.char_prime(j)
            string2_list.append(num2)

        sort_list = string1_list + string2_list
        print(sort_list)

        d = functions.radix_sort(sort_list)
        print('Here is the new sorted prime number list:', d)

    else:

        print('Error. Did not input a string or string was not all upper-case or the string contained spaces...')


main()
