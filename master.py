from tkinter import*
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def number_Enter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum ==".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True 
        self.current = float(self.current)
        if self.check_sum == True:
            self.solve_Entries()
        else:
            self.total = float(txtDisplay.get())
            
    def solve_Entries(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "subtract":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.solve_Entries()
        elif not self.result:
            self.total = self.current 
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Delete_Entry(self):
        numlen = len(txtDisplay.get())
        txtDisplay.delete(numlen - 1, "end")
        if numlen == 1:
            txtDisplay.insert(0, "0")

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def opPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

        
add_value = Calc()
root = Tk()
root.title("Project Casio")
root.resizable(width = False, height = False)
calc = Frame(root)
calc.grid()

# this represents the button/s in the calculator

txtDisplay = Entry(calc, font=("arial", 18, "bold"), bg="powder blue", bd=30, width = 28, justify = RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, "0")

# ------------------------------ /Row 1/ --------------------------------

btnAllClear = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "AC", bg="orange", command = add_value.All_Clear_Entry).grid(row = 1, column = 0)

btnDelete = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "DEL", bg="orange", command = add_value.Delete_Entry).grid(row = 1, column = 1)

btnSqroot = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "√", command = add_value.squared).grid(row = 1, column = 2)

btnAdd = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "+", command = lambda:add_value.operation("add")).grid(row = 1, column = 3)

# ------------------------------- /Row 2/ --------------------------------

btn7 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "7", bg="powder blue", command = lambda:add_value.number_Enter(7)).grid(row = 2, column = 0)

btn8 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "8", bg="powder blue", command = lambda:add_value.number_Enter(8)).grid(row = 2, column = 1)

btn9 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "9", bg="powder blue", command = lambda:add_value.number_Enter(9)).grid(row = 2, column = 2)

btnSubtract = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "-", command = lambda:add_value.operation("subtract")).grid(row = 2, column = 3)

# ------------------------------- /Row 3/ --------------------------------

btn4 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "4", bg="powder blue", command = lambda:add_value.number_Enter(4)).grid(row = 3, column = 0)

btn5 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "5", bg="powder blue", command = lambda:add_value.number_Enter(5)).grid(row = 3, column = 1)

btn6 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "6", bg="powder blue", command = lambda:add_value.number_Enter(6)).grid(row = 3, column = 2)

btnMultiply = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "x", command = lambda:add_value.operation("multiply")).grid(row = 3, column = 3)

# ------------------------------- /Row 4/ --------------------------------

btn1 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "1", bg="powder blue", command = lambda:add_value.number_Enter(1)).grid(row = 4, column = 0)

btn2 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "2", bg="powder blue", command = lambda:add_value.number_Enter(2)).grid(row = 4, column = 1)

btn3 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "3", bg="powder blue", command = lambda:add_value.number_Enter(3)).grid(row = 4, column = 2)

btnDivide = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "÷", command = lambda:add_value.operation("divide")).grid(row = 4, column = 3)

# ------------------------------- /Row 5/ --------------------------------

btn0 = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "0", bg="powder blue", command = lambda:add_value.number_Enter(0)).grid(row = 5, column = 0)

btnDot = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = ".", command = lambda:add_value.number_Enter(".")).grid(row = 5, column = 1)

btnPM = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "±", command = add_value.opPM).grid(row = 5, column = 2)

btnEquals = Button(calc, pady = 1, bd = 4, fg = "black", font=("arial", 18, "bold"), width = 6, height = 2,
    text = "=", command = add_value.sum_of_total).grid(row = 5, column = 3)


root.mainloop()