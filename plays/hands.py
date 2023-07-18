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


# 3NT
# trump = [NOTRUMP]
# first = [WEST]
# dealer = [EAST]
# vul = [VUL_BOTH]
# PBN = [b"N:42.JT97.AJ952.Q5 QT973.64.T74.A72 AK.K32.Q6.KJT943 J865.AQ85.K83.86"]

# 4SE Deal 9 Team Tournament
trump = [SPADES]
first = [SOUTH]
dealer = [EAST]
vul = [VUL_EW]
PBN = [b"N:94.Q9872.T.J9543 KJ65.4.J9874.T86 QT7.A5.KQ6532.Q7 A832.KJT63.A.AK2"]

#// Number of cards returned for solutions == 2, i.e. for
#// all cards leading to the optimal score (taking into
#// account equivalences.

cardsSoln2 = [6, 3, 4]
        
#// Number of cards returned for solutions == 3, i.e. for
#// all legally playable cards (taking into account equivalences).
cardsSoln3 = [9, 7, 8]

#// Double dummy table.  The order here is:
#// Spades: North, East, South, West
#// Hearts: same
#// etc.
DDtable = [
    [
 
        5, 8, 5, 8,  6, 6, 6, 6,  5, 7, 5, 7,  7, 5, 7, 5,  6, 6, 6, 6
    ]
]

parScore = [
    [
        "", ""
    ]
]

parString = [
    [
        "" , ""
    ]
]
     

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
