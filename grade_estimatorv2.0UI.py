'''
12/7/22
@Kevin Parfien
grade_estimatorv2.0UI

Essentially what this does is it controls the UI and what is displayed on the UI. It does the whole process including the grade calculation. 
Has a whole series of methods in GradeCalcUI which handles the UI creation and edits. Also manages the class from grade_estimatorv2.0
'''

from grade_estimatorv2_0 import classes
import tkinter as tk


class GradeCalcUI:
    def __init__(self):
        '''Initializes all the important parts of the gradecalc class'''
        self.sectionEntryList = []
        self.sectionWeightList = []
        self.assignmentButtonList = []
        self.assignmentLst = []
        self.frameLst = []
        self.editButtonLst = []
        self.sectionNum = 2
        self.assignmentNum = 3
        self.initCanvas()
        self.labels()
        self.tkVars()
        self.uiEntries()
        self.uiButtons()
        self.shownresults = False
        
        


    def initCanvas(self):
        '''Initializes the canvas including setting up the scrollbar'''
        self.root = tk.Tk()
        self.root.title("Grade Calculator")
        self.root.geometry('1000x1000')
        self.root.resizable(0,0)
        self.scrollbarFullSetup()

    def onMW(self,event):
        '''Command which allows the scroll bar to work'''
        self.mainCanvas.yview_scroll(-1 * int((event.delta)), "units")

    def scrollbarFullSetup(self):
        '''Sets up the scrollbar which requires some initiation of the canvas'''
        self.mainFrame = tk.Frame(self.root)

        self.mainFrame.pack(fill=tk.BOTH, expand=1)
        self.mainCanvas = tk.Canvas(self.mainFrame)
        self.mainCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollBar = tk.Scrollbar(self.mainCanvas, orient='vertical',command=self.mainCanvas.yview )

        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.mainCanvas.configure(yscrollcommand=self.scrollBar.set)
        self.mainCanvas.bind('<Configure>', lambda e: self.mainCanvas.configure(scrollregion=self.mainCanvas.bbox(tk.ALL)))
        self.mainCanvas.bind_all("<MouseWheel>", self.onMW)
        self.rootFrame = tk.Frame(self.mainCanvas)
        self.scrollBar
        self.mainCanvas.create_window((0,0),window=self.rootFrame, anchor=tk.NE)
        


    
    def updateScroll(self):
            '''Allows there to be an update to the scroll feature and assures that the results are not visible if there is an update to the class'''
            self.updateButtons()
            self.root.update()
            self.mainCanvas.configure(scrollregion=self.mainCanvas.bbox(tk.ALL))
            self.removeResults()
                
           

 

    def tkVars(self):
        '''Class name gets set up'''
        self.classN = tk.StringVar()

    def updateButtons(self):
        '''Updates the position of the quit, result and the addButton'''
        newRow= self.sectionNum + 2 
        self.quitButton.grid(row= newRow)
        self.resultButton.grid(row=newRow)
        self.addButton.grid(row=newRow)

    def labels(self):
        '''Initializes the first few labels in the  in the class and puts it in its own frame'''
        self.startFrame = tk.Frame(self.rootFrame)
        self.startFrame.grid(row=0, column=0, columnspan=3)
        
        for x in range(5):
                self.startFrame.columnconfigure(x, minsize=100)

        
        self.welcomeLabel = tk.Label(self.startFrame, text='Welcome to the Grade Calculator V2.0', foreground='white')
        self.welcomeLabel.grid(row=0,column=0, sticky=tk.W)
        
        self.className = tk.Label(self.startFrame, text='Please enter your class name:', foreground='white')
        self.className.grid(row=1, column= 0,sticky=tk.W)
        
        

        self.Spacer = tk.Label(self.rootFrame, text='\t         ', foreground='white')
        self.Spacer.grid(row=0,column=3,sticky= tk.E)
        

    def uiEntries(self):
        '''First Entry box for the class'''
        self.classEntry = tk.Entry(self.startFrame, textvariable = self.classN)
        self.classEntry.grid(row=1, column=1, columnspan=2)
        


    def uiButtons(self):
        '''Initilization of the submit, result and quit button'''
        self.submitButton = tk.Button(self.startFrame, text='Submit',command=self.lockname)
        self.submitButton.grid(row=1, column=3,sticky=tk.NW)
        self.resultButton = tk.Button(self.rootFrame, text='Result', command=self.printResults)
        self.resultButton.grid(row=100, column= 4)
        self.quitButton = tk.Button(self.rootFrame,text="Quit", command=self.root.destroy)
        self.quitButton.grid(row=100, column=5, sticky=tk.SE)
    
    def printResults(self):
        '''Shows the current percentage in the class, does a few checks to make sure that all the entry boxes are disabled'''
        try:
            if (len(self.sectionEntryList) == 0 and len(self.assignmentLst) == 0 ):
                raise ValueError

            for entry in self.sectionEntryList:
                if(entry.cget('state') != 'disabled'):
                    raise ValueError
            for assignmentMng in self.assignmentLst:
                for assignment in assignmentMng:
                    if(assignment[0].cget('state') != 'disabled'):
                        raise ValueError
            if self.shownresults:
                self.removeResults()
            self.resultFrame = tk.Frame(self.rootFrame)
            self.resultFrame.grid(row=self.sectionNum + 3, column = 0,columnspan=4)
            gradeLabel = tk.Label(self.resultFrame, text=f'Current Percentage in your class {self.mainClass.name} is {self.mainClass.getCurrentGrade():.02f}%')
            gradeLabel.grid(row=0, column= 0, sticky=tk.W)
            self.shownresults = True
        except:
            pass
            
                
    def removeResults(self):
        '''Removes the shown results from the screen'''
        if(self.shownresults):
            self.resultFrame.destroy()
            self.shownresults = False        
                

    def addNewSection(self):
        '''Addition of a new section when the add section button is hit, makes it so the section appears at the end of the 
        section list and that the weight and name are stored. Also adds a done/edit button'''
        try:
            
            if self.sectionNum != 2:
                float(self.sectionWeightList[-1].get())
                if(not(self.sectionEntryList[-1].get().isalpha())):
                    raise TypeError
                
                
                if (self.editButtonLst[-1].cget('text') != 'Edit'):
                    self.editButtonLst[-1].invoke()

                    if self.sectionEntryList[-1].cget('state') != 'disabled':
                        raise TypeError

                self.assignmentNum +=1
                
                
                
            frame = tk.Frame(self.rootFrame)
            frame.grid(row=self.sectionNum,column=0, columnspan=4, sticky=tk.W)
            frame.columnconfigure(4, minsize=100)

            self.weightLabel = tk.Label(frame, text='Weight:', foreground='white')
            self.weightLabel.grid(row=0, column=2,sticky=tk.E)
            self.sectionLabel = tk.Label(frame, text='Section Name:',foreground='white')
            self.sectionLabel.grid(row=0, column=0,sticky=tk.E)
            self.sectionWeightList.append(tk.Entry(frame))
            self.sectionEntryList.append(tk.Entry(frame)) 
            self.sectionEntryList[-1].grid(row=0, column=1)
            self.sectionWeightList[-1].grid(row=0, column=3)

            self.frameLst.append(frame)
            
            
            #Edit/Done Button
            editButtonPos = len(self.editButtonLst)
            posOfWeightnSection = len(self.sectionWeightList) - 1
            edit = tk.Button(frame, text='Done',command=lambda: self.doneSection(editButtonPos, posOfWeightnSection))
            edit.grid(row=0, column = 4)
            self.editButtonLst.append(edit)



            self.sectionNum +=1
            
            self.updateScroll()
            
        except:
            pass
    
    def doneSection(self, editButtonPos, posOfWeightnSection):
        '''What is done to close a section when the done button is hit, makes sure that every entry is filled out.
        Makes sure the entry fields have the correct information.'''
        try:
            
            tempWeight = float(self.sectionWeightList[posOfWeightnSection].get())
            tempSectionName = self.sectionEntryList[posOfWeightnSection].get()
            if(not(tempSectionName.isalpha())):
                raise TypeError
            self.mainClass.makeSection(tempSectionName)
            self.mainClass.setSectionWeight(tempSectionName, tempWeight)
            

            
            lstPos = len(self.assignmentButtonList)
            if(len(self.sectionEntryList) > len(self.assignmentButtonList)):
                self.assignmentButtonList.append(tk.Button(self.rootFrame, text='Add assignment', command = lambda: self.addAssignments(lstPos)))
                self.assignmentButtonList[-1].grid(row=self.assignmentNum, column=2)
                self.assignmentLst.append([])
                self.assignmentNum +=1
                self.sectionNum += 1
            self.sectionEntryList[posOfWeightnSection].configure(state='disabled')
            self.sectionWeightList[posOfWeightnSection].configure(state='disabled')
            self.editButtonLst[editButtonPos].configure(text='Edit',command= lambda: self.editSection(False, editButtonPos,posOfWeightnSection, tempSectionName))
            
            self.updateScroll()
        except:
            pass
   
        
    
    def editSection(self, isDone, posOfWeightnSection, editButtonPos, oldName):
        '''What is done when someone hits edit section. Controls the editing/done aspect of a button'''
        try:
            if isDone:
                
                tempWeight = float(self.sectionWeightList[posOfWeightnSection].get())
                tempSectionName = self.sectionEntryList[posOfWeightnSection].get()
                if(not(tempSectionName.isalpha())):
                    raise TypeError
                if oldName != tempSectionName:
                    self.mainClass.renameSection(oldName, tempSectionName)
                self.mainClass.setSectionWeight(tempSectionName, tempWeight)
                
                self.sectionEntryList[posOfWeightnSection].configure(state='disabled')
                self.sectionWeightList[posOfWeightnSection].configure(state='disabled')
                self.editButtonLst[editButtonPos].configure(text='Edit',command= lambda: self.editSection(False, editButtonPos,posOfWeightnSection, tempSectionName))
                
            else:
                self.sectionEntryList[posOfWeightnSection].configure(state='normal')
                self.sectionWeightList[posOfWeightnSection].configure(state='normal')
                self.editButtonLst[editButtonPos].configure(text='Done',command= lambda: self.editSection(True, editButtonPos,posOfWeightnSection, oldName))
        except:
            pass
    

    def addAssignments(self, lstPos):
        '''What is done when an assignment is added to a section. Makes sure to keep track of what section it belongs to. Very similar to addSection'''
        try:

            buttonInfo = self.assignmentButtonList[lstPos].grid_info()
            buttonRow = buttonInfo['row']
            
            if(len(self.frameLst) > 1):
                if self.frameLst[buttonRow - 3 - lstPos].grid_info()['column'] == 1:
                    
                    assert float(self.assignmentLst[lstPos][-1][1].get())
                    assert float(self.assignmentLst[lstPos][-1][2].get())
                    tempName = self.assignmentLst[lstPos][-1][0].get()
                    if(not(tempName.isalpha())):
                        raise ValueError
                    
                    if(self.editButtonLst[buttonRow - 4 - lstPos].cget('text') != 'Edit'):
                        self.editButtonLst[buttonRow - 4 - lstPos].invoke()
                        if self.assignmentLst[lstPos][-1][1].cget('state') != 'disabled':
                            raise TypeError
                    
                    
                    



            
            frame = tk.Frame(self.rootFrame)
            frame.grid(row=buttonRow, column=1, columnspan=5,sticky=tk.W)

            frame.columnconfigure(4, minsize=100 )
            assignNameLabel = tk.Label(frame, text='Name of Assignment', foreground='white')
            assignName = tk.Entry(frame)

            numerLabel = tk.Label(frame, text='Your Score:', foreground='white')
            numer = tk.Entry(frame)

            denomLabel = tk.Label(frame, text='Total Score:', foreground='white')
            denom = tk.Entry(frame)
            assignNameLabel.grid(row=0, column=0)
            assignName.grid(row=0, column=1)
            numerLabel.grid(row=0, column=2)
            numer.grid(row=0, column=3)
            denomLabel.grid(row=0, column=4)
            denom.grid(row=0, column=5)
            self.assignmentLst[lstPos].append((assignName, numer, denom))
            self.frameLst.insert(buttonRow-2 - lstPos, frame)

            #Edit/Done button
            numOfAssignments = len(self.assignmentLst[lstPos]) - 1
            editLstPos = buttonRow - 3 - lstPos
            edit = tk.Button(frame, text = 'Done',command= lambda: self.doneAssignment(editLstPos, lstPos, numOfAssignments))
            edit.grid(row=0, column=7)
            self.editButtonLst.insert(buttonRow - 3 - lstPos, edit)
            
            
            
            
            
            for x in range(buttonRow - 1 - lstPos, len(self.frameLst)):
                rowTemp = self.frameLst[x].grid_info()['row']
                self.frameLst[x].grid(row= rowTemp + 1)
                
            for x in range(lstPos, len(self.assignmentButtonList)):
                
                rowTemp = self.assignmentButtonList[x].grid_info()['row']
                self.assignmentButtonList[x].grid(row=rowTemp+1)
            
            self.sectionNum +=1 
            self.assignmentNum +=1
            self.updateScroll()
            
        except:
            pass
        
        
                


        
         
    def doneAssignment(self, editLstPos, lstPos, numOfAssignment):
        '''What is done when someone clicks done on an assignment'''
        try:
            tempNumer = float(self.assignmentLst[lstPos][numOfAssignment][1].get())
            tempDenom = float(self.assignmentLst[lstPos][numOfAssignment][2].get())
            tempName = self.assignmentLst[lstPos][numOfAssignment][0].get()
            
            if(not(tempName.isalpha())):
                raise ValueError
            
            self.mainClass.setNewAssignment(self.sectionEntryList[lstPos].get(), tempName, tempNumer, tempDenom)
            self.assignmentLst[lstPos][numOfAssignment][0].configure(state = 'disabled')
            self.assignmentLst[lstPos][numOfAssignment][1].configure(state = 'disabled')
            self.assignmentLst[lstPos][numOfAssignment][2].configure(state = 'disabled')
            self.editButtonLst[editLstPos].configure(text='Edit', command= lambda: self.editAssignment(False, editLstPos, lstPos, numOfAssignment, tempName))
          
        except:
            pass
        
    def editAssignment(self, isDone, editLstPos,lstPos, numOfAssignment, oldName):
        '''allows the user to edit an assignment when they click the edit/done button'''
        try:
            if isDone:
                tempNumer = float(self.assignmentLst[lstPos][numOfAssignment][1].get())
                tempDenom = float(self.assignmentLst[lstPos][numOfAssignment][2].get())
                tempName = self.assignmentLst[lstPos][numOfAssignment][0].get()
                
                if(not(tempName.isalpha())):
                    raise ValueError
                if(oldName != tempName):
                    self.mainClass.renameAssignment(self.sectionEntryList[lstPos].get(), tempName, oldName)
                self.mainClass.redoAssignment(self.sectionEntryList[lstPos].get(), tempName, tempNumer, tempDenom)
                self.assignmentLst[lstPos][numOfAssignment][0].configure(state = 'disabled')
                self.assignmentLst[lstPos][numOfAssignment][1].configure(state = 'disabled')
                self.assignmentLst[lstPos][numOfAssignment][2].configure(state = 'disabled')
                self.editButtonLst[editLstPos].configure(text='Edit', command= lambda: self.editAssignment(False, editLstPos, lstPos, numOfAssignment, tempName))
            else:
                self.assignmentLst[lstPos][numOfAssignment][0].configure(state = 'normal')
                self.assignmentLst[lstPos][numOfAssignment][1].configure(state = 'normal')
                self.assignmentLst[lstPos][numOfAssignment][2].configure(state = 'normal')
                self.editButtonLst[editLstPos].configure(text='Done', command= lambda: self.editAssignment(True,editLstPos, lstPos, numOfAssignment, oldName))
        except:
            pass

        

    def lockname(self):
        '''Locks the class name and initilizes the add section button'''
        if self.classN.get().isalnum():
            self.classEntry.config(state= 'disabled')
            self.submitButton.config(state= 'disabled')
            self.submitButton.destroy
            self.mainClass = classes(self.classN.get())
            self.addButton = tk.Button(self.rootFrame, text='Add section',command=self.addNewSection)
            self.addButton.grid(row = 100, column=3)
            

            
if __name__ == '__main__':
    gradeCalc = GradeCalcUI()
    gradeCalc.root.mainloop()