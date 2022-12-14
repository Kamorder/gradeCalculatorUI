'''
12/7/22
@Kevin Parfien

This is how the data for the classes are stored. GradeSections is how the sections hold assignments and the classes class holds instances of the gradesection class.
This could be used as its own separate entity or linked to the UI made. 
'''
class inDict(Exception):

    pass

class classes: 
    def __init__(self, name=None):
       self.name = name
       self.totalGrade = {}

    def setName(self, newName):
        '''sets the name for the classes if the user wanted to change it'''
        self.name = newName

    def makeSection(self, sectionName):
        '''Makes a new section if requested'''
        if sectionName in self.totalGrade:
            raise inDict 
        self.totalGrade[sectionName] = gradeSections(sectionName)

    def setSectionWeight(self,name, weight):
        '''Sets the section weight for a section'''
        self.totalGrade[name].setWeight(weight)

    def renameSection(self, oldSectionName, sectionName):
        '''renames a section by deleting the old section and putting in the contents with a newname'''
        if sectionName in self.totalGrade:
            raise inDict 
        temp = self.totalGrade[oldSectionName]
        del(self.totalGrade[oldSectionName])
        self.totalGrade[sectionName] = temp
        self.totalGrade[sectionName].setName(sectionName)
    
    def setNewAssignment(self, name, nameA, nume, denom):
        '''adds a new assignment to said section'''
        self.totalGrade[name].makeAssignment(nameA, nume, denom)
    
    def renameAssignment(self, name,nameNew, nameOld):
        '''gives the ability to rename an assignment'''
        self.totalGrade[name].renameAssignment(nameNew, nameOld)
    
    def redoAssignment(self, name, nameA, newNume, newDenom):
        '''gives the ability to redo the numerator and denominator for an assignment'''
        self.totalGrade[name].reAssignmentGrades(nameA,newNume,newDenom)
    
    def delAssignment(self,name,nameA):
        '''gives the ability to delete an assignment'''
        self.totalGrade[name].delAssignments(nameA)

    def getTotalWeight(self):
        '''get the total weight of all the sections in a class'''
        totalWeight = 0 
        for val in self.totalGrade.values():
            totalWeight += val.getWeight()
        return totalWeight

    def getCurrentGrade(self):
        '''get the current grade for a class'''
        totalWeight = self.getTotalWeight()
        currentWeight = 0
        for val in self.totalGrade.values():
            currentWeight += val.currentWeighting()
        if totalWeight == 0:
            return float(currentWeight / 1) * 100
        return float(currentWeight / totalWeight) * 100
        


    def printAll(self):
        '''Print the current grade of the class'''
        print(f'''Tester:
Name:{self.name}
Section Names{self.totalGrade.keys()}
Grade: {self.getCurrentGrade():.02F}
Total Points Possible: {self.getTotalWeight()}
        
''')
        for name in self.totalGrade.values():
            name.printAll()
        



class gradeSections:
    def __init__(self, name):
        self.sectName = name
        self.weight = 0
        self.assignments = {}
    
    def setName(self, name):
        '''set the name for a section'''
        self.sectName = name

    def setWeight(self, num):
        '''set a weight for a section'''
        self.weight = num
    
    def getWeight(self):
        '''return the weight'''
        return self.weight

    def makeAssignment(self, name, numer, denom):
        '''make a new assignment'''
        if name in self.assignments:
            raise inDict
        self.assignments[name] = [numer, denom]

    def renameAssignment(self, newName, oldName):
        '''rename an assignment'''
        if newName in self.assignments:
            raise inDict
        self.assignments[newName] = self.assignments[oldName]
        del self.assignments[oldName]
    
    def reAssignmentGrades(self, name, newNum, newDenom):
        '''change the numerator and denominator for an assignment'''
        self.assignments[name] = [newNum, newDenom]

    def delAssignments(self, assignName):
        '''delete an assignment'''
        del self.assignments[assignName]
    
    def getPercent(self):
        '''get the percentage for a section using the assignments'''
        totalnum = 0
        totaldenum = 0
        for grade in self.assignments.values():
            totalnum += grade[0]
            totaldenum += grade[1]
        if totaldenum == 0:
            return float(totalnum/1) * 100
        return float(totalnum/totaldenum) * 100
   
    def getAssignmentPercent(self, name):
        '''get the percentage for an assignment'''
        if self.assignments[name][1] == 0:
            return float(self.assignments[name][0] / 1) * 100
        return float(self.assignments[name][0]/ self.assignments[name][1]) * 100

    def currentWeighting(self):
        '''find out the weight * percentage'''
        return self.weight * (self.getPercent() /100)

    

    def printAll(self):
        '''Prints the section nmae, weight, and percent'''
        print(f'''

        Section Name: {self.sectName}
        Weighting: {self.weight}
        Your Weighting: {self.currentWeighting():.02F}
        Total Percent: {self.getPercent():.02F}

        ''')
        for assign, gradeList in self.assignments.items():
            print(f'\t \t Name:{assign} grade: {gradeList[0]} / {gradeList[1]} Percent {self.getAssignmentPercent(assign):.02F}')
    
   
        
        
        

if __name__ == '__main__':
    pass


    
