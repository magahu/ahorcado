from ahorcado import *

def main():
    welcome()

    while True:
        op = get_option()
        spaces_to_complete = []
        ahorcado_parts = len(FIGURES)-1
        i = 0

        if op == 'N':
            intro_message()

            word = generate_word()
            hiden_word = generate_hiden_word(word)
            spaces_to_complete = hiden_word[:]

            display_ahorcado(i)
            display_gameboard(hiden_word)

            while i < ahorcado_parts:
                user_letter = get_user_letter()
                hiden_word = check_word(word, user_letter, hiden_word)
                check_letter(user_letter, word)
                i = check_life(i, word, user_letter)
                display_actual_gameboard(i, hiden_word)
                spaces_to_complete = user_inputs(user_letter, word, spaces_to_complete)

                if ''.join(spaces_to_complete) == word:
                    congrats()
                    break

                if i == ahorcado_parts:
                    game_over(word)

        elif op == 'I':
            instructions()

        elif op == 'E':
            break

        else:
            print('\nPlease, select a valid option\n')

if __name__ == '__main__':
    main()

