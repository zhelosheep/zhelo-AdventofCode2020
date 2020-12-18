def main():
    expenses = []
    f = open('day1.txt', 'r')
    for line in f:
        expenses.append(int(line))
    
    expenses.sort()
    max = len(expenses)
    for i in range(0, max):
        for f in range(max-1, i, -1):
            sum = expenses[i] + expenses[f]
            if sum == 2020:
                print(expenses[i], expenses[f])
                print(expenses[i] * expenses[f])
                return


if __name__ == "__main__":
    main()