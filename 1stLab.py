accuracy = 1e-3
accuracy_n = 3


def main():
    # Gauss
    input = [[2.958, 0.147, 0.354, 0.238, 0.651], [0.127, 2.395, 0.256, 0.273, 0.898],
             [0.403, 0.184, 3.815, 0.416, 0.595], [0.259, 0.361, 0.281, 3.736, 0.389]]
    m = Matrix(input)
    m.gauss_calc()

    # Yakobi
    # check convergence
    for i in range(len(input)):
        sum_ = 0
        for j in range(len(input)):
            if i != j:
                sum_ += abs(input[i][j])

        if not abs(input[i][i]) > sum_:
            print("FAILED Yakobi: convergence test is failed")
            return

    print("PASSED Yakobi: convergence test is passed")

    import random
    solution_now = random.sample(range(1, 10), len(input))
    solution_next = [0] * len(input)

    while is_iter(solution_now, solution_next):
        for i in range(len(input)):
            solution_next[i] = input[i][len(input)]
            for j in range(len(input)):
                if i != j:
                    solution_next[i] -= input[i][j] * solution_now[j]
            solution_next[i] /= input[i][i]
        solution_now, solution_next = solution_next, solution_now

    print(', '.join('x{} = {}'.format(i + 1, round(x, accuracy_n)) for i, x in enumerate(solution_now)))


def is_iter(now, next):
    return max([abs(x1 - x2) for x1, x2 in zip(now, next)]) >= accuracy


class Matrix:
    def __init__(self, data):
        self.data = [row[:] for row in data]

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def sub(self, row1, row2):
        for i in range(len(self.data[row1])):
            self.data[row1][i] -= self.data[row2][i]

    def div(self, row, num):
        for i in range(len(self.data[row])):
            self.data[row][i] /= num

    def print(self):
        for d in self.data:
            print(d)

    def gauss_calc(self):
        for step in range(len(self.data)):

            for r in range(step, len(self.data)):
                if self.data[r][step] != 0:
                    self.div(r, self.data[r][step])
                    if self.data[step][step] == 0:
                        self.swap(step, r)
                if self.data[step][step] == 0:
                    print("FAILED GAUSS: Matrix determinant is equal to ZERO")
                    return

            for r in range(step + 1, len(self.data)):
                if self.data[r][step] != 0:
                    self.sub(r, step)

        solution = [None] * len(self.data)

        for step in range(len(self.data) - 1, -1, -1):
            value = self.data[step][len(self.data)]
            for i in range(step + 1, len(self.data)):
                value -= self.data[step][i] * solution[i]

            solution[step] = value / self.data[step][step]

        print("PASSED GAUSS: Matrix determinant is not equal to ZERO")
        print(', '.join('x{} = {}'.format(i + 1, round(x, accuracy_n)) for i, x in enumerate(solution)))

if __name__ == '__main__':
    main()
