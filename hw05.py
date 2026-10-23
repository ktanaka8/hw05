"""
Name: (put your name here)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter(letter):
    """ Add your own Docstring """
    # remove the default return and add your code
    while len(letter) != 1 or (letter not in {"A", "B", "C"}):
        if len(letter)==1:
            if letter in {"A", "B", "C"}:
                continue
            else:
                print("Error: You provided the wrong character.")
                letter = input("Give a single uppercase letter: ")
        else:
            print("Error: it needs to be a single character.")
            letter = input("Give a single uppercase letter: ")
    return letter

def get_digit(digit):
    """ Add your own Docstring """
    # remove the default return and add your code
    while not digit.isdigit() or digit not in range(1,4):
        if digit.isdigit():
            n_digit = int(digit)
            if 1 <= n_digit <= 3:
                return n_digit
            else:
                print("Error: a single digit needs to be in [1,3].")
                digit=input("Give an single number character: ")
        else:
            print("Error: your input should be only digits.")
            digit = input("Give an single number character: ")
    return n_digit

def check_pattern(letter, digit, lst):
    """ Add your own Docstring """
    # remove the default pass and add your code
    sequence = letter+str(digit)
    sp_sequence = letter+"@"+str(digit)
    print("Strings with the pattern:")
    print()
    for phrase in lst:
        if (sp_sequence in phrase) or (sequence in phrase):
            print(phrase, end=" ")
        else:
            continue
    print ()


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    letter = input("Give a single uppercase letter: ")
    letter = get_letter(letter)
    digit = input("Give an single number character: ")
    digit = get_digit(digit)
    check_pattern(letter, digit, st_list)
    choice = input("Try Again? (y/n): ")
    while choice == "y":
        letter = input("Give a single uppercase letter: ")
        letter = get_letter(letter)
        digit = input("Give an single number character: ")
        digit = get_digit(digit)
        check_pattern(letter, digit, st_list)
        choice = input("Try Again? (y/n): ")
    

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()