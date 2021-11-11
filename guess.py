#!/usr/bin/env python3
import random


def play_game(secret):
    print('Myslím si číslo od "1" do "20".')
    tip = None
    lives = 5

    while lives > 0 and tip != secret:
        tip = int(input('\nTvoj tip: '))
        if tip < secret:
            print('Hmm... Moje číslo je väčšie ako tvoje.')
            lives -= 1
            print(lives)
        elif tip > secret:
            print('Hmm... Moje číslo je menšie ako tvoje.')
            lives -= 1
            print(lives)
        else:
            print('Gratulujem! Uhádol si!')
            break
    else:
        print(f'Neuhádol si! Správna odpoveď je {secret}.')


if __name__ == '__main__':
    play = 'ano'
    while play in ('a', 'ano', 'y', 'yes'):
        play_game(random.randint(1, 20))
        play = input('\nChceš hrať znova? (ano/nie): ').lower().lstrip().rstrip()
    else:
        print('\nĎakujem za hranie. Dovidenia!')
        print('Autor: Dárius Lindvai')
