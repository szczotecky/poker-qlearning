from random import *
from translator import translate_cards
import qlearnplayer
import poker

import os

x = 0
game = None
opcja = None
cards = []
max_pot = 0
game_counter = 0
players = poker.players

# =========================================================  METODY
def add_player(name, kasa):
    global players

    players.append(poker.player(name, kasa))


# =========================================================  EKRANY
def start_screen():
    global x
    os.system('cls' if os.name == 'nt' else 'clear')

    print '========== POKER =========='
    print 'MENU:'
    print '\t1. Dodaj gracza'
    print '\t2. Rozpocznij gre'
    print '\n\t9. Zakoncz'

    x = input('Wybierz opcje: ')

    if x > 2 and x != 9:
        x = 0
        print '\n!!! NIEPRAWIDLOWY WYBOR !!!'
        raw_input('Wcisnij ENTER by kontynuowac')


def add_player_scr():
    global x

    os.system('cls' if os.name == 'nt' else 'clear')

    print '======= DODAJ GRACZA ======'
    name = raw_input('Podaj imie gracza: ')
    kasa = raw_input('Podaj ile pieniedzy: ')

    if kasa.isdigit():
        add_player(name, kasa)
        print 'dodano gracza: ', name, 'money: ', kasa
        raw_input('\nWcisnij ENTER by kontynuowac')

    else:

        print '\n!!! NIEPRAWIDLOWE DANE !!!'
        raw_input('Wcisnij ENTER by kontynuowac')

    x = 0


def player_screen(player):
    os.system('cls' if os.name == 'nt' else 'clear')

    global cards
    global x
    global opcja

    opcja = 0

    print '=========== GRASZ ========='

    poker.print_pot()
    poker.print_status(player)

    print 'checked = ', player.checked

    if cards:
        print 'STOL: ', translate_cards(cards)

    print '====== Wybierz opcje ======'
    print '\t1. Podbij'
    print '\t2. Pas'
    print '\t3. Czekaj \ Sprawdz'

    opcja = input('Wybierz opcje: ')


def winner_screen(players, winner):
    global cards

    os.system('cls' if os.name == 'nt' else 'clear')

    print '=========== WYNIK ==================='
    print 'STOL: \t', translate_cards(cards), '\n'

    for pl in players:
        if pl == winner:
            print '\t', pl.name, '\t Cards: ', translate_cards(pl.hand), '\tstatus:', pl.in_game, ' <-WINNER'
        else:
            print '\t', pl.name, '\t Cards: ', translate_cards(pl.hand), '\tstatus:', pl.in_game

        if winner == None:
            print '\t BRAK ZWYCIEZCY'


def decision(player, opcja, players):
    global max_pot

    if opcja == 1:  # podbij

        print '\n\n Stawka aktualna: ', player.pl_pot,'pinionce: ', player.money
        print 'Minimalna stawka:', max_pot-player.pl_pot+1
        pot = raw_input('\nPodaj stawke: ')

        if player.money > 100 and pot+player.pl_pot >= max_pot+1:
            player.raise_pot(pot)

            for pl in players:
                pl.checked = False

        else:
            decision(player,1,players)


    elif opcja == 2:  # pass
        player.game_pass()

    elif opcja == 3:  # sprawdz/czekaj
        player.checked = True

        if max_pot > 0 and max_pot > player.pl_pot:
            player.raise_pot(max_pot - player.pl_pot)

    elif opcja == 8:  # mala_slepa
        player.raise_pot(5)
        max_pot = 5
    elif opcja == 9:  # duza_slepa
        player.raise_pot(10)
        max_pot = 10


def pc_decision(player, opcja, players, pot):
    global max_pot

    if opcja == 1:  # podbij
        player.raise_pot(pot)

        for pl in players:
            pl.checked = False

    elif opcja == 2:  # pasuj
        player.game_pass()


    elif opcja == 3:  # czekaj/sprawdz
        player.checked = True
        #print player.name, '\t sprawdzam/czekam'

        if max_pot > 0 and max_pot > player.pl_pot:
            player.raise_pot(max_pot - player.pl_pot)


