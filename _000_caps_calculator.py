
# Se puso 1.000.000 como límite a arena 16 para tener un valor.

def determine_caps(rank):
    # dict = {arena : [min, max, caps]}
    arenas = {1: [0, 300, 10], 2: [300, 650, 10], 3: [650, 1200, 10],
              4: [1200, 1800, 12], 5: [1800, 2500, 18], 6: [2500, 3200, 25],
              7: [3200, 3900, 32], 8: [3900, 4600, 39], 9: [4600, 5300, 46],
              10: [5300, 6000, 53], 11: [6000, 6500, 60], 12: [6500, 7000, 65],
              13: [7000, 7500, 69], 14: [7500, 8000, 73], 15: [8000, 8500, 76],
              16: [8500, 1000000, 78]}

    for arena in range (1,17):
        if rank >= arenas[arena][0] and rank < arenas[arena][1]:
            caps = arenas[arena][2]

    return caps


def determine_plus_minus(rank, margin):
    # dict = {arena: [min, max, +, -]}
    arenas = {1: [0, 300, 0, 0], 2: [300, 650, 0, 0], 3: [650, 1200, 2, 0],
              4: [1200, 1800, 6, -2], 5: [1800, 2500, 7, -6], 6: [2500, 3200, 7, -7],
              7: [3200, 3900, 7, -7], 8: [3900, 4600, 7, -7], 9: [4600, 5300, 7, -7],
              10: [5300, 6000,7, -7], 11: [6000, 6500, 5, -7], 12: [6500, 7000, 4, -5],
              13: [7000, 7500, 4, -4], 14: [7500, 8000, 3, -4], 15: [8000, 8500, 2, -3],
              16: [8500, 1000000, 0, -2]}

    plus = 0
    minus = 0

    for arena in range (1,17):

        if rank >= arenas[arena][0] and rank < arenas[arena][1] and abs(arenas[arena][1] - rank) <= margin:
            plus = arenas[arena][2]
        elif rank >= arenas[arena][0] and rank < arenas[arena][1] and abs(rank - arenas[arena][0]) <= margin:
            minus = arenas[arena][3]

    return plus, minus


