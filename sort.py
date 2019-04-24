import random
import time
import copy
import numpy as np

def generateRandomArr(n, rangeL, rangeU):  # generate a array for sort
    randomArr = []
    for i in range(n):
        randomArr.append(random.randint(rangeL, rangeU))  # random.randint return a integer in range [a,b] including both end points
    return randomArr

def selectionSort(dataToSort):  # delectionsort O(n^2)
    dataLength = len(dataToSort)
    for i in range(dataLength):
        minIndex = i
        for j in range(i+1, dataLength):
            if dataToSort[j] < dataToSort[minIndex]:
                minIndex = j
        dataToSort[i], dataToSort[minIndex] = dataToSort[minIndex], dataToSort[i]
    return dataToSort

def insertionSort(dataToSort):  #insertionsort O(n^2)
    dataLength = len(dataToSort)
    for i in range(1, dataLength):
        for j in range(i):
            if dataToSort[i-j] < dataToSort[i-j-1]:
                dataToSort[i-j], dataToSort[i-j-1] = dataToSort[i-j-1], dataToSort[i-j]
            else:
                break  # the inner loop of insertion sort can stop in advance
    return dataToSort

def insertionSortP(dataToSort):  # insertionsortP O(n^2)
    # the differences between insertionsort and advanced insertion is that the advanced version can reduce
    # the times of swaping numbers. And swaping needs more time than calculation
    dataLength = len(dataToSort)
    for i in range(1, dataLength):
        minValue = dataToSort[i]
        j = 0
        while i-j > 0:
            if minValue < dataToSort[i-j-1]:
                # minValue = dataToSort[i-j]
                dataToSort[i-j] = dataToSort[i-j-1]
            else:
                break
            j += 1
        dataToSort[i-j] = minValue
    return dataToSort

def bubbleSort(dataToSort):  # bubblesort O(n^2) find the biggest number and put it at the end of the list
    dataLength = len(dataToSort)
    for i in range(dataLength):
        for j in range(dataLength-i-1):
            if dataToSort[j] > dataToSort[j+1]:
                dataToSort[j], dataToSort[j+1] = dataToSort[j+1], dataToSort[j]
    return dataToSort

def shellSort(dataToSort):  # shellsort O(n^3/2) but the time to run this sort algorithm is much higher than the other
    # algorithm I donnot konw what is wrong, can you debug it?
    gap = dataLength = len(dataToSort)
    dataMat = np.mat(dataToSort)
    while gap >= 2:
        gap //= 2
        for i in range(gap, dataLength):
            locList = [i-x*gap for x in range(0, dataLength) if i-x*gap >= 0]
            locList.reverse()
            a = dataMat[0, locList].tolist()
            sortedSubSequence = insertionSortP(dataMat[0, locList].tolist()[0])
            dataMat[0, locList] = sortedSubSequence
    return dataMat.tolist()[0]



if __name__ == "__main__":
    dataArr = generateRandomArr(11, 666, 66666)
    # print(dataArr)
    lengthOfData = len(dataArr)
    resultArr = {}
    for sortMethod in [selectionSort, insertionSort, insertionSortP, bubbleSort, shellSort]:
        dataToSort = copy.copy(dataArr)
        startTime = time.time()
        sortedArr = sortMethod(dataToSort)
        # print(sortedArr)
        endTime = time.time()
        sortError = np.mat(sortedArr[1:]) - np.mat(sortedArr[:-1]) < 0
        error = np.sum(sortError, axis=1)[0, 0]
        resultArr[sortMethod.__name__] = {'timeUsed': endTime - startTime, 'error': error}
    print(resultArr)
