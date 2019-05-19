import modulo
from translator import translate_figure

HAND = ['ROYAL_FLUSH', 'STRAIGHT_FLUSH', 'FOUR_OF_A_KIND', 'FULL_HOUSE', 'FLUSH', 'STRAIGHT', 'THREE_OF_A_KIND',\
        'TWO_PAIRS', 'PAIR', 'HIGH_CARD']

def konwertuj_q(karty_hand, karty_table):

    karty = []
    karty.extend(karty_hand)
    karty.extend(karty_table)


    karty.sort()

    uklad1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    kolor = [0, 0, 0, 0]
    check_f = 1
    kolor_tmp = 0
    card_tmp = None
    card_tmp2= None

    tmp = []

    r_value = None  # zwracana wartosc - index w tablicy

    hand_name = []


    dl = len(karty)

    if len(karty) > 4:

        # sprawdzenie kolor, poker,royal poker
        for x in range(dl):
            if karty[x] >= 0 and karty[x] < 13:
                kolor[0] += 1
            elif karty[x] >= 13 and karty[x] < 26:
                kolor[1] += 1
            elif karty[x] >= 26 and karty[x] < 39:
                kolor[2] += 1
            elif karty[x] >= 39:
                kolor[3] += 1

        # czy jest 5 kart w kolorze?

        for x in range(len(kolor)):

            if kolor[x] > 4:
                kolor_tmp = 1  # flaga znalezienia 5 kart
                poker_tmp = x  # index

    if kolor_tmp > 0:

        # sprawdzamy poker krolewski

        if poker_tmp == 0:
            kolor_tmp = karty.count(8)

            # zwykly poker
            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1] and karty[x+1]<13:
                    if check_f == 1:
                        card_tmp = karty[x]
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight flush 1'
                r_value = 1
            else:
                #print 'KOLOR 1'
                r_value = 4

            if kolor_tmp == 1:

                kolor_tmp = karty.index(8)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                       # print 'ROYAL POKER 1'
                        r_value = 0


        elif poker_tmp == 1:
            kolor_tmp = karty.count(21)

            # zwykly poker
            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1] and karty[x+1]<26 and karty[x]>12:
                    if check_f == 1:
                        card_tmp = karty[x]
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
               # print 'Straight flush 2'
                r_value = 1
            else:
               # print 'KOLOR 2'
                r_value = 4

            if kolor_tmp == 1:
                kolor_tmp = karty.index(21)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                        #print 'ROYAL POKER 2'
                        r_value = 0

        elif poker_tmp == 2:
            kolor_tmp = karty.count(34)

            # zwykly poker
            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1]and karty[x+1]<39 and karty[x]>25:
                    if check_f == 1:
                        card_tmp = karty[x]
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight flush 3'
                r_value = 1
            else:
               #print 'KOLOR 3'
                r_value = 4

            if kolor_tmp == 1:
                kolor_tmp = karty.index(34)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                        #print 'ROYAL POKER 3'
                        r_value = 0

        elif poker_tmp == 3:
            kolor_tmp = karty.count(47)

            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1] and karty[x]>38:
                    if check_f == 1:
                        card_tmp = karty[x]
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight flush 4'
                r_value = 1
            else:
                #print 'KOLOR 4'
                r_value = 4

            if kolor_tmp == 1:
                kolor_tmp = karty.index(47)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                        #print 'ROYAL POKER 4'
                        r_value = 0

                    # zwykly poker

    else:

        # sprawdzenie pary,2par,3ki,4ki,full,straight
        modulo.modulo(karty, 13)
        karty.sort()

        # flush

        for x in range(dl):
            uklad1[karty[x]] += 1

        para = uklad1.count(2)
        trojka = uklad1.count(3)
        kareta = uklad1.count(4)

        # print 'para:' , para, 'trojka:', trojka, 'kareta:', kareta

        if len(karty) > 1:
            check_f = 0

            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1]:
                    if check_f == 1:
                        card_tmp = karty[x]%13
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight'
                r_value = 5

            elif para == 1 and trojka == 1:
                #print 'FULL'
                r_value = 3
                card_tmp = uklad1.index(2)
                card_tmp2 = uklad1.index(3)

            elif kareta == 1:
                #print 'KARETA'
                r_value = 2
                card_tmp = uklad1.index(4)

            elif trojka == 1:
                #print 'TROJKA'
                r_value = 6
                card_tmp = uklad1.index(3)

            elif para == 3 or para == 2:
                #print 'DWIE PARY'

                r_value = 7
                tmp_list = []

                for i in range(len(uklad1)):
                    if uklad1[i] == 2:
                        tmp_list.append(i)

                tmp_list.reverse()

                card_tmp = tmp_list[0]
                card_tmp2 = tmp_list[1]

            elif para == 1:
                #print 'PARA'
                r_value = 8
                card_tmp = uklad1.index(2)

            else:
                #print 'HIGH CARD'
                karty.reverse()
                r_value = 9
                card_tmp = karty[0]


    tmp = [HAND[r_value]]

    if (r_value != 0) and (r_value != 4):
        if card_tmp2 != None :
            if card_tmp2 < card_tmp:
                tmpp = card_tmp2
                card_tmp2 = card_tmp
                card_tmp = tmpp

        if card_tmp != None :
            tmp += [translate_figure(card_tmp)]
        if card_tmp2 != None:
            tmp += [translate_figure(card_tmp2)]

    hand_name.append('_'.join(tmp))

    return hand_name


#print konwertuj_q([40,2,41,5,42,43,44],[])
#print konwertuj_q([40,2,51,50,47,48,49],[])
#print konwertuj_q([1,8,9,10,11,12,13],[])
#print konwertuj_q([13,15,17,18,21,20,23],[])
#print konwertuj_q([11,25,23,35,40,20,6],[])
#print konwertuj_q([28,32,25,26,24],[27,30])
