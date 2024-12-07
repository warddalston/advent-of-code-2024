list_1, list_2 = [], []
with open('/Users/wardda/Desktop/AOC_input_1', 'r') as inputs:
    while (new_line := inputs.readline().split()):
        list_1.append(int(new_line[0]))
        list_2.append(int(new_line[1]))

list_1.sort()
list_2.sort()
out = 0
for i, j in zip(list_1, list_2):
    out += abs(i - j)

counts = {}
for j in list_2:
    if j not in counts:
        counts[j] = 1
    else:
        counts[j] += 1

out_2 = 0
for i in list_1:
    if i in counts:
        out_2 += counts[i] * i

print(out)
print(out_2)