
import sys
def read_input_stdin():
    input = sys.stdin.read().strip().split()
    C = int(input[0])
    n = int(input[1])
    values = []
    weights = []
    index = 2
    for _ in range(n):
        values.append(int(input[index]))
        weights.append(int(input[index + 1]))
        index += 2
    return C, n, values, weights