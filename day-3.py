#############################
## For part 1
#############################

def find_digit(start_index, case: str, closer: str) -> tuple[int, int]:
    """Look for a digit to multiply in a potentially malformed instruction.
    
    Returns the found digit, and the next index in the string to check.
    Malformed cases return a 0 for the found digit.
    """
    end_index = start_index
    if case[start_index] == closer:
        return 0, end_index + 1
    while True and end_index < len(case):
        if case[end_index].isdigit():
            end_index += 1
            continue
        break
    if end_index < len(case) and case[end_index] == closer:
        return int(''.join(case[start_index: end_index])), end_index + 1
    return 0, end_index


def command_check(case: str) -> tuple[int, int]:
    """Found a string starting with 'm'. Check if it is a valid command.
    
    Returns the sum to add to the total (or 0 if this case is malformed)
    and the index at which to continue searching.
    """
    index = 0
    for c in 'mul(':
        if case[index] != c:
            return 0, index
        index += 1

    first_digit, index = find_digit(index, case, ',')
    if not first_digit:
        return 0, index
    second_digit, index = find_digit(index, case, ')')
    return first_digit * second_digit, index


def solve(case: str) -> int:
    i, out = 0, 0
    while i < len(case):
        add_to_i = 1
        if case[i] == 'm':
            add_to_out, add_to_i = command_check(case[i:])
            out += add_to_out
        i += add_to_i
    return out


example = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)'
solve(example)

with open('/Users/wardda/advent-of-code/AOC_input_3', 'r') as file:
    print(solve(file.read()))


#############################
## For part 2
#############################

def find_digit_2(start_index, case: str, closer: str) -> tuple[int, int]:
    """Look for a digit to multiply in a potentially malformed instruction.
    
    Returns the found digit, and the next index in the string to check.
    Malformed cases return a 0 for the found digit.
    """
    end_index = start_index
    if case[start_index] == closer:
        return 0, end_index + 1
    while True and end_index < len(case):
        if case[end_index].isdigit():
            end_index += 1
            continue
        break
    if end_index < len(case) and case[end_index] == closer:
        return int(''.join(case[start_index: end_index])), end_index + 1
    return 0, end_index


def command_check_2(case: str) -> tuple[int, int]:
    """Found a string starting with 'm'. Check if it is a valid command.
    
    Returns the sum to add to the total (or 0 if this case is malformed)
    and the index at which to continue searching.
    """
    index = 0
    for c in 'mul(':
        if case[index] != c:
            return 0, index
        index += 1

    first_digit, index = find_digit_2(index, case, ',')
    if not first_digit:
        return 0, index
    second_digit, index = find_digit_2(index, case, ')')
    return first_digit * second_digit, index


def do_switch(case: str, current_state: bool) -> tuple[bool, int]:
    """Found a string starting with 'd'. Check if we need to switch do.
    
    Returns a bool with the state after applying the command, if it is a valid command.
    Also returns the index at which to continue searching.
    """
    if case[:2] != 'do':
        return current_state, 1
    if case[2:7] == "n't()":
        return False, 7
    if case[2:4] == '()':
        return True, 4
    return current_state, 2


def solve_2(case: str) -> int:
    i, out, do = 0, 0, True
    while i < len(case):
        add_to_i = 1
        if case[i] == 'd':
            # need to check for do switch
            do, add_to_i = do_switch(case[i:], do)
        elif case[i] == 'm' and do:
            add_to_out, add_to_i = command_check_2(case[i:])
            out += add_to_out
        i += add_to_i
    return out


example_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
solve_2(example_2)

with open('/Users/wardda/advent-of-code/AOC_input_3', 'r') as file:
    print(solve_2(file.read()))