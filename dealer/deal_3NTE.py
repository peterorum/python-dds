from constants import NORTH, EAST, SOUTH, WEST
import re


def deal_3NTE(hands, stats):
    hcp = stats["HCP"]
    shape = stats["shape"]

    # 3NT E

    ok = (
        hcp[EAST] >= 15
        and hcp[EAST] <= 17
        and hcp[WEST] + hcp[EAST] >= 25
        and hcp[WEST] + hcp[EAST] <= 32
        and re.search("4432|4423", shape[EAST])
        and re.search("[2-5][2-5][2-5][2-5]", shape[WEST])
    )

    return ok
