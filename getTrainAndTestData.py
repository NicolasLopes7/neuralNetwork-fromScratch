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

trainX, trainY, testX, testY = trainTestSplit(dataset, 80)

def signal(u):
    return 1 if u >= 0 else -1

def adjust(w, x, d, y):
    learning_rate
    return w + learning_rate * (d-y) * x

def perceptronFit(x, d):
    epoch = 0
    w = [random.random() for i in range(3)]
    print(w)

    while True:
        error = False
        for i in range(len(x)):
            u = sum(w[0] * -1, w[1] * x[i][0], w[2] * x[i][1])
            y = signal(u)
            if y != d[i]:
                w[0] = adjust(w[0], -1, d[i], y)
                w[1] = adjust(w[1], x[i][0], d[i], y)
                w[2] = adjust(w[2], x[i][1], d[i], y)
                error = True
            epoch += 1
            if error is False or epoch == 1000:
                break
    print(epoch)