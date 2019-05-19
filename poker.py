from random import *
from modulo import *
from konwerter import konwertuj
from translator import translate_cards


# ZMIENNE GLOBALNE

pot = 0
cards = []
used_cards = []
players = []
winner = None

seed()  # zarodek losowania


class player():
    name = 0
    hand = []
    money = 0
    pl_pot = 0
    all_in = 0
    in_game = False  # czy gracz jest w grze? czy nie zrzucil?
    balance = 0  # zysk/strata z calej gry
    checked = False
    pl_score = None
    pl_kicker = []
    random_bot = False
    qlearn_bot = False
    learn = False
    blef = False
    alfa_const = False
    win = 0
    lost = 0
    money_win = []
    money_lost = []
    win_tab = []
    lost_tab = []


    last_decision = None

    qPlayer = None

    button = False
    SB = False
    BB = False

    def __init__(self, imie, kasa):
        self.name = imie
        self.money = kasa
        self.lost_tab = []
        self.win_tab = []
        self.hand = []
        self.money_win = []
        self.money_lost = []
        self.alfa_cons = False

    def new_game_pl(self):
        self.hand = []
        self.in_game = True
        self.pl_pot = 0
        self.checked = False
        self.pl_score = 20000000
        self.pl_kicker = []

        self.last_decision = None


    def game_pass(self):
        self.in_game = False
        #print self.name, ' koncze gre'

        sum_raise(self.pl_pot)
        #self.pl_pot = 0


    def raise_pot(self, money):

        tmp_money = int(money)

        if tmp_money == self.money:
            all_in = 1
            self.money = int(self.money) - tmp_money
            self.pl_pot = int(self.pl_pot) + tmp_money
            #print 'ALL IN ', tmp_money
            sum_raise(tmp_money)

        elif tmp_money <= self.money:
            self.money = int(self.money) - tmp_money
            self.pl_pot = int(self.pl_pot) + tmp_money
            #print self.name, 'podbijam o', tmp_money
            sum_raise(tmp_money)
        else:
            print 'stowke za malo piekny kawalerze'

    def aktualizuj_staty(self, check, pot):
        if check:
            self.win += 1
            self.money_win.append(pot)
            self.money_lost.append(0)
        else:
            self.lost += 1
            self.money_lost.append(self.pl_pot)
            self.money_win.append(0)

        self.win_tab.append(self.win)
        self.lost_tab.append(self.lost)

    def export_dane(self):
        tmp = self.name + '_win.txt'
        self.zapisz(self.win_tab,tmp)

        tmp = self.name + '_lose.txt'
        self.zapisz(self.lost_tab,tmp)

        tmp = self.name + '_win_money.txt'
        self.zapisz(self.money_win,tmp)

        tmp = self.name + '_lost_money.txt'
        self.zapisz(self.money_lost,tmp)

    def zapisz(self, table, name):
        file1=open(name, "w")
        for el in table:
            element = el
            print >> file1, element
        file1.close()
## METODY GLOBALNE =====================================================


def new_game(players):
    global cards
    global used_cards
    global pot
    global winner

    cards = []
    used_cards = []
    pot = 0
    winner = None

    for pl in players:
        pl.new_game_pl()

    # jumphead() #zmiana stanu generatora

    #print ' NEW GAME!!!'


def give_button(players):
    if len(players) == 2:
        players[0].button = True
        players[0].SB = True
        players[1].BB = True
    else:
        players[0].button = True
        players[1].SB = True
        players[2].BB = True


def move_button(players):
    if len(players) == 2:

        ind = None
        tmp = None
        l = len(players)
        # znajdujemy index buttona

        for pl in players:
            if pl.button == True:
                ind = pl
            pl.button = False
            pl.SB = False
            pl.BB = False

        tmp = players.index(ind)

        players[(tmp + 1) % l].button = True
        players[(tmp + 1) % l].SB = True
        players[(tmp) % l].BB = True
    else:
        ind = None
        tmp = None
        l = len(players)
        # znajdujemy index buttona

        for pl in players:
            if pl.button == True:
                ind = pl
            pl.button = False
            pl.SB = False
            pl.BB = False

        tmp = players.index(ind)

        players[(tmp + 1) % l].button = True
        players[(tmp + 2) % l].SB = True
        players[(tmp + 3) % l].BB = True


