from calculator import Calculator

def main():
    numbersList = [-10, 7, -4, 8, -7, -10, 3, 5, 8, 3, -4, 2, -5, 1, 8, -11, 6, 6, -9, 5, -12,-10, 1, -7, -10, 2, -7, -11]

    calc1 = Calculator(numbersList)

    print(f"Smallest number is {calc1.minNumber} \nLargest number is {calc1.maxNumber}")
    print(f"The most common number is {calc1.mostCommonNumber}")
    print(f"The average number is {calc1.averageNumber}")
    print(f"The varians is {calc1.varians}")
    print(f"the spread is {calc1.spread}")



if __name__ == '__main__':
    main()