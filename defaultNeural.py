import csv
import random

dataset = []
with open('data.csv') as _file:
    data = csv.reader(_file, delimiter=',')
    for line in data:
        line = [float(element) for element in line]
        dataset.append(line)

def trainTestSplit(dataset, percentage):
    percent = percentage * len(dataset) // 100
    trainData = random.sample(dataset, percent)
    testData = [data for data in dataset if data not in trainData]

    def mount(dataset):
        x, y = [],[]
        for data in dataset:
            x.append(data[1:3])
            y.append(data[0])
        return x,y
    
    trainX, trainY = mount(trainData)
    testX, testY = mount(testData)
    return trainX, trainY, testX, testY