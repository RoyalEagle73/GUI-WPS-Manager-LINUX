import script
from tkinter import *
home = Tk()

up_frame = Frame(home, bg="black")
up_frame.grid()

req_data = script.script()

bottom_frame = Frame(home)
bottom_frame.grid(row=1)

click_me = Button(up_frame, text="Click to reveal", bg="black", fg="green")

my_canvas = Canvas(bottom_frame)
my_canvas.pack()

text_scroll = Scrollbar(my_canvas)
text_scroll.pack(side=RIGHT, fill=Y)

my_text =Text(my_canvas, yscrollcommand=text_scroll.set)
my_text.pack(side=LEFT, fill=X) 

text_scroll.configure(command=my_text.yview, background="black")

def write(a):
	my_text.delete(1.0, END)
	my_text.insert(END,req_data)

click_me.bind("<Button-1>", write)	
click_me.pack()

home.resizable(0,0) 
home.title("WPS MANAGER (GUI)")
home.mainloop()