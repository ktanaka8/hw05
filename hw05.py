"""
Name: (put your name here)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter(l):
    """ Add your own Docstring """
    # remove the default return and add your code
    while len(l) != 1 or (l not in {"A", "B", "C"}):
        if len(l)==1:
            if l in {"A", "B", "C"}:
                continue
            else:
                print("Error: You provided the wrong character.")
                l = input("Give a single uppercase letter: ")
        else:
            print("Error: it needs to be a single character.")
            l = input("Give a single uppercase letter: ")
    return l

def get_digit(n):
    """ Add your own Docstring """
    # remove the default return and add your code
    while not n.isdigit() or n not in range(1,4):
        if n.isdigit():
            n_int = int(n)
            if 1 <= n_int <= 3:
                return n_int
            else:
                print("Error: a single digit needs to be in [1,3].")
                n=input("Give an single number character: ")
        else:
            print("Error: your input should be only digits.")
            n = input("Give an single number character: ")
    return n_int

def check_pattern(letter, digit, lst):
    """ Add your own Docstring """
    # remove the default pass and add your code
    pass


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
    user_let = input("Give a single uppercase letter: ")
    user_let = get_letter(user_let)
    user_num = input("Give an single number character: ")
    user_num = get_digit(user_num)

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()