def findAverage(list):
    totalEmuration = int()
    average = int()
    for num in list:
        totalEmuration = num + totalEmuration
        average = totalEmuration/len(list)
    return average


def findVariation():
    print("")



def findSpread():
    print("")


def main():
    numList = [1, 2, 3, 4, 5]
    findAverage(numList)


if __name__ == '__main__':
    main()