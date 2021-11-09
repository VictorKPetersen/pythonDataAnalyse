from math import pow, sqrt
from statistics import mode

class Calculator:
    minNumber = float()
    maxNumber = float()
    mostCommonNumber = float()
    averageNumber = float()
    varians = float()
    spread = float()

    def __init__(self, numList):
        self.numList = numList

        self.sortList()
        self.findMinMax()
        self.findMostCommon()
        self.findAverage()
        self.findVarians()
        self.findSpread()


    def sortList(self):
        return self.numList.sort()

    def findMinMax(self):
        self.minNumber = self.numList[0]
        self.maxNumber = self.numList[len(self.numList)-1]

    def findMostCommon(self):
        self.mostCommonNumber = (mode(self.numList))

    def findAverage(self):
        tempTotal = float()
        for i in self.numList:
            tempTotal = tempTotal + i
        self.averageNumber = tempTotal/len(self.numList)


    def findVarians(self):
        tempNumber = float()
        for i in self.numList:
            tempNumber = tempNumber + pow((i - self.averageNumber), 2)
        self.varians = tempNumber/len(self.numList)


    def findSpread(self):
        self.spread = sqrt(self.varians)