# =========================================================  METODY POM

def check_game(players):
    result = 0
    for pl in players:
        if pl.in_game == True:
            result += 1
    return result


def check_money(players, winner):
    for pl in players:
        poker.player.money -= poker.player.pl_pot

    winner.money += poker.show_pot()


def check_game_winner(players):
    result = 0
    result_2 = 1
    ran = len(players)
    winner = None

    for pl in players:
        if pl.in_game == True:
            result += 1

    for x in range(ran - 1):
        if players[x].pl_pot == players[x + 1].pl_pot:
            result_2 += 1

    if result_2 == ran or result < 2:

        winner = poker.check_hand(players)

        if winner != None:
            check_money(players, winner)

            #print 'The winner is ', winner.name
        #else:
            #print 'Brak winera'

        game = False

    return winner


def check_game_checked(players):
    result = 0
    for pl in players:
        if pl.checked == True:
            result += 1
    return result


def check_bets(players):
    tmp = len(players) - 1

    for p in players:
        if p.in_game == False:
            tmp -= 1

    for p in range(len(players) - 1):
        if players[p].pl_pot == players[p + 1].pl_pot:
            tmp -= 1

    return tmp


def check_flop(players):
    global cards

    if check_bets(players) < 1 and check_game(players) > 1:

        if len(cards) < 3:
            cards = poker.flop()
        elif len(cards) < 4:
            cards = poker.turn()
        elif len(cards) < 5:
            cards = poker.river()

        for pl in players:
            pl.checked = False


def wplac_slepe(players):
    global opcja
    global max_pot

    max_pot = 0

    for pl in players:
        # znajdz slepa
        if max_pot == 0 and pl.button == True:
            decision(pl, 3, players)

        elif max_pot == 0 and pl.SB == True:
            decision(pl, 8, players)
            max_pot = 5

        elif max_pot == 5 and pl.BB == True:
            decision(pl, 9, players)
            max_pot = 10

    for pl in players:
        pl.checked = False


def licytacja(players,i):
    global opcja
    global max_pot

    licitation = True

    counter = 1

    while licitation == True and check_game(players) > 1:

        for pl in players:

            # jezeli juz wplacone slepe
            if pl.in_game == True and check_game(players) > 1:

                # jezeli graczy w grze jest wiecej niz 1

                if pl.random_bot == True:
                    option = randrange(3) + 1

                    if pl.money > 100 and option==1:
                        pot_tmp = randrange(100) + (max_pot - pl.pl_pot)
                        pc_decision(pl, option, players, pot_tmp)
                    else:
                        option = randrange(2)+2

                        pc_decision(pl, option, players, 0)

                #============================================================QLEARN BOT =====   V V V

                elif pl.qlearn_bot == True:
                    if pl.blef == False:
                        option = pl.qPlayer.select_action(pl)      #bez blefowania
                    elif pl.blef == True:
                        option = pl.qPlayer.select_action_blef(pl)  #z blefem


                    if pl.money > 100 and option==1:
                        pot_tmp = randrange(100)+1
                        pl.last_decision = option
                        pc_decision(pl, option, players, pot_tmp)
                    elif option == 2 or option == 3:
                        pc_decision(pl, option, players, 0)
                    else:
                        option = randrange(2)+2

                        pc_decision(pl, option, players, 0)

                    if pl.learn == True:
                        pl.qPlayer.aktualizuj(0,0,pl,i,pl.alfa_const)

                else:
                    player_screen(pl)
                    decision(pl, opcja, players)

            if pl.pl_pot > max_pot:
                max_pot = pl.pl_pot
                counter = 1
                for pla in players:
                    pla.checked = False
                    licitation = True

            elif pl.checked == True:
                counter += 1
            elif pl.pl_pot == max_pot:
                counter += 1

            if counter == len(players):
                licitation = False



