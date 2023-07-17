SPADES = 0
HEARTS = 1
DIAMONDS = 2
CLUBS = 3
NOTRUMP = 4

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

VUL_NONE = 0
VUL_BOTH = 1
VUL_NS = 2
VUL_EW = 3


trump = [NOTRUMP]
first = [SOUTH]
dealer = [NORTH]
vul = [VUL_NONE]

PBN = [b"N:K742.Q7.752.QJT9 A53.A58.Q4.A8643 T8.KT9632.A93.K7 QJ96.J4.KJT86.52"]

#// Number of cards returned for solutions == 2, i.e. for
#// all cards leading to the optimal score (taking into
#// account equivalences.

cardsSoln2 = [6, 3, 4]
        
#// Number of cards returned for solutions == 3, i.e. for
#// all legally playable cards (taking into account equivalences).
cardsSoln3 = [9, 7, 8]
        

#// Useful constants

dbitMapRank = [
    0x0000, 0x0000, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020,
    0x0040, 0x0080, 0x0100, 0x0200, 0x0400, 0x0800, 0x1000, 0x2000
]

dcardRank = [
    'x', 'x', '2', '3', '4', '5', '6', '7',
    '8', '9', 'T', 'J', 'Q', 'K', 'A'
]

dcardSuit = ["S", "H", "D", "C", "N"]
dcardHand = ['N' 'E', 'S', 'W']
