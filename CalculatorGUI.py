#!/usr/bin/python
''' Simple Calculator with the Tkinter GUI'''
'''Project by KiliBio'''


from tkinter import *
import tkinter.messagebox

class Calculator:

    def __init__(self, master):
        master.title("Kili's Calculator")
        frame = Frame(master, cursor="tcross", height=1000, width=1000)
        frame.pack(fill=BOTH)
        '''
        All the buttons
        '''
        self.button1 = Button(frame, text="   1   ", bg="lightgrey", activebackground="green4", command=self.button1operation).grid(row=0, column=0, sticky=W, ipadx=5, ipady=5, padx=2, pady=2)
        self.button2 = Button(frame, text="   2   ", bg="lightgrey", activebackground="green4", command=self.button2operation).grid(row=0, column=1, ipadx=5, ipady=5, padx=2, pady=2)
        self.button3 = Button(frame, text="   3   ", bg="lightgrey", activebackground="green4", command=self.button3operation).grid(row=0, column=2, sticky=E, ipadx=5, ipady=5, padx=2, pady=2)
        self.buttonplus = Button(frame, text="   +   ", bg="grey", activebackground="mediumpurple3",command=self.buttonplusoperation).grid(row=0, column=3, sticky=E, ipadx=5, ipady=5, padx=2, pady=2)
        self.button4 = Button(frame, text="   4   ", bg="lightgrey", activebackground="green4", command=self.button4operation).grid(row=1, column=0, sticky=W, ipadx=5, ipady=5, padx=2, pady=2)
        self.button5 = Button(frame, text="   5   ", bg="lightgrey", activebackground="green4", command=self.button5operation).grid(row=1, column=1, ipadx=5, ipady=5, padx=2, pady=2)
        self.button6 = Button(frame, text="   6   ", bg="lightgrey", activebackground="green4", command=self.button6operation).grid(row=1, column=2, sticky=E, ipadx=5, ipady=5, padx=2, pady=2)
        self.buttonminus = Button(frame, text="   -    ", bg="grey", activebackground="mediumpurple3",command=self.buttonminusoperation).grid(row=1, column=3, sticky=E, ipadx=5, ipady=5, padx=2, pady=2)
        self.button7 = Button(frame, text="   7   ", bg="lightgrey", activebackground="green4", command=self.button7operation).grid(row=2, column=0, sticky=W, ipadx=5, ipady=5, padx=2, pady=2)
        self.button8 = Button(frame, text="   8   ", bg="lightgrey", activebackground="green4", command=self.button8operation).grid(row=2, column=1, ipadx=5, ipady=5, padx=2, pady=2)
        self.button9 = Button(frame, text="   9   ", bg="lightgrey", activebackground="green4", command=self.button9operation).grid(row=2, column=2, sticky=E, ipadx=5, ipady=5, padx=2, pady=2)
        self.buttontimes = Button(frame, text="   x    ", bg="grey", activebackground="mediumpurple3", command=self.buttontimesoperation).grid(row=2, column=3, sticky=E, ipadx=5, ipady=5, padx=2, pady=2)
        self.button0 = Button(frame, text="   0   ", bg="lightgrey", activebackground="green4", command=self.button0operation).grid(row=3, column=1, ipadx=5, ipady=5, padx=2, pady=2)
        self.buttondivide = Button(frame, text="   /    ", bg="grey", activebackground="mediumpurple3",command=self.buttondivideoperation).grid(row=3, column=3, sticky=E, ipadx=5, ipady=5, padx=2,pady=2)
        self.buttonEnter = Button(frame, text="                       Enter                       ", bg="orange red",activebackground="red3", command=self.enteroperation).grid(row=4, columnspan=4, ipadx=5, ipady=5,padx=2, pady=2)

        '''
        Entry Field and Lowerspace
        '''

        self.entry = Entry(master)
        self.entry.bind("<Return>", self.evaluate)  # .bind, bind the return statement to a certain object
        self.entry.pack()

        self.lowerspace = Label(master, height=2)
        self.lowerspace.pack()

        lastFrame = Frame(master)
        lastFrame.pack(fill=BOTH)

        self.Exitbutton = Button(lastFrame, takefocus=500, text="                          Exit                         ", bg="red2",activebackground="firebrick4", command=frame.quit)
        self.Exitbutton.pack()

    '''
    Button Functions and Operations
    '''
    operations = []

    def button1operation(self):
        self.operations.append('1')
        return

    def button2operation(self):
        self.operations.append('2')
        return

    def button3operation(self):
        self.operations.append('3')
        return

    def button4operation(self):
        self.operations.append('4')
        return

    def button5operation(self):
        self.operations.append('5')
        return

    def button6operation(self):
        self.operations.append('6')
        return

    def button7operation(self):
        self.operations.append('7')
        return

    def button8operation(self):
        self.operations.append('8')
        return

    def button9operation(self):
        self.operations.append('9')
        return

    def button0operation(self):
        self.operations.append('0')
        return

    def buttonplusoperation(self):
        self.operations.append(' +')
        return

    def buttonminusoperation(self):
        self.operations.append(' -')
        return

    def buttontimesoperation(self):
        self.operations.append(' * ')
        return

    def buttondivideoperation(self):
        self.operations.append(' / ')
        return

    def enteroperation(self):
        print(self.operations)
        self.letsmath(self.operations)

    def letsmath(self,inputlist):
        '''Transforms the list generated by the button entry into a list which can be used to calculate 
        than takes in a transformed list, which can be used to calculate all operations'''
        string = ''.join(inputlist)
        lnandope = string.split()  # lnandope contains sorely large numbers and the operations * and /
        worklist = lnandope.copy()  # creates a copy of the list to work with
        print(worklist)
        final = 0  # is needed to calculate the final result
        whileFlag = 0  # to regulate the number of loops of the while loop to 80
        while whileFlag < 80:  # that's not really pretty, but I couldn't think of a better way to end the loop after
            # all the multiplications and divisions were done and the list was updated
            for element in worklist:
                try:  # identifies all number
                    int(element)
                    whileFlag += 1
                except:  # identifies all * or / operation
                    # print(worklist[worklist.index(element) - 1], worklist.index(element), worklist[worklist.index(element) + 1])
                    '''After identifying the operation, the elements left and right of the operation symbol are 
                    taking to perform the operation. The result is inserted at the end of those three elements
                    (number1, * symbol and number2), and all those three elements are deleted'''
                    if element == '*':
                        result = int(worklist[worklist.index(element) - 1]) * int(worklist[worklist.index(element) + 1])
                        worklist.insert(worklist.index(element) + 2, result)
                        del worklist[worklist.index(element) - 1:worklist.index(element) + 2]
                    else:
                        result = int(worklist[worklist.index(element) - 1]) / int(worklist[worklist.index(element) + 1])
                        worklist.insert(worklist.index(element) + 2, result)
                        del worklist[worklist.index(element) - 1:worklist.index(element) + 2]
                        '''After which all multiplication and divisions are done, all the numbers are added'''
        for numberelement in worklist:
            print(numberelement)
            final = final + float(numberelement)

        print(final)
        return final

    def evaluate(self,event):
        entered = eval(self.entry.get())
        self.lowerspace.configure(text="= " + str(entered))

main = Tk()
calcGUI = Calculator(main)
main.mainloop()
