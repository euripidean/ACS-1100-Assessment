"""
Banking App
"""
users = {}
attempts = 3
def load_data(file):
    """
    Loads in data file and sets values to dictionary of users
    Returns:
        Dictionary of users storing username, password, fullname and balance for each line item.
    """
    file_to_read = open(file, 'r', encoding="utf")
    user_data = file_to_read.readlines()
    file_to_read.close()
    i = 0
    for line in user_data: # builds indexed dictionary of users
        user = line.split(',')
        users[i] = {}
        users[i]['username'] = user[0]
        users[i]['password'] = user[1]
        users[i]['fullname'] = user[2]
        users[i]['balance'] = int(user[3])
        i += 1

def display():
    """
    Displays asterisks to break up interface.
    Returns:
        String of asterisks.
    """
    print('*' * 100 + '\n')

def log_in():
    """
    Displays log in prompts for user.
    Returns:
        Passes through inputs to validation function as arguments.
    """
    username = input('Please enter your user name: > ')
    password = input('Please enter your password: > ')
    validate_user(username, password)

def validate_user(username, password):
    """
    Validates the user name and password provided.
    Returns:
        If false, returns error message and prompts user to try logging in again.
        If true, displays balance. Incorrect log in attempts increment the attempt limit.
        If increment limit of attempts are reached, program exits.
    """
    global attempts
    validation = False
    # Set log in attempts to zero, but must be global otherwise would reset each log_in call.
    while validation is False:
        for user, data in users.items():
        #Check to see if password and username match records
            if data['username'] == username and data['password'] == password:
                account = user
                validation = True # exit while loop on next iteration
                display()
                view_account(account) # takes index of account and uses it to display information.
                return
        attempts -= 1
        if attempts > 1:
            print('Your username or password is incorrect. Please try again.')
            print(f'You have {attempts} attempts remaining.')
            log_in()
        elif attempts == 1: #Final warning
            print('You have one final log in attempt remaining.')
            print('If you are unsuccessful, your account will be locked.')
            log_in()
        else:
            display()
            print('Please call customer service.')
            print('The account you are trying to access is now locked.')
            display()
            exit()

def view_account(user):
    """
    Displays account balance.
    Returns:
        String: Full name of user and balance.
    """
    balance = users[user]['balance']
    fullname = users[user]['fullname']
    display()
    print(f'Hi there {fullname}! Your balance is currently ${balance}')
    display()
    banking_options(user)

def make_deposit(user):
    """
    Takes input for user as to value they would like to deposit.
    Adds deposit to balance and updates user balance in dictionary.
    Returns:
        String of deposit and balance. Updates balance in  users dictionary.
    """
    deposit = int(input('What amount would you like to deposit? >'))
    balance = (users[user]['balance'])
    new_balance = balance + deposit
    users[user]['balance'] = new_balance # ensures new balance updates the user dictionary
    print(f'You successfully deposited ${deposit}. Your new balance is ${new_balance}.')
    display()
    banking_options(user) #returns user to main menu

def withdraw_funds(user):
    """
    Takes input for user as to value they would like to withdraw.
    If withdrawal amount will take balance under 0, prompts for re-entry.
    Substracts withdrawal to balance and updates user balance in dictionary.
    Returns:
        String of deposit and balance. Updates balance in users dictionary.
    """
    withdrawal = int(input('What amount would you like to withdraw? >'))
    balance = int(users[user]['balance'])
    while balance - withdrawal < 0: # Does not permit withdrawal that will make user overdrawn
        print('You have insufficient funds to withdraw that amount.')
        print('Please try again.')
        withdrawal = int(input('What amount would you like to withdraw? >'))
    new_balance = balance - withdrawal
    users[user]['balance'] = new_balance #updates balance in user dictionary
    print(f'You successfully withdrew ${withdrawal}. Your new balance is ${new_balance}.')
    display()
    banking_options(user) #returns user to main menu


def validate_transfer_user(sender):
    """
    Checks that the user to be transferred to is valid and not the sender.
    Returns:
        Passes verified recipient and sender into transfer funds function.
    """
    recipient = input('Please enter the name of the user you would like to transfer to: > ')
    validation = False
    while validation is False:
        for user, data in users.items():
            #ensures recipient is user and is not sender user
            if recipient == data['username'] and recipient != users[sender]['username']: 
                recipient = user
                validation = True
                transfer_funds(recipient, sender) #sends on to function handling transfer
        print('Please enter a valid user')
        recipient = input('Please enter the name of the user you would like to transfer to: > ').lower()


def transfer_funds(recipient, sender):
    """
    Takes transfer amount as input form user. If transfer will take balance under 0, requests
    re-entry.
    Transfer amount is substracted from sender balance and added to recipient balance.
    Returns:
        String: Confirms transfer amount and recipient. Confirms new sender balance.
    """
    sender_balance = int(users[sender]['balance'])
    transfer_amount = int(input('What amount would you like to transfer? > '))
    while sender_balance - transfer_amount < 0: #ensures transfer will not make user overdrawn
        print('You cannot transfer that amount. Please enter another value > ')
        transfer_amount = int(input('What amount would you like to transfer? > '))
    new_sender_balance = int(users[sender]['balance']) - transfer_amount
    users[sender]['balance'] = new_sender_balance
    recipient_name = users[recipient]['fullname']
    display()
    print(f'Your transfer of ${transfer_amount} to {recipient_name} has been successful.')
    print(f'Your new balance is ${new_sender_balance}.') #confirms sender balance
    display()
    banking_options(sender) #returns user to main menu, feeding in sender to keep their validated session alive

def banking_options(user):
    """
    Prompts user to choose what they would like to do in their account.
    Returns:
        User entry determines function they enter:
        make deposit, withdraw funds or validate transfer.
        Exits program if option 4 is selected.
    """
    options = [1,2,3,4]
    print('Press 1 to Make a Deposit.')
    print('Press 2 to Withdraw Funds.')
    print('Press 3 to Transfer Funds.')
    print('Press 4 to exit.')
    user_choice = int(input('Choose your option > '))
    while user_choice not in options:
        user_choice = int(input('Please choose 1, 2, 3 or type 4 to exit'))
    if user_choice == 1:
        make_deposit(user)
    elif user_choice == 2:
        withdraw_funds(user)
    elif user_choice == 3:
        validate_transfer_user(user)
    else:
        display()
        print('Thank you for using our service.')
        display()
        return

def accrue_interest(rate):
    """
    Doc String
    """
    for data in users.values():
        percentage = rate/100
        balance = data['balance']
        new_balance = balance + data['balance']*percentage
        data['balance'] = new_balance
        balance = new_balance
        full_name = data['fullname']
        print(f'After interest accrual the new balances are: {full_name} --> ${balance:.2f}.')
        display()

# Function Calls
FILE = 'data.txt'
load_data(FILE)
log_in()
accrue_interest(2)
