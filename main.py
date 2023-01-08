import random 

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1   

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 9
}

symbol_value = {
    "A": 5,
    "B": 3.5,
    "C": 2.5,
    "D": 1.5
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] 
        for column in columns:
            symbol_to_check = column[line] 
            if symbol != symbol_to_check: # if not the same, break (and check other lines if there are any)
                break
        else:       # if they are the same they win, and the else statement runs
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols): # Generate slot machine items
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items gives u both the key(symbol) and value (symbol_counter)
        for _ in range(symbol_count): #looping through the symbol count = anonomus value
            all_symbols.append(symbol)

    columns = []                    
    for _ in range(cols):                 # generate a column for every single column we have
        column = []                     
        current_symbols = all_symbols[:]            # [:] slice operator, current symbols(the one we can choose from) is a copy of all symbols
        for _ in range(rows):                 
            value = random.choice(current_symbols)             
            current_symbols.remove(value)                   
            column.append(value)                 

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): 
        for i, column in enumerate(columns): 
            if i != len(columns) -1: 
                print(column[row], end=" | ") # default of end is \n (moves to the next line) after every since column,we only wanna do it after every since row so we add |
            else:
                print(column[row], end="")
        print()
    
def deposit():  # responsible for collecting user input that gets the deposit from the user
    while True: 
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount) 
            if amount > 0:  
                break 
            else: 
                print("Amount must be greater than 0.")

        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines(): # we ask to pick a number 1-3
    while True: 
        lines = input("Enter the amount of lines to bet on (1-" + str(MAX_LINES) + ")? ") # convert to a str bcz 1 is a string, otherwise a problem would occur.
        if lines.isdigit():  
            lines = int(lines)  
            if 1 <= lines <= MAX_LINES:
                break # 
            else: 
                print("Enter a valid number of lines. ") # otherwise we print this

        else:
            print("Please enter a number.") # if its not a number we print this

    return lines

def get_bet():
    while True: 
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET <= amount <= MAX_BET:  
                break 
            else: 
                print(f"Amount must be between. ${MIN_BET} - {MAX_BET}.") # auto converted to a string (if it can)

        else:
            print("Please enter a number.") 

    return amount
    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines) # * = unpack/splat operator, passes every single line from winning lines to the print function
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You're left with ${balance}")

main() # start running main
# btw type cls to clear when u run

