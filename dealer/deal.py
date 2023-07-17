#! /usr/bin/env python3

# brute-force generate random deals that fit criteria

import argparse
from functools import reduce
from pprint import pprint
import random
import re
import sys
import time

from constants import NORTH, EAST, SOUTH, WEST

from constraints import deal_3NTE, deal_weak23

SUITS = "SHDC"
RANKS = "23456789TJQKA"

# --- create 52 card deck


def create_deck():
    deck = [rank + suit for suit in SUITS for rank in RANKS]

    return deck


# --- deal 4 hands
def deal_hands(deck):
    random.shuffle(deck)

    # assume sequence is NESW
    hands = [deck[i::4] for i in range(4)]

    return hands


# --- calc HCP etc
def calc_hand_stats(hands):
    stats = {}

    # hcp
    stats["HCP"] = [sum(map(lambda x: hcp(x), hand)) for hand in hands]

    # shape of each suit 4432 etc

    stats["shape"] = [""] * 4

    for i in range(4):
        hand = hands[i]

        for s in range(4):
            suit = SUITS[s]
            stats["shape"][i] += str(len([card for card in hand if card[1] == suit]))

    return stats


# --- calc high card value of card
def hcp(c):
    return "JQKA".find(c[0]) + 1


# --- test a deal for criteria



def test_deal_constraints(func, hands, stats):

    return func(hands, stats)


# --- create PBN formatted string of hands


def PBN(hands):
    # must convert to bytes before passing to dds: the_text.encode('utf-8')

    # eg "N:QJ6.K652.J85.T98 873.J97.AT764.Q4 K5.T83.KQ9.A7652 AT942.AQ4.32.KJ3"

    # assume NESW
    pbn = "N:"

    for h in range(4):
        hand = hands[h]
        for s in range(4):
            cards = "".join([card[0] for card in hand if card[1] == SUITS[s]])
            pbn += cards

            if s < 3:
                pbn += "."

        if h < 3:
            pbn += " "

    return pbn


# --- main
def main():
    parser = argparse.ArgumentParser(
        description="Bridge hand generator for creating hands that fit certain criteria"
    )

    parser.add_argument(
        "-n", "--deals", help="Number of deals to generate", type=int, default=1
    )

    args = parser.parse_args()

    deals = args.deals

    deck = create_deck()

    start_time = time.time()

    for deal in range(deals):
        hands = []
        stats = {}

        attempts = 0


        while True:
            attempts += 1

            hands = deal_hands(deck)
            stats = calc_hand_stats(hands)

            if test_deal_constraints(deal_weak23, hands, stats):
                break

        print(PBN(hands))

    end_time = time.time()
    execution_time = end_time - start_time

    if deals == 1:
        pprint(hands)
        pprint(stats)
        print(f"attempts { attempts}")

    print(f"\nExecution time: {execution_time} seconds", file=sys.stderr)

if __name__ == "__main__":
    main()
