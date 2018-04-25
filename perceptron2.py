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
        self.coeff = 0 #tuple 
        self.occurrence = 0
        self.error = 0
        


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
        pw = []
        th = []
        species = []
        for i in self.ord:
            sw.append(self.sepalWidth[i])
            pl.append(self.petalWidth[i])
            pw.append(self.petalLengh[i])
            species.append(self.species[i])
            th.append(self.truth[i])

        self.sepalWidth = sw[:]
        self.petalWidth = pl[:]
        self.petalLengh = pw[:]
        self.truth = th[:]
        self.species = species[:]

##        print(len(self.sepalWidth))
##        print("\n")
##        print(len(self.petalLengh))
##        print("\n")
##        print(len(self.truth))
##        print("\n")
        

     
        
    def processData(self): 

        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
    
        finished = False
        while not finished:

            self._shuffleSet()
            
            self.error = 0
            size = len(self.petalWidth)  
            for i in range(size): 
                sw = self.sepalWidth[i]
                pl = self.petalLengh[i]
                pw = self.petalWidth[i]
                truth = self.truth[i]
            
                model = (c1 * 1) + (c2 * sw) + (c3 * pl)
##                model = (c1 * 1) + (c2 * sw) + (c3 * pl) + (c4 * pw)
                    
                if truth > 0 and model < 0:
                    c1 = c1 + 1
                    c2 = c2 + sw
                    c3 = c3 + pl
##                   c4 = c4 + pw
                    self.error += 1
                    
                if truth < 0 and model >= 0:
                    c1 = c1 - 1
                    c2 = c2 - sw
                    c3 = c3 - pl
##                    c4 = c4 - pw
                    self.error += 1
         `          self.coeff = (c1, c2, c3
##                    self.coeff = (c1, c2, c3, c4)
                
                
            if self.error <= 5:
                finished = True
            
             

    def printResults(self):  
            
        
        #print("\n\n Petal Lengh VS Petal Width\n")
        #print("\n\n Petal Width VS Petal Lengh\n")
        #print("\n\n Sepal Width VS Petal Lengh\n")
        print("\n\n Sepal Width VS Petal Lengh VS Petal Width\n")
        print(" C1     |   C2    |   C3     |  errors")
        print("%.2f  |  %.2f  |  %.2f  |    %d\n"%(self.coeff[0], self.coeff[1], self.coeff[2], self.error))
##        print(" C1     |   C2    |   C3     |   C4     |  errors")
##        print("%.2f  |  %.2f  |  %.2f  |  %.2f  |    %d\n"%(self.coeff[0], self.coeff[1], self.coeff[2], self.coeff[3], self.error))
            

def main():

    p = Perceptron()

    p.loadData("perceptLab2.csv")

    p.processData()

    p.printResults()
 

main()
 


