mas = [
    [2, 4, 6],
    [3, 9, 1],
    [2, 2, 1]
]

column_sums = [0] * len(mas[0])

for row in mas:
    for i, value in enumerate(row):
        column_sums[i] += value

print(column_sums)
print("Відсортований масив: ")
col_sum = [sum(col) for col in zip(*mas) ]
sorting = sorted(col_sum)
print(sorting)