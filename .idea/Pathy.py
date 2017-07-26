# This is used to confirm that I understand 2d arrays in Python

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = 4, 4, 1

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [1, 2], [2, 3]

for i in range(e):
    ei = int(3)  # the index of an exit gateway node

# game loop
while True:
    si = 2  # The index of the node on which the Skynet agent is positioned this turn

    print(n1[0], ", ", n2[0])
    print(n1[1], ", ", n2[1])

    # Identify if the agent is one node from the exit and terminate if so
    # for i, j in range(n1, n2):
    #     if ((si == i) and (ei == j)):
    #         print(i, j)
    #     elif ((si == j) and (ei == i)):
    #         print(j, i)
    #
    #     # Identify if exit node is part of linked pair and terminate if so
    #     for i, j in range(n1, n2):
    #         if (ei == i):
    #             print(i, j)
    #         elif (ei == j):
    #             print(j, i)
    #
    #         # Otherwise, terminate any pair
    # print(n1, n2)
