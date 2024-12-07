from collections.abc import Callable
import time


def timeit(fn: Callable) -> Callable:
    def timed(*args, timeit: bool = False, n: int = 10, **kwargs):
        if timeit:
            durations = []
            for _ in range(n):
                start = time.perf_counter_ns()
                fn(*args, **kwargs)
                end = time.perf_counter_ns()
                durations.append(end - start)
            return sum(durations)/len(durations)
        return fn(*args, **kwargs)
    return timed

@timeit
def report_safety(report: list[int]) -> int:
    valid_steps = {-1, -2, -3} if report[0] < report[1] else {1, 2, 3}
    for i in range(1, len(report)):
        if (report[i - 1] - report[i]) not in valid_steps:
            return 0
    return 1

@timeit
def report_safety_2(report: list[int]) -> tuple[int, int, int]:
    valid_steps = {-1, -2, -3} if report[0] < report[1] else {1, 2, 3}
    for i in range(1, len(report)):
        if (report[i - 1] - report[i]) not in valid_steps:
            return 0, i-1, i
    return 1, 0, 0

@timeit
def dampened_BF(report: list[int]) -> int:
    if report_safety(report):
        return 1
    for i in range(len(report)):
        test_report = [report[k] for k in range(len(report)) if k != i]
        if report_safety(test_report):
            return 1
    return 0

@timeit
def dampened_2(report: list[int]) -> int:
    outcome, remove_1, remove_2 = report_safety_2(report)
    if outcome != 1:
        if remove_1 == 1 and report_safety(report[1:]):
            return 1
        test_list_1 = [report[i] for i in range(len(report)) if i != remove_1]
        outcome_1 = report_safety(test_list_1)
        
        test_list_2 = [report[i] for i in range(len(report)) if i != remove_2]
        outcome_2 = report_safety(test_list_2)
        return max(outcome_1, outcome_2)
    return outcome


sample_report = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

report_safety(sample_report[0], timeit=True, n=100_000)

dampened_2(test_report, timeit=True, n=1_000_000)
dampened_BF(test_report, timeit=True, n=1_000_000)

for r in sample_report:
    print(report_safety(r))

for r in sample_report:
    print(dampened_2(r))

safe_reports = 0
dampened_safe_2 = 0
dampened_safe_BF = 0
with open('/Users/wardda/AOC_input_2', 'r') as file:
    while (new_line := file.readline().split()):
        report = [int(i) for i in new_line]
        safe_reports += report_safety(report)
        dampened_safe_BF += dampened_BF(report)
        dampened_safe_2 += dampened_2(report)
        if dampened_safe_BF != dampened_safe_2:
            print(report)
            break

print(safe_reports)
print(dampened_safe_2)
print(dampened_safe_BF)

test_report = [43, 40, 41, 44, 45, 46, 48, 51]

report_safety_2(test_report)