def sum_raise(s):
    global pot
    pot += s


def give_hand(player):
    # daj reke startowa dla gracza

    global used_cards

    tmp_licznik = len(player.hand)
    tmp_hand = []

    while tmp_licznik < 2:

        card = randrange(52)  # losuje wsrod 52 kart
        tmp = used_cards.count(card)

        if tmp == 0:
            # print 'daje karte'
            tmp_hand.append(card)
            tmp_licznik += 1
            used_cards.append(card)

    player.hand = tmp_hand
    player.in_game = True


def river():
    global cards
    global used_cards

    #print '\t LECI FLOP'
    if len(cards) < 5:

        tmp_licznik = 0

        while tmp_licznik < 1:
            card = randrange(52)  # losuje wsrod 52 kart
            tmp = used_cards.count(card)

            if tmp == 0:
                # print 'daje karte'
                cards.append(card)
                tmp_licznik += 1
                used_cards.append(card)
    return cards


def turn():
    global cards
    global used_cards

    #print '\t LECI FLOP'
    if len(cards) < 4:

        tmp_licznik = 0

        while tmp_licznik < 1:
            card = randrange(52)  # losuje wsrod 52 kart
            tmp = used_cards.count(card)

            if tmp == 0:
                # print 'daje karte'
                cards.append(card)
                tmp_licznik += 1
                used_cards.append(card)
    return cards


def flop():
    global cards
    global used_cards

    #print '\t LECI FLOP'
    if len(cards) < 3:

        tmp_licznik = 0

        while tmp_licznik < 3:
            card = randrange(52)  # losuje wsrod 52 kart
            tmp = used_cards.count(card)

            if tmp == 0:
                # print 'daje karte'
                cards.append(card)
                tmp_licznik += 1
                used_cards.append(card)
    return cards


# print 'FLOP: \n\t', translate_cards(cards)
def print_pot():
    global pot
    print 'PULA:\t ', pot


def print_status(pl):
    print pl.name, '\n\tkarty:\t', translate_cards(
        pl.hand), '\n\tpula:\t', pl.pl_pot, '\n\tkasa:\t', pl.money, '\n===================\n\n'


def kicker_table(hand, cards):
    karty = []
    karty.extend(hand)
    karty.extend(cards)

    modulo(karty, 13)
    karty.sort()

    return karty


def check_hand(players):
    minimal = 13025400
    winner = None
    kickers = []
    flaga = 0
    tmp_kicker = 0

    for pl in players:
        if pl.in_game == True:
            pl.pl_score = konwertuj(pl.hand, cards)
            pl.pl_kicker = kicker_table(pl.hand, cards)

            #print 'punkty gracza', pl.name, ' =', pl.pl_score

            if pl.pl_score < minimal:
                minimal = pl.pl_score
                winner = pl

    # teraz ranking graczy zrobic :)

    for pl in players:
        if minimal == pl.pl_score:
            tmp_kicker += 1

    for pl in players:
        if pl.in_game == True:
            kickers.append([pl.pl_score, pl.pl_kicker])



    if len(kickers) > 0 and tmp_kicker > 1:
        winner = kickers.index(min(kickers))
        winner = players[winner]
    elif minimal < 13025400:
        winner = winner
    else:
        winner = None

    return winner


def show_pot():
    global pot

    return pot

### MAIN ##==============================================================
# players.append(player('maciej'))
# players.append(player('michal'))

# new_game(players)

# for pl in players:
# give_hand(pl)

# players[0].raise_pot(1100)

# flop()

# print_status(players)

# winner=check_hand(players)

# print 'the winner is ', winner.name







##print gracz2.hand
##print gracz2.in_game

##gracz.game_pass()

##print gracz.hand
##print gracz.in_game
##print gracz.money

# print 'uzyte ',used_cards
# print 'pot', pot
