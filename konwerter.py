import modulo


def konwertuj(karty_hand, karty_table):
    karty = []
    karty.extend(karty_hand)
    karty.extend(karty_table)

    karty.sort()

    uklad1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    kolor = [0, 0, 0, 0]
    check_f = 1
    kolor_tmp = 0

    r_value = 0  # zwracana wartosc - im mniej tym, lepiej

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
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight flush 1'
                r_value = 36 - karty[4]
            else:
                #print 'KOLOR 1'
                r_value = 5108

            if kolor_tmp == 1:

                kolor_tmp = karty.index(8)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                        #print 'ROYAL POKER 1'
                        r_value = 4


        elif poker_tmp == 1:
            kolor_tmp = karty.count(21)

            # zwykly poker
            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1]and karty[x+1]<26 and karty[x]>12:
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight flush 2'
                r_value = 36 - karty[4]
            else:
                #print 'KOLOR 2'
                r_value = 5108

            if kolor_tmp == 1:
                kolor_tmp = karty.index(21)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                        #print 'ROYAL POKER 2'
                        r_value = 4

        elif poker_tmp == 2:
            kolor_tmp = karty.count(34)

            # zwykly poker
            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1]and karty[x+1]<39 and karty[x]>25:
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight flush 3'
                r_value = 36 - karty[4]
            else:
                #print 'KOLOR 3'
                r_value = 5108

            if kolor_tmp == 1:
                kolor_tmp = karty.index(34)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                        #print 'ROYAL POKER 3'
                        r_value = 4

        elif poker_tmp == 3:
            kolor_tmp = karty.count(47)

            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1] and karty[x]>38:
                    check_f += 1
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight flush 4'
                r_value = 36 - karty[4]
            else:
                #print 'KOLOR 4'
                r_value = 5108

            if kolor_tmp == 1:
                kolor_tmp = karty.index(47)
                if kolor_tmp + 4 < len(karty):
                    if karty[kolor_tmp] + 4 == karty[kolor_tmp + 4]:
                        #print 'ROYAL POKER 4'
                        r_value = 4

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

        if len(karty) > 4:
            check_f = 1

            dupa = len(karty)

            for x in range(len(karty) - 1):

                if karty[x] + 1 == karty[x + 1]:
                    check_f += 1
                elif karty[x] == karty[x + 1]:
                    check_f = check_f
                elif check_f < 5:
                    check_f = 1
            if check_f > 4:
                #print 'Straight'
                r_value = 10200

            elif para == 1 and trojka == 1:
                #print 'FULL'
                r_value = 3744 - uklad1.index(2) - uklad1.index(3)

            elif kareta == 1:
                #print 'KARETA'
                r_value = 624 - uklad1.index(4)

            elif trojka == 1:
                #print 'TROJKA'
                r_value = 54912 - uklad1.index(3)

            elif para == 3 or para == 2:
                #print 'DWIE PARY'

                r_value = 123552
                tmp_list = []

                for i in range(len(uklad1)):
                    if uklad1[i] == 2:
                        tmp_list.append(i)

                tmp_list.reverse()

                # print tmp_list

                for i in range(2):
                    r_value -= tmp_list[i]

            elif para == 1:
                #print 'PARA'
                r_value = 1098240 - uklad1.index(2)

            else:
                #print 'HIGH CARD'
                karty.reverse()
                r_value = 1302540 - karty[0]

    return r_value

# konwertuj([40,2,41,5,42,43,44])
# konwertuj([40,2,51,50,47,48,49])
# konwertuj ([1,8,9,10,11,12,13])
# konwertuj([13,15,17,18,21,20,23])
# konwertuj([11,25,23,35,40,20,6])
konwertuj([27, 15, 39, 30, 29],[25, 40])
