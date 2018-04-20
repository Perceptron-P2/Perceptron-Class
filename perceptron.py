from csv import reader
import random as rand
from sklearn import datasets

class Perceptron():

    def __init__(self, epochs):
        self.epochs = 5
        self. errors = 0
        self.weights = 0, 0, 0
        self.best_weights = 0, 0, 0
        self.least_errors = 100
        #change dataset for main project
        self.data = datasets.load_iris()

    # -- We can load from sklearn datasets or use this --
    # -- But then we need to parse it --
    # def loadData(self, filename):
    #     with open(filename, 'r') as file:
    #         csv_reader = reader(file)
    #         dataset = []
    #         for row in csv_reader:
    #             if not row:
    #                 continue
    #             dataset.append(row)
    #             #Printed dataset to make sure it works.
    #         #for row in dataset:
    #             #print(row)
    #     return dataset

    def shuffleSet(self, iris):
        rand.shuffle(iris)

        return iris

    #fix
    def processData(self, iris, weights):
        errors = 0
        current_truthval = [0] #whatever column that is in dataset
        truthval = 0 #coefficient match current truthval (This is just a place holder)

        for i in range(self.epochs, weights):
            #run perceptron rule and append errors when they occur...
            print("Processing Data")
            if current_truthval != truthval:
                errors += 1
        if self.errors < self.evalSol(self.least_errors, self.best_weights):
            self.least_errors = self.errors
            self.best_weights = weights
        self.shuffleSet(self.data)
        return self.least_errors, self.best_weights


    def evalSol(self, least_errors, weights):
        self.best_weights = 0, 0, 0
        least_errors = self.errors
        return least_errors


    def printResults(self):
        print(f"Best Weights: ", {self.best_weights})

    def tableInfo(self):
        for row in self.data:
            print(row)




def main():
    per = Perceptron(50)
    per.printResults()
    per.tableInfo()

main()