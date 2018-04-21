import csv
import random

class Perceptron:

    def __init__(self):
 
        self.sepalWidth = []
        self.petalLengh = []
        self.petalWidth = []
        self.species = []
        self.ord = []
        self.truth = [] 
        self.coeff = []
        self.c_coeff = 0 #tuple
        self.error = 0
        self.occurrence = 0
        


    def loadData(self, filename):
        
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if 'Sepal Width' in row and row['Sepal Width'] != '':
                    self.sepalWidth.append(float(row['Sepal Width']))
                    
                if 'Petal Length' in row and row['Petal Length'] != '':
                    self.petalLengh.append(float(row['Petal Length']))
                    
                if 'Petal Width' in row and row['Petal Width'] != '':
                    self.petalWidth.append(float(row['Petal Width']))
                    
                if 'Species' in row and row['Species'] != '':
                    self.species.append(row['Species'])
                    
                if 'Truth' in row and row['Truth'] != '':
                    self.truth.append(int(row['Truth']))
                
            csvfile.close()

        for i in range(len(self.sepalWidth)):
            self.ord.append(i)

##        print(self.sepalWidth)
##        print("\n")
##        print(self.petalLengh)
##        print("\n")
##        print(self.petalWidth)
##        print("\n")
##        print(self.species)
##        print("\n")
##        print(self.ord)
##        print("\n")
            

    def _shuffleSet(self):

        random.shuffle(self.ord)
        sw = []
        pl = []
        species = []
        for i in self.ord:
            sw.append(self.petalWidth[i])
            pl.append(self.petalLengh[i])
            species.append(self.species[i])

        self.petalWidth = sw[:]
        self.petalLengh = pl[:]
        self.species = species[:]
        


    def evalSol(self):

        #Empty dictionnary
        coeffDic = {}

        #Save the coefficients as keys in the dictionnary and their values initialized to 0
        for i in self.coeff:
            coeffDic[i] = 0

        #Save the occurence of each coefficients
        for i in self.coeff:
            if i in coeffDic:
                coeffDic[i] += 1

        #Save the occurences in the list myOcc in descendig order
        myOcc = sorted(coeffDic.values(), reverse=True)

        #Retrieve the biggest occurence
        maxError = myOcc[0]

        #Get the c-coefficients that appear mostly
        for coeff, occ in coeffDic.items():
            if maxError == occ:
                self.c_coeff = coeff 
                self.occurrence = occ

        #number of error
        self.error = len(self.petalWidth) - self.occurrence       
        
    
        
    def processData(self): 

        c1 = 0
        c2 = 0
        c3 = 0
    
        finished = False
        while not finished:

            self.model = []
            self.coeff = []

            size = len(self.petalWidth)  
            for i in range(size): 
                sw = self.petalWidth[i]
                pl = self.petalLengh[i]
                #pw = self.petalWidth[i]
                truth = self.truth[i]
            
 
            
                model = (c1 * 1) + (c2 * sw) + (c3 * pl) 
                    
                if truth > 0 and model < 0:
                    c1 = c1 + 1
                    c2 = c2 + sw
                    c3 = c3 + pl
                    
                if truth < 0 and model >= 0:
                    c1 = c1 - 1
                    c2 = c2 - sw
                    c3 = c3 - pl

                self.model.append(model)
                self.coeff.append((c1, c2, c3))

                self.evalSol()
                
                if self.error <= 10:
                    finished = True
                    
                else:
                    self._shuffleSet()


            print(" C1   |   C2   |   C3   |  occ  |  errors")
            print("%.2f  |  %.2f  |  %.2f  |  %d   |    %d\n"%(self.c_coeff[0], self.c_coeff[1], self.c_coeff[2], self.occurrence, self.error))
                    


    def printResults(self):  
            
        print(" C1   |   C2   |   C3   |  occ  |  errors")
        print("%.2f  |  %.2f  |  %.2f  |  %d   |    %d\n"%(self.c_coeff[0], self.c_coeff[1], self.c_coeff[2], self.occurrence, self.error))
            

def main():

    p = Perceptron()

    p.loadData("perceptLab2.csv")

    p.processData()

    p.printResults()
 

main()
 


