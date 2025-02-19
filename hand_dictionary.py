
hand_dict = {\
'ROYAL_FLUSH'           :1,\
'STRAIGHT_FLUSH_ACE'    :2,\
'STRAIGHT_FLUSH_TWO'    :3,\
'STRAIGHT_FLUSH_THREE'  :4,\
'STRAIGHT_FLUSH_FOUR'   :5,\
'STRAIGHT_FLUSH_FIVE'   :6,\
'STRAIGHT_FLUSH_SIX'    :7,\
'STRAIGHT_FLUSH_SEVEN'  :8,\
'STRAIGHT_FLUSH_EIGHT'  :9,\
'STRAIGHT_FLUSH_NINE'   :10,\
'FOUR_OF_A_KIND_ACE'    :11,\
'FOUR_OF_A_KIND_TWO'    :12,\
'FOUR_OF_A_KIND_THREE'  :13,\
'FOUR_OF_A_KIND_FOUR'   :14,\
'FOUR_OF_A_KIND_FIVE'   :15,\
'FOUR_OF_A_KIND_SIX'    :16,\
'FOUR_OF_A_KIND_SEVEN'  :17,\
'FOUR_OF_A_KIND_EIGHT'  :18,\
'FOUR_OF_A_KIND_NINE'   :19,\
'FOUR_OF_A_KIND_TEN'    :20,\
'FOUR_OF_A_KIND_JACK'   :21,\
'FOUR_OF_A_KIND_QUEEN'  :22,\
'FOUR_OF_A_KIND_KING'   :23,\
'FULL_HOUSE_ACE_TWO'    :24,\
'FULL_HOUSE_ACE_THREE'  :25,\
'FULL_HOUSE_ACE_FOUR'   :26,\
'FULL_HOUSE_ACE_FIVE'   :27,\
'FULL_HOUSE_ACE_SIX'    :28,\
'FULL_HOUSE_ACE_SEVEN'  :29,\
'FULL_HOUSE_ACE_EIGHT'  :30,\
'FULL_HOUSE_ACE_NINE'   :31,\
'FULL_HOUSE_ACE_TEN'    :32,\
'FULL_HOUSE_ACE_JACK'   :33,\
'FULL_HOUSE_ACE_QUEEN'  :34,\
'FULL_HOUSE_ACE_KING'   :35,\
'FULL_HOUSE_TWO_ACE'    :36,\
'FULL_HOUSE_TWO_THREE'  :37,\
'FULL_HOUSE_TWO_FOUR'   :38,\
'FULL_HOUSE_TWO_FIVE'   :39,\
'FULL_HOUSE_TWO_SIX'    :40,\
'FULL_HOUSE_TWO_SEVEN'  :41,\
'FULL_HOUSE_TWO_EIGHT'  :42,\
'FULL_HOUSE_TWO_NINE'   :43,\
'FULL_HOUSE_TWO_TEN'    :44,\
'FULL_HOUSE_TWO_JACK'   :45,\
'FULL_HOUSE_TWO_QUEEN'  :46,\
'FULL_HOUSE_TWO_KING'   :47,\
'FULL_HOUSE_THREE_ACE'  :48,\
'FULL_HOUSE_THREE_TWO'  :49,\
'FULL_HOUSE_THREE_FOUR' :50,\
'FULL_HOUSE_THREE_FIVE' :51,\
'FULL_HOUSE_THREE_SIX'  :52,\
'FULL_HOUSE_THREE_SEVEN':53,\
'FULL_HOUSE_THREE_EIGHT':54,\
'FULL_HOUSE_THREE_NINE' :55,\
'FULL_HOUSE_THREE_TEN'  :56,\
'FULL_HOUSE_THREE_JACK' :57,\
'FULL_HOUSE_THREE_QUEEN':58,\
'FULL_HOUSE_THREE_KING' :59,\
'FULL_HOUSE_FOUR_ACE'   :60,\
'FULL_HOUSE_FOUR_TWO'   :61,\
'FULL_HOUSE_FOUR_THREE' :62,\
'FULL_HOUSE_FOUR_FIVE'  :63,\
'FULL_HOUSE_FOUR_SIX'   :64,\
'FULL_HOUSE_FOUR_SEVEN' :65,\
'FULL_HOUSE_FOUR_EIGHT' :66,\
'FULL_HOUSE_FOUR_NINE'  :67,\
'FULL_HOUSE_FOUR_TEN'   :68,\
'FULL_HOUSE_FOUR_JACK'  :69,\
'FULL_HOUSE_FOUR_QUEEN' :70,\
'FULL_HOUSE_FOUR_KING'  :71,\
'FULL_HOUSE_FIVE_ACE'   :72,\
'FULL_HOUSE_FIVE_TWO'   :73,\
'FULL_HOUSE_FIVE_THREE' :74,\
'FULL_HOUSE_FIVE_FOUR'  :75,\
'FULL_HOUSE_FIVE_SIX'   :76,\
'FULL_HOUSE_FIVE_SEVEN' :77,\
'FULL_HOUSE_FIVE_EIGHT' :78,\
'FULL_HOUSE_FIVE_NINE'  :79,\
'FULL_HOUSE_FIVE_TEN'   :80,\
'FULL_HOUSE_FIVE_JACK'  :81,\
'FULL_HOUSE_FIVE_QUEEN' :82,\
'FULL_HOUSE_FIVE_KING'  :83,\
'FULL_HOUSE_SIX_ACE'    :84,\
'FULL_HOUSE_SIX_TWO'    :85,\
'FULL_HOUSE_SIX_THREE'  :86,\
'FULL_HOUSE_SIX_FOUR'   :87,\
'FULL_HOUSE_SIX_FIVE'   :88,\
'FULL_HOUSE_SIX_SEVEN'  :89,\
'FULL_HOUSE_SIX_EIGHT'  :90,\
'FULL_HOUSE_SIX_NINE'   :91,\
'FULL_HOUSE_SIX_TEN'    :92,\
'FULL_HOUSE_SIX_JACK'   :93,\
'FULL_HOUSE_SIX_QUEEN'  :94,\
'FULL_HOUSE_SIX_KING'   :95,\
'FULL_HOUSE_SEVEN_ACE'  :96,\
'FULL_HOUSE_SEVEN_TWO'  :97,\
'FULL_HOUSE_SEVEN_THREE':98,\
'FULL_HOUSE_SEVEN_FOUR' :99,\
'FULL_HOUSE_SEVEN_FIVE' :100,\
'FULL_HOUSE_SEVEN_SIX'  :101,\
'FULL_HOUSE_SEVEN_EIGHT':102,\
'FULL_HOUSE_SEVEN_NINE' :103,\
'FULL_HOUSE_SEVEN_TEN'  :104,\
'FULL_HOUSE_SEVEN_JACK' :105,\
'FULL_HOUSE_SEVEN_QUEEN':106,\
'FULL_HOUSE_SEVEN_KING' :107,\
'FULL_HOUSE_EIGHT_ACE'  :108,\
'FULL_HOUSE_EIGHT_TWO'  :109,\
'FULL_HOUSE_EIGHT_THREE':110,\
'FULL_HOUSE_EIGHT_FOUR' :111,\
'FULL_HOUSE_EIGHT_FIVE' :112,\
'FULL_HOUSE_EIGHT_SIX'  :113,\
'FULL_HOUSE_EIGHT_SEVEN':114,\
'FULL_HOUSE_EIGHT_NINE' :115,\
'FULL_HOUSE_EIGHT_TEN'  :116,\
'FULL_HOUSE_EIGHT_JACK' :117,\
'FULL_HOUSE_EIGHT_QUEEN':118,\
'FULL_HOUSE_EIGHT_KING' :119,\
'FULL_HOUSE_NINE_ACE'   :120,\
'FULL_HOUSE_NINE_TWO'   :121,\
'FULL_HOUSE_NINE_THREE' :122,\
'FULL_HOUSE_NINE_FOUR'  :123,\
'FULL_HOUSE_NINE_FIVE'  :124,\
'FULL_HOUSE_NINE_SIX'   :125,\
'FULL_HOUSE_NINE_SEVEN' :126,\
'FULL_HOUSE_NINE_EIGHT' :127,\
'FULL_HOUSE_NINE_TEN'   :128,\
'FULL_HOUSE_NINE_JACK'  :129,\
'FULL_HOUSE_NINE_QUEEN' :130,\
'FULL_HOUSE_NINE_KING'  :131,\
'FULL_HOUSE_TEN_ACE'    :132,\
'FULL_HOUSE_TEN_TWO'    :133,\
'FULL_HOUSE_TEN_THREE'  :134,\
'FULL_HOUSE_TEN_FOUR'   :135,\
'FULL_HOUSE_TEN_FIVE'   :136,\
'FULL_HOUSE_TEN_SIX'    :137,\
'FULL_HOUSE_TEN_SEVEN'  :138,\
'FULL_HOUSE_TEN_EIGHT'  :139,\
'FULL_HOUSE_TEN_NINE'   :140,\
'FULL_HOUSE_TEN_JACK'   :141,\
'FULL_HOUSE_TEN_QUEEN'  :142,\
'FULL_HOUSE_TEN_KING'   :143,\
'FULL_HOUSE_JACK_ACE'   :144,\
'FULL_HOUSE_JACK_TWO'   :145,\
'FULL_HOUSE_JACK_THREE' :146,\
'FULL_HOUSE_JACK_FOUR'  :147,\
'FULL_HOUSE_JACK_FIVE'  :148,\
'FULL_HOUSE_JACK_SIX'   :149,\
'FULL_HOUSE_JACK_SEVEN' :150,\
'FULL_HOUSE_JACK_EIGHT' :151,\
'FULL_HOUSE_JACK_NINE'  :152,\
'FULL_HOUSE_JACK_TEN'   :153,\
'FULL_HOUSE_JACK_QUEEN' :154,\
'FULL_HOUSE_JACK_KING'  :155,\
'FULL_HOUSE_QUEEN_ACE'  :156,\
'FULL_HOUSE_QUEEN_TWO'  :157,\
'FULL_HOUSE_QUEEN_THREE':158,\
'FULL_HOUSE_QUEEN_FOUR' :159,\
'FULL_HOUSE_QUEEN_FIVE' :160,\
'FULL_HOUSE_QUEEN_SIX'  :161,\
'FULL_HOUSE_QUEEN_SEVEN':162,\
'FULL_HOUSE_QUEEN_EIGHT':163,\
'FULL_HOUSE_QUEEN_NINE' :164,\
'FULL_HOUSE_QUEEN_TEN'  :165,\
'FULL_HOUSE_QUEEN_JACK' :166,\
'FULL_HOUSE_QUEEN_KING' :167,\
'FULL_HOUSE_KING_ACE'   :168,\
'FULL_HOUSE_KING_TWO'   :169,\
'FULL_HOUSE_KING_THREE' :170,\
'FULL_HOUSE_KING_FOUR'  :171,\
'FULL_HOUSE_KING_FIVE'  :172,\
'FULL_HOUSE_KING_SIX'   :173,\
'FULL_HOUSE_KING_SEVEN' :174,\
'FULL_HOUSE_KING_EIGHT' :175,\
'FULL_HOUSE_KING_NINE'  :176,\
'FULL_HOUSE_KING_TEN'   :177,\
'FULL_HOUSE_KING_JACK'  :178,\
'FULL_HOUSE_KING_QUEEN' :179,\
'FLUSH'                 :180,\
'STRAIGHT_ACE'          :181,\
'STRAIGHT_TWO'          :182,\
'STRAIGHT_THREE'        :183,\
'STRAIGHT_FOUR'         :184,\
'STRAIGHT_FIVE'         :185,\
'STRAIGHT_SIX'          :186,\
'STRAIGHT_SEVEN'        :187,\
'STRAIGHT_EIGHT'        :188,\
'STRAIGHT_NINE'         :189,\
'STRAIGHT_TEN'          :190,\
'THREE_OF_A_KIND_ACE'   :191,\
'THREE_OF_A_KIND_TWO'   :192,\
'THREE_OF_A_KIND_THREE' :193,\
'THREE_OF_A_KIND_FOUR'  :194,\
'THREE_OF_A_KIND_FIVE'  :195,\
'THREE_OF_A_KIND_SIX'   :196,\
'THREE_OF_A_KIND_SEVEN' :197,\
'THREE_OF_A_KIND_EIGHT' :198,\
'THREE_OF_A_KIND_NINE'  :199,\
'THREE_OF_A_KIND_TEN'   :200,\
'THREE_OF_A_KIND_JACK'  :201,\
'THREE_OF_A_KIND_QUEEN' :202,\
'THREE_OF_A_KIND_KING'  :203,\
'TWO_PAIRS_TWO_ACE'     :204,\
'TWO_PAIRS_TWO_THREE'   :205,\
'TWO_PAIRS_TWO_FOUR'    :206,\
'TWO_PAIRS_TWO_FIVE'    :207,\
'TWO_PAIRS_TWO_SIX'     :208,\
'TWO_PAIRS_TWO_SEVEN'   :209,\
'TWO_PAIRS_TWO_EIGHT'   :210,\
'TWO_PAIRS_TWO_NINE'    :211,\
'TWO_PAIRS_TWO_TEN'     :212,\
'TWO_PAIRS_TWO_JACK'    :213,\
'TWO_PAIRS_TWO_QUEEN'   :214,\
'TWO_PAIRS_TWO_KING'    :215,\
'TWO_PAIRS_THREE_ACE'   :216,\
'TWO_PAIRS_THREE_FOUR'  :217,\
'TWO_PAIRS_THREE_FIVE'  :218,\
'TWO_PAIRS_THREE_SIX'   :219,\
'TWO_PAIRS_THREE_SEVEN' :220,\
'TWO_PAIRS_THREE_EIGHT' :221,\
'TWO_PAIRS_THREE_NINE'  :222,\
'TWO_PAIRS_THREE_TEN'   :223,\
'TWO_PAIRS_THREE_JACK'  :224,\
'TWO_PAIRS_THREE_QUEEN' :225,\
'TWO_PAIRS_THREE_KING'  :226,\
'TWO_PAIRS_FOUR_ACE'    :227,\
'TWO_PAIRS_FOUR_FIVE'   :228,\
'TWO_PAIRS_FOUR_SIX'    :229,\
'TWO_PAIRS_FOUR_SEVEN'  :230,\
'TWO_PAIRS_FOUR_EIGHT'  :231,\
'TWO_PAIRS_FOUR_NINE'   :232,\
'TWO_PAIRS_FOUR_TEN'    :233,\
'TWO_PAIRS_FOUR_JACK'   :234,\
'TWO_PAIRS_FOUR_QUEEN'  :235,\
'TWO_PAIRS_FOUR_KING'   :236,\
'TWO_PAIRS_FIVE_ACE'    :237,\
'TWO_PAIRS_FIVE_SIX'    :238,\
'TWO_PAIRS_FIVE_SEVEN'  :239,\
'TWO_PAIRS_FIVE_EIGHT'  :240,\
'TWO_PAIRS_FIVE_NINE'   :241,\
'TWO_PAIRS_FIVE_TEN'    :242,\
'TWO_PAIRS_FIVE_JACK'   :243,\
'TWO_PAIRS_FIVE_QUEEN'  :244,\
'TWO_PAIRS_FIVE_KING'   :245,\
'TWO_PAIRS_SIX_ACE'     :246,\
'TWO_PAIRS_SIX_SEVEN'   :247,\
'TWO_PAIRS_SIX_EIGHT'   :248,\
'TWO_PAIRS_SIX_NINE'    :249,\
'TWO_PAIRS_SIX_TEN'     :250,\
'TWO_PAIRS_SIX_JACK'    :251,\
'TWO_PAIRS_SIX_QUEEN'   :252,\
'TWO_PAIRS_SIX_KING'    :253,\
'TWO_PAIRS_SEVEN_ACE'   :254,\
'TWO_PAIRS_SEVEN_EIGHT' :255,\
'TWO_PAIRS_SEVEN_NINE'  :256,\
'TWO_PAIRS_SEVEN_TEN'   :257,\
'TWO_PAIRS_SEVEN_JACK'  :258,\
'TWO_PAIRS_SEVEN_QUEEN' :259,\
'TWO_PAIRS_SEVEN_KING'  :260,\
'TWO_PAIRS_EIGHT_ACE'   :261,\
'TWO_PAIRS_EIGHT_NINE'  :262,\
'TWO_PAIRS_EIGHT_TEN'   :263,\
'TWO_PAIRS_EIGHT_JACK'  :264,\
'TWO_PAIRS_EIGHT_QUEEN' :265,\
'TWO_PAIRS_EIGHT_KING'  :266,\
'TWO_PAIRS_NINE_ACE'    :267,\
'TWO_PAIRS_NINE_TEN'    :268,\
'TWO_PAIRS_NINE_JACK'   :269,\
'TWO_PAIRS_NINE_QUEEN'  :270,\
'TWO_PAIRS_NINE_KING'   :271,\
'TWO_PAIRS_TEN_ACE'     :272,\
'TWO_PAIRS_TEN_JACK'    :273,\
'TWO_PAIRS_TEN_QUEEN'   :274,\
'TWO_PAIRS_TEN_KING'    :275,\
'TWO_PAIRS_JACK_ACE'    :276,\
'TWO_PAIRS_JACK_QUEEN'  :277,\
'TWO_PAIRS_JACK_KING'   :278,\
'TWO_PAIRS_QUEEN_ACE'   :279,\
'TWO_PAIRS_QUEEN_KING'  :280,\
'TWO_PAIRS_KING_ACE'    :281,\
'PAIR_ACE'              :282,\
'PAIR_TWO'              :283,\
'PAIR_THREE'            :284,\
'PAIR_FOUR'             :285,\
'PAIR_FIVE'             :286,\
'PAIR_SIX'              :287,\
'PAIR_SEVEN'            :288,\
'PAIR_EIGHT'            :289,\
'PAIR_NINE'             :290,\
'PAIR_TEN'              :291,\
'PAIR_JACK'             :292,\
'PAIR_QUEEN'            :293,\
'PAIR_KING'             :294,\
'HIGH_CARD_ACE'         :295,\
'HIGH_CARD_TWO'         :296,\
'HIGH_CARD_THREE'       :297,\
'HIGH_CARD_FOUR'        :298,\
'HIGH_CARD_FIVE'        :299,\
'HIGH_CARD_SIX'         :300,\
'HIGH_CARD_SEVEN'       :301,\
'HIGH_CARD_EIGHT'       :302,\
'HIGH_CARD_NINE'        :303,\
'HIGH_CARD_TEN'         :304,\
'HIGH_CARD_JACK'        :305,\
'HIGH_CARD_QUEEN'       :306,\
'HIGH_CARD_KING'        :307,\
}
