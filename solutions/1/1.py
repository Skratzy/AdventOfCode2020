def solve():
    f = open("1.txt", "r")
    values = []
    for line in f:
        values.append(int(line))
    values.sort()
    sum_to_get = 2020
    for i in range(len(values)):
        val1 = values[i]
        for j in range(i, len(values)):
            val2 = values[j]
            _sum = val1 + val2
            if _sum == sum_to_get:
                return val1 * val2


print(solve())
