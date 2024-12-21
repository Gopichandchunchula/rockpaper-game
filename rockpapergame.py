import random

def user_input():
    ui = input('Enter your choice: Rock, Paper, or Scissors: ').lower()
    if ui not in ['rock', 'paper', 'scissors']:
        print('Invalid option. Please try again.')
        return None
    else:
        print(f'Your choice is {ui}.')
        return ui

def computer_input():
    ci = random.choice(['rock', 'paper', 'scissors'])
    print(f'Computers choice is {ci}.')
    return ci

def rps(ui, ci):
    if ui == ci:
        print('It is a tie!')
    elif (ui == 'rock' and ci == 'scissors') or (ui == 'paper' and ci == 'rock') or (ui == 'scissors' and ci == 'paper'):
        print('You win!')
    else:
        print('You lose!')

print('Welcome to the Rock, Paper, Scissors Game!')   
while True:
    userinput = user_input()
    if userinput:
        computerinput = computer_input()
        rps(userinput, computerinput)
    
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        print('Thanks for playing! Goodbye!')
        break
