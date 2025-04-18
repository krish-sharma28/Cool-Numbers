import webbrowser
import sys

def main():
    key = 0
    welcome_string = """Welcome to 24! \n \
    The game of adding, subtracting, multiplying, and dividing 
    4 numbers to reach 24."""
    
    # handle logic for leaderboard, help, and play
    while key == 0:
        print(welcome_string)
        gather = input("What would you like to do? ")
        print(gather)
        if gather.lower() == 'leaderboard':
            leaderboard()
        elif gather.lower() == 'rules':
            help()
        elif gather.lower() == 'play':
            c_result = card()
            key = 1
            break
        elif gather.lower() == 'exit':
            return print("Exiting program.")
        else:
            print("""Not a valid input! Choose between leaderboard, rules, 
                  and play. Write 'exit' at any time to end program.""")
    while key == 1:
        print("-----------------")
        print(f"| {c_result[0]} | {c_result[1]} | {c_result[2]} | {c_result[3]} |")
        print("-----------------")
        gather = input("Enter your answer in reverse polish notation. ")
        
        if score(gather):
            print("Yippee!")
            key == 0
        elif gather.lower() == 'exit':
            return print("Exiting program.")
        else:
            print("Incorrect! Try Again!")
            pass
        
def leaderboard():
    pass

def help():
    site = "https://mathworld.wolfram.com/ReversePolishNotation.html"
    string = """After typing 'play' into the prompt box, you will be greeted 
    with a card. \n 
    ----------------- \n 
    | 2 | 3 | 2 | 4 | \n 
    ----------------- \n 
    To play, enter your expression in reverse polish notation (RPN). \n 
    If you do not know RPN, type 'RPN' into the text box. 
    Otherwise, type 'return' """
    print(string)
    gather = input("What would you like to do? ")
    if gather.lower() == 'exit':
        print("Exiting program.")
        sys.exit()
    if gather.lower() == "rpn":
        webbrowser.open_new(site)
        return
    if gather.lower() == "return":
        return
    else:
        print("not an option, oh well.")
        return
        
    
def card():
    stuf = [2,3,2,4]
    return stuf

def score(string):
    return False

if __name__ == "__main__":
    main()