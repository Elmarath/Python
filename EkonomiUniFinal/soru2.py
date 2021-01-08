# check if the string is palindrome

def is_palindrom(string):
    rev_string = string[::-1]
    if rev_string == string:
        return True
    else:
        return False


pal_list = []

run = True

while run:
    # get a string
    u_string = str(input("Enter a string\n"))    # unchecked string

    # check if the string is "STOP"
    if u_string == 'STOP':
        print('Quiting the program...')
        run = False

    # if not check if it is palindrom
    elif is_palindrom(u_string):
        # print out if it is palindrom
        print("Palindrom: ", u_string)

        # add to the palindrom list
        pal_list.append(u_string)

if(len(pal_list) == 0):
    print("There is nothing in the list ")

else:
    # find the longest palindrom from the list
    longest_string = max(pal_list, key=len)

    # print the longest palindrom of the list
    print("Longest of the palindroms is:")
    print(longest_string)
