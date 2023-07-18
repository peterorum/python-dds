#! /c/Users/porum/AppData/Local/Microsoft/WindowsApps/python3
# /usr/bin/python

import dds
import ctypes
import hands
import functions

dlPBN = dds.dealPBN()

threadIndex = 0
line = ctypes.create_string_buffer(80)

dds.SetMaxThreads(0)

for handno in range(1):
    dlPBN.trump = hands.trump[handno]
    dlPBN.first = hands.first[handno]

    dlPBN.currentTrickSuit[0] = 0
    dlPBN.currentTrickSuit[1] = 0
    dlPBN.currentTrickSuit[2] = 0

    dlPBN.currentTrickRank[0] = 0
    dlPBN.currentTrickRank[1] = 0
    dlPBN.currentTrickRank[2] = 0

    dlPBN.remainCards = hands.PBN[handno]

    target = -1
    solutions = 3
    mode = 0
    fut3 = dds.futureTricks()

    res = dds.SolveBoardPBN(
        dlPBN,
        target,
        solutions,
        mode,
        ctypes.pointer(fut3),
        0)

    if res != dds.RETURN_NO_FAULT:
        dds.ErrorMessage(res, line)
        print("DDS error {}".format(line.value.decode("utf-8")))

    line = "SolveBoardPBN, hand {}:".format(
        handno + 1)

    functions.PrintPBNHand(line, dlPBN.remainCards)