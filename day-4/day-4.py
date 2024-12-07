from typing import NamedTuple


small_puzzle = (
    """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    .split()
)

# For each X, it can be the end of up to 8 XMAS
# The _brute force_ method is to find each X, then check all 8 possibilities.
"""
There are eight possible correct per X. Indicate these using compass directions.

if in row 0, 1, or 2 then NW, N, and NE _cannot_ be valid.
if in column 0, 1, or 2, then NW, W, and SW _cannot_ be valid
if in column -1, -2, or -3, then NE, E, and SE _cannot_ be valid.
if in row -1, -2, or -3, then SW, S, and SE _cannot_ be valid.
"""
class Step(NamedTuple):
    vertical: int
    horizontal: int


class Instruction(NamedTuple):
    step: Step
    bounds: tuple[str, str]


directions = [
    Step(-1, -1), Step(-1, 0), Step(-1, 1),
    Step(0, -1),               Step(0, 1),
    Step(1, -1),  Step(1, 0),  Step(1, 1)
]

# TODO: Fix the logic in these
small_puzzle_bounding = {
    'top': lambda x: x in [0, 1, 2],
    'left': lambda y: y in [0, 1, 2],
    'right': lambda y: y in [len(small_puzzle[0]) - x for x in (1, 2, 3)],
    'bottom': lambda x: x in [len(small_puzzle) - val for val in (1, 2, 3)],
    'other': lambda x: True
}

check_instructions = {
    'NW': Instruction(Step(-1, -1), ('top', 'left')),
    'N': Instruction(Step(-1, 0), ('top', 'other')),
    'NE': Instruction(Step(-1, 1), ('top', 'right')),
    'W': Instruction(Step(0, -1), ('other', 'left')),
    'E': Instruction(Step(0, 1), ('other', 'right')),
    'SW': Instruction(Step(1, -1), ('bottom', 'left')),
    'S': Instruction(Step(1, 0), ('bottom', 'other')),
    'SE': Instruction(Step(1, 1), ('bottom', 'right'))
}

found_words = 0
for r in range(len(small_puzzle)):
    for c in range(len(small_puzzle[r])):
        if small_puzzle[r][c] == 'X':
            print(f'Found X at {r}, {c}! Checking for XMAS!')
            for instruction in check_instructions.values():
                    if small_puzzle_bounding[instruction.bounds[0]](r):
                        print('passed row bound check')
                #     and small_puzzle_bounding[instruction.bounds[1]](c)
                #     and small_puzzle[r + instruction.step.vertical][c + instruction.step.horizontal] == 'M'
                #     and small_puzzle[r + (2 * instruction.step.vertical)][c + (2 * instruction.step.horizontal)] == 'A'
                #     and small_puzzle[r + (3 * instruction.step.vertical)][c + (3 * instruction.step.horizontal)] == 'S'
                # ):
                #     found_words += 1
print(found_words)
