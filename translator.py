

COLORS = [ "SPADE", "CLUB", "HEART", "DIAMOND" ]
FIGURES = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]
FIGURES2 = [ 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING', 'ACE' ]

def translate_cards(cards):

	cards_names = []

	for c in cards:

		if c < 13:
			t=[COLORS[0]]

		elif c>12 and c<26:
			t=[COLORS[1]]

		elif c>25 and c<39:
			t=[COLORS[2]]

		elif c>38 and c<52:
			t=[COLORS[3]]

		t+= [FIGURES[c%13]]

		cards_names.append(' '.join(t))

	return cards_names

def translate_figure(card):

	t= FIGURES2[card%13]

	return t


#translate_cards([12, 13, 14])
#print translate_figure(23)
#print translate_cards([23])