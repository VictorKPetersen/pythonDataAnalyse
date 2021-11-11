from math import pow, sqrt
from statistics import mode

class Calculator:

    def __init__(self, numList):
        self.numList = numList
        self.sortList()

        self.minNumber = self.findMin()
        self.maxNumber = self.findMax()
        self.diffrenceNumber = self.findDiffrence()
        self.mostCommonNumber = self.findMostCommon()
        self.averageNumber = self.findAverage()
        self.varians = self.findVarians()
        self.spread = self.findSpread()
        self.observations = len(numList)


    def sortList(self):
        return self.numList.sort()

    def findMin(self):
        return self.numList[0]


    def findMax(self):
        return self.numList[len(self.numList)-1]

    def findMostCommon(self):
        return (mode(self.numList))

    def findDiffrence(self):
        return self.maxNumber - self.minNumber

    def findAverage(self):
        tempTotal = float()
        for i in self.numList:
            tempTotal = tempTotal + i
        return tempTotal/len(self.numList)


    def findVarians(self):
        tempNumber = float()
        for i in self.numList:
            tempNumber = tempNumber + pow((i - self.averageNumber), 2)
        return tempNumber/len(self.numList)


    def findSpread(self):
        return sqrt(self.varians)

    def printData(self):
        print(f"Smallest number is {self.minNumber} \nLargest number is {self.maxNumber}")
        print(f"There is a diffrence of {self.diffrenceNumber} between the smallest and largest number")
        print(f"The most common number is {self.mostCommonNumber}")
        print(f"There are {self.observations} observations")
        print(f"The average number is {self.averageNumber}")
        print(f"The varians is {self.varians}")
        print(f"the spread is {self.spread}")





