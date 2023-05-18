def bubSort(numList):
    swapNumber = 0
    for valNum in range(len(numList) - 1, 0, -1):
        for valNum2 in range(valNum):

            if numList[valNum2 + 1] < numList[valNum2]:
                placeholder = numList[valNum2]
                numList[valNum2] = numList[valNum2 + 1]
                numList[valNum2 + 1] = placeholder
                swapNumber += 1
    print(swapNumber)


numList = [10,7,3,5,8,9]
bubSort(numList)