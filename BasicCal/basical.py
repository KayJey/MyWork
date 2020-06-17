from tkinter import *
from tkinter import messagebox
#import packages 


window = Tk()
window.geometry("1000x700") 
window.title(" calculator ")
#tkinter window defination and allocating dimensions 
	

aa = IntVar()
bb = IntVar()
#defining the type of the variables

a = Entry(window , relief = "solid" , textvariable= aa).place(x = 200 , y  = 100 )
b = Entry(window , relief = "solid" , textvariable= bb).place(x = 200 , y  = 200 )
#Enrty() is used to get inuput from the user and save the value in the variable called "textvarible"


labell = Label(window,text= "This is a basic Calculator" , relief = "solid"  ,font = ("arial" , 20 , "bold" )).pack()
#This is the heading 

label1 = Label(window , text = "Entre you value here :- " ,font = ( "bold")).place(x = 100 ,y =70)
label2 = Label(window , text = "NUM 1 :- " ,font = ( "bold" , 10 )).place(x = 100 , y= 100)
label3 = Label(window , text = "NUM 2 :- " ,font = ( "bold" , 10 )).place(x = 100 , y= 200) 
#other necesaary labels , with cordinated points

def add():
	aaa = int(aa.get())
	bbb = int (bb.get())
	c = aaa+bbb
	messagebox.showinfo("Result" , c)
	return 

def sub():
	aaa = int(aa.get())
	bbb = int (bb.get())
	c = aaa-bbb
	messagebox.showinfo("Result" , c)
	return
#defination of the funtions add() and sub ()  

buttona =Button(window , text = "ADD" , relief = "groove"  , command = lambda:add())
buttona.place(x = 200 , y  = 300)

buttonb =Button(window , text = "SUB" , relief = "groove" , command = lambda:sub())
buttonb.place(x = 300 , y  = 300) 

Button(window, text="Quit",relief = "groove" , fg = "red" ,command=window.destroy).pack()
# the required buttons 


window.mainloop()