# ========================================================== MAIN
def main():
    global game
    global x
    global cards
    global game_counter
    global players

    range_n=5000000 #============================================================= ILE PRZEBIEGOW

    add_player('alfa_zmienna', 99999999999)
    add_player('alfa_stala', 99999999999)
    add_player('alfa_zmienna_blef', 99999999999)
    add_player('alfa_stala_blef', 99999999999)

    players[0].qlearn_bot = True #ten douczany ciagle
    players[1].qlearn_bot = True #ten jako poprzednie doswiadczneia, nie uczy sie
    players[2].qlearn_bot = True
    players[3].qlearn_bot = True

    players[0].blef = False
    players[1].blef = False
    players[2].blef = True
    players[3].blef = True

    #players[1].random_bot = True

    players[0].learn = True
    players[1].learn = True
    players[2].learn = True
    players[3].learn = True

    players[0].alfa_const = False
    players[1].alfa_const = True
    players[2].alfa_const = False
    players[3].alfa_const = True



    QL_bot = players[0]
    players[0].qPlayer = qlearnplayer.Q_Player()

    QL_bot2 = players[1]
    players[1].qPlayer = qlearnplayer.Q_Player()

    players[2].qPlayer = qlearnplayer.Q_Player()
    players[3].qPlayer = qlearnplayer.Q_Player()

    players[0].qPlayer.import_qtable("dane_zmienna.p")
    players[1].qPlayer.import_qtable("dane_stala.p")
    players[2].qPlayer.import_qtable("dane_zmienna_blef.p")
    players[3].qPlayer.import_qtable("dane_stala_blef.p")


    while x < 9:

        if x == 0:
            start_screen()

        elif x == 1:
            add_player_scr()

        elif x == 2:
            if len(players) > 1:
                for i in range (range_n):

                    if i%10000 == 0:
                        print i

                    for pl in players:
                        if pl.qlearn_bot == True and pl.learn == True:
                            pl.qPlayer.clean_states(pl)

                    #print '=========================================================================================='

                    poker.new_game(players)
                    if game_counter == 0:
                        poker.give_button(players)
                        game_counter += 1
                    else:
                        poker.move_button(players)
                        game_counter += 1

                    cards = []
                    game = True

                    for pl in players:
                        poker.give_hand(pl)

                    wplac_slepe(players)
                    licytacja(players,i+1)

                    check_flop(players)
                    licytacja(players,i+1)
                    check_flop(players)
                    licytacja(players,i+1)
                    check_flop(players)
                    licytacja(players,i+1)

                    #for pl in players:
                        #print pl.hand
                    #print cards

                    winner = check_game_winner(players)
                    #winner_screen(players, winner)

                    for pl in players:
                        if winner == pl and pl.qlearn_bot == True and pl.learn == True:
                            pl.qPlayer.aktualizuj(1,poker.pot,pl,i+1,pl.alfa_const)

                        elif pl.qlearn_bot == True and pl.learn == True:
                            pl.qPlayer.aktualizuj(-1,poker.pot,pl,i+1,pl.alfa_const)

                        if winner == pl:
                            pl.aktualizuj_staty(True, poker.pot)

                        elif winner != pl:
                            pl.aktualizuj_staty(False, poker.pot)

                    #if winner != None:
                    #    print 'game winner ', winner.name
                    #    print 'winner cards ', translate_cards(winner.hand)
                    #else:
                    #    print 'Nikt nie wygral'

                    #raw_input('Wcisnij ENTER by kontynuowac')
                    x = 0
                players[0].qPlayer.export_qtable("dane.p")
                #players[1].qPlayer.export_qtable("dane_learn.p")

                for pl in players:
                    #print pl.name, '\tZWYCIESTW: ', pl.win, '\tPORAZEK: ',pl.lost#, 'dlugosc win:', len(pl.win)
                    print pl.name, '\tZWYCIESTW: ', pl.win_tab[len(pl.win_tab)-1], '\tPORAZEK: ',pl.lost_tab[len(pl.lost_tab)-1], 'dlugosc win:', len(pl.win_tab)

                    print pl.name, '\tKASA WYGRANA: ', sum(pl.money_win), '\tPORAZEK: ', sum(pl.money_lost)

                    pl.export_dane()


            else:
                print 'Brak graczy'
                raw_input('Wcisnij ENTER by kontynuowac')
                x = 0


if __name__ == '__main__':
    main()
