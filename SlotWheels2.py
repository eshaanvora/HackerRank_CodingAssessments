def slotWheels(history):
    result = 0
    maxColumn = []
    historyList = []
    for i in history:
        stageList = []
        for k in i:
            stageList.append(int(k))
        historyList.append(stageList)

    for k in range(len(historyList)-1):
        for i in historyList:
            maxNum = max(i)
            maxColumn.append(maxNum)
            i.remove(maxNum)

        result += max(maxColumn)
        maxColumn = []

    return result

history = ["712","246","365","312"]

print(slotWheels(history))
