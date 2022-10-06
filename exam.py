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
    for line in user_data:
        user = line.split(',')
        users[i] = {}
        users[i]['username'] = user[0]
        users[i]['password'] = user[1]
        users[i]['fullname'] = user[2]
        users[i]['balance'] = user[3]
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
        If false, returns error message and prompts user to try logginglog in again.
        If true, displays balance. Incorrect log in attempts increment the attempt limit.
    """
    global attempts
    validation = False
    # Set log in attempts to zero, but must be global otherwise would reset each log_in call.
    while validation is False:
        for user, data in users.items():
        #Check to see if password and username match records
            if data['username'] == username and data['password'] == password:
                account = user
                validation = True
                display()
                view_account(account)
                return
        attempts -= 1
        if attempts > 1:
            print('Your username or password is incorrect. Please try again.')
            print(f'You have {attempts} attempts remaining.')
            log_in()
        elif attempts == 1:
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
    """
    balance = users[user]['balance']
    fullname = users[user]['fullname']
    display()
    print(f'Hi there {fullname}! Your balance is currently ${balance}')
    display()
    banking_options(user)

def make_deposit(user):
    """
    Docstring
    """
    print(user)
    print('Make a desposit, you filthy animal.')

def withdraw_funds(user):
    """
    Doc string
    """
    print(user)
    print('Withdraw it all!')

def transfer_funds(user):
    """
    Doc string
    """
    print(user)
    print('Transfer it all to me, dude.')

def banking_options(user):
    """
    Prompts user to choose what they would like to do in their account.
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
        transfer_funds(user)
    else:
        print('Thank you for using our service.')
        exit()

# Function Calls
FILE = 'ACS-1100-Assessment/data.txt'
load_data(FILE)
log_in()
