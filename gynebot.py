# Python program to create a simple GUI


#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json

# Create a GUI Window
root = Tk()
file = open("res.txt", "w+")

# set the size of the GUI Window
root.geometry("800x800")


# set the title of the Window
root.title("GYNE BOT")
container = Frame(width=800, height=800)
container.pack()
canvas = Canvas(container)
scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

container.pack()
canvas.pack(side="left", fill="both", expand=True )
scrollbar.pack(side='right', fill='y')             
gui = scrollable_frame

# get the data from the json file
with open('data.json') as f:
	data = json.load(f)

print(data['question'][0])

wait = False

def printAnswer(gui, m, index,buttons):
        ans = Label(gui, text=m,background="white", foreground="black",font=("Arial", 12),anchor="e")
        ans.pack(side=RIGHT)

        for i in buttons:
                i["state"] = DISABLED

        makeQuestion(gui, index + 1)
        toWrite = f"{question[index]}  {m}\n"
        file.write(toWrite)
        canvas.update_idletasks()
        canvas.yview_moveto(1)

        

def makeQuestion(gui, index):
        buttons = []
        print(index)
        print(len(question))
        if(index >= len(question)):
                print(index)
                root.destroy()
                return 
        ques = Label(gui, text=data['question'][index],background="dodger blue", foreground="white",font=("Arial", 13),anchor="w")
        
        
        
        for i in data['options'][index]:
                buttons.append(Button(gui, text=i, command=lambda m = i: printAnswer(gui, m, index, buttons)))

        ques.pack()
        for i in buttons:
                i.pack()

# set the question, options, and answer
question = (data['question'])
options = (data['options'])

makeQuestion(gui, 0)






# create an object of the Quiz Class.
root.mainloop()
file.close()
#quiz = Quiz()
# Start the GUI

# END OF THE PROGRAM


