from tkinter import *
import ast

root = Tk()
# root.geometry('200x200')
display = Entry(root)
display.grid(row=1, columnspan=6)
i=0
def get_num(num):
    global i
    display.insert(i,num)
    i+=1

def get_operations(operator):
    global i
    display.insert(i,operator)
    i+=len(operator)

numbers = [1,2,3,4,5,6,7,8,9]
counter = 1
for i in range(3):
    for j in range(3):
        button_text = numbers[counter-1]
        button= Button(root,text=button_text, width=4,height=2, command=lambda text=button_text:get_num(text))
        button.grid(row=i+2, column=j)
        counter+=1
button_zero= Button(root,text='0', width=4, height=2,command=lambda:get_num(0))
button_zero.grid(row=5, column=1)

operations = ['+','-','*','/','//','%','**2','*3.14','(',')','**','.']

count = 0
for x in range(5):
    for y in range(3):
        if count <len(operations):
            button = Button(root,text=operations[count],width=4,height=2,command=lambda text=operations[count]:get_operations(text))
            button.grid(row=x+2,column=y+3)
            count+=1

def clearall():
    display.delete(0,END)

def calculate():
    entire_string = display.get()
    try:
        node = ast.parse(entire_string,mode='eval')
        result = eval(compile(node,'<string>','eval'))
        clearall()
        display.insert(0,result)
    except Exception:
        clearall()
        display.insert(0,'Error')

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clearall()
        display.insert(0,new_string)
    else:
        clearall()
        display.insert(0,'')

button_clear = Button(root, text='clear', width=4,height=2, command=clearall).grid(row=5, column=0)
button_eq = Button(root, text='=',width=4,height=2,command=calculate).grid(row=5,column=2)
button_del_sing = Button(root,text='<-x', width=4, height=2,command=undo).grid(row=6, column=1)


if __name__ == "__main__":
    root.title('mycalc')
    root.mainloop()
    