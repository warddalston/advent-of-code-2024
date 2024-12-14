###################
# PART 1 SOLUTION #
###################
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

with open("input.txt", 'r') as file:
    puzzle = file.read().split()

small_puzzle_bounding = {
    'top': lambda x: x not in [0, 1, 2],
    'left': lambda y: y not in [0, 1, 2],
    'right': lambda y: y not in [len(puzzle[0]) - x for x in (1, 2, 3)],
    'bottom': lambda x: x not in [len(puzzle) - val for val in (1, 2, 3)],
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
for r in range(len(puzzle)):
    for c in range(len(puzzle[r])):
        if puzzle[r][c] == 'X':
            print(f'Found X at {r}, {c}! Checking for XMAS!')
            for instruction in check_instructions.values():
                if (
                    small_puzzle_bounding[instruction.bounds[0]](r)
                    and small_puzzle_bounding[instruction.bounds[1]](c)
                    and puzzle[r + instruction.step.vertical][c + instruction.step.horizontal] == 'M'
                    and puzzle[r + (2 * instruction.step.vertical)][c + (2 * instruction.step.horizontal)] == 'A'
                    and puzzle[r + (3 * instruction.step.vertical)][c + (3 * instruction.step.horizontal)] == 'S'
                ):
                    found_words += 1
print(found_words)

# Now we are looking for X-mas.
# There are four ways to write an x-mas
# M . M    M . S    S . M    S . S
# . A .    . A .    . A .    . A .
# S . S    M . S    S . M    M . M
# We need to scan through the input, stopping everytime we find an A to search.
# We can skip A's in the first row, last row, first column, and last column,
# As they are never the center of an X.
# We check the NW first. If it is S, we then check for M in SE. (and vice versa
# for if NW is M). If a MAS is found, then check in NE and SW. At any failure,
# continue scanning until the next A.

found_mas = 0
locations = []
for r in range(1, len(puzzle) -1):
    for c in range(1, len(puzzle[r]) - 1):
        if puzzle[r][c] == 'A':
            print(f'FOund A at {r}, {c}! Checking for X-MAS!')
            if (
                (
                    (puzzle[r + 1][c + 1] == 'M' and puzzle[r - 1][c - 1] == 'S')
                    or
                    (puzzle[r + 1][c + 1] == 'S' and puzzle[r - 1][c - 1] == 'M')
                )
                and
                (
                    (puzzle[r + 1][c - 1] == 'M' and puzzle[r - 1][c + 1] == 'S')
                    or
                    (puzzle[r - 1][c + 1] == 'M' and puzzle[r + 1][c - 1] == 'S')
                )
            ):
                found_mas += 1
                locations.append((r, c))
print(found_mas)
#print(locations)
