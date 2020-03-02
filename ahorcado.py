import random
from figures import FIGURES
from words import WORDS

def welcome():
    print('{}  W E L C O M E  T O  A H O R C A D O  {}'.format(' * '*3, ' * '*3))


def get_option():
    option = input('''
    Select one of the following options:
    [N] NEW GAME
    [I] Instructions
    [E] EXIT
    Enter your choise: ''').upper()
    return option


def intro_message():
    deco = '*'
    message = '{} G A M E   S T A R T E D! {}'.format(deco*5, deco*5)
    print('\n\n{}'.format(deco*len(message)))
    print('{}'.format(message))
    print(deco*len(message))


def generate_word():
    i = random.randint(0, len(WORDS)-1)
    return WORDS[i]


def generate_hiden_word(word):
    hiden_word = []
    #print(word)
    for letter in word:
        hiden_word.append(' ___ ')
    return hiden_word


def display_ahorcado(i):
    print(FIGURES[i])


def display_gameboard(hiden_word):
    print(''.join(hiden_word))


def get_user_letter():
    letter = None
    while not letter:
        letter = input('\nEnter a letter: ')
    return letter.lower()


def user_inputs(user_letter, word, spaces_to_complete):
    for i in range(len(word)):
        if word[i] == user_letter:
            spaces_to_complete[i] = user_letter
    return spaces_to_complete
    complete_word.append(user_letter)
    return complete_word


def check_word(word, user_letter, hiden_word):
    for i in range(len(word)):
        if word[i] == user_letter:
            hiden_word[i] = ' _{}_ '.format(user_letter)
    return hiden_word


def check_life(i, word, user_letter):
    for letter in word:
        if letter.lower() == user_letter.lower():
            return i
    i+=1
    return i


def check_letter(user_letter, word):
    repeated_letters = 0
    for letter in word:
        if letter == user_letter.lower():
             repeated_letters += 1
    if repeated_letters < 1:
        return 'Letter {} ISN\'T in the hiden word'
    else:
        return 'letter {} appears {} times'.format(user_letter, repeated_letters)


def display_actual_gameboard(i, hiden_word):
    print(FIGURES[i])
    print(''.join(hiden_word))


def congrats():
    deco = '*'
    message = "{} C O N G R A T S! {}".format(deco*10, deco*10)
    print('\n\n{}'.format(message))
    print("\nYOU'VE FOUND THE HIDEN WORD IN TIME!\n")
    print(deco*len(message))

def game_over(word):
    deco = '*'
    message = "{} G A M E   O V E R {}".format(deco*10, deco*10)
    print('\n\n{}'.format(message))
    print('\nThe hiden word was: {}\n'.format(word.upper()))
    print(deco*len(message))

def instructions():
    title = '{} I N S T R U C T I O N S {}'.format('*'*20, '*'*20)
    print('\n{}'.format(title))
    print("\nFind the secret word before the 'ahorcado' appears!\nYou only can input  one letter by turn.\n")
    print('*'*len(title))
