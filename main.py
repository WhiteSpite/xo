def showGame():
    print('     0 1 2')
    print(f'   0 {game_table["00"]} {game_table["10"]} {game_table["20"]}')
    print(f'   1 {game_table["01"]} {game_table["11"]} {game_table["21"]}')
    print(f'   2 {game_table["02"]} {game_table["12"]} {game_table["22"]}')


def choise(items, text):
    choise = input(text)
    while choise not in items or choise in game_table and game_table[choise] != '-':
        choise = input('   Некорректный выбор! Попробуй еще раз!: ')
    return choise


def clear_console():
    print('\n' * 100)


def clear_game():
    global game_table, win, first_player_turn
    game_table = {k: '-' for k in [str(i) + str(j) for i in range(3) for j in range(3)]}
    win = False
    first_player_turn = True
clear_game()


def clear_counters():
    global counter1, counter2, counter3
    counter1 = counter2 = counter3 = 0
clear_counters()




start = choise(('0', '1'), "-- Добро пожаловать в игру Крестики-нолики!\n   1. Начать\n   0. Выход\n\n   Ввод: ")

if int(start):
    play = True
else:
    clear_console()
    exit()

while play:
    clear_console()
    showGame()
    if first_player_turn:
        playerNum = 1
        mark_name = 'крестик'
        mark = 'x'
        first_player_turn = False
    else:
        playerNum = 2
        mark_name = 'нолик'
        mark = 'o'
        first_player_turn = True
    mark_place = choise(game_table,
                        f"\n-- Игрок {playerNum} выбирает, куда поставить {mark_name}. Введите координаты в формате 'xy'.\n\n   Ввод: ")
    game_table[mark_place] = mark

    for i in range(3):
        if game_table[mark_place] == game_table[mark_place[0] + str(i)]:
            counter1 += 1
            if counter1 == 3:
                win = True
        if game_table[mark_place] == game_table[str(i) + mark_place[1]]:
            counter2 += 1
            if counter2 == 3:
                win = True
        if mark_place[0] == mark_place[1]:
            if game_table[mark_place] == game_table[str(i) + str(i)]:
                counter3 += 1
                if counter3 == 3:
                    win = True
    clear_counters()

    if win:
        clear_console()
        showGame()
        game_over = choise(('0', '1'), f"\n-- Игрок {playerNum} победил!\n   1. Реванш\n   0. Выход\n\n   Ввод: ")
        if game_over == '1':
            clear_game()
        else:
            exit()
