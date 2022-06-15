from tkinter import *
import tkinter as tk


BACKGROUND = "#EFFFFD"
BUTTON_COLOR = "#42C2FF"
TIMER = 5
check_time = None

# initialize screen
screen = Tk()
screen.title("Dissapearing Typist")
screen.config(
    bg=BACKGROUND,
    padx=20,
    pady=20
)


# function to get current text lenght
def get_text_lenght():
    global user_text
    length_of_text = len(user_text.get("1.0", tk.END))
    return length_of_text

# start function logic
def start():
    global check_time
    text_lenght = 1
    user_text.delete('1.0', END)
    check_time = screen.after(5000, check_text_lenght, text_lenght)
    

# check for inactivity with 5 seconds intervals
def check_text_lenght(text_lenght):
    global user_text, check_time
    lenght = get_text_lenght()
    if lenght <= text_lenght:
        print(lenght)
        print(text_lenght)
        print("GAME OVER")
        screen.after_cancel(check_time)
        user_text.delete('1.0', END)
        user_text.insert(tk.END, "GAME OVER           5 seconds elapsed without activity          Press Enter to  restart. ")

    else:
        text_lenght = lenght
        check_time = screen.after(5000, check_text_lenght, text_lenght)


    
# user_text widget
user_text = tk.Text(height=30, width=100)
#Puts cursor in textbox.
user_text.focus()
#Adds some text to begin with.
user_text.insert(tk.END, "Press Enter to  start.")
#Get's current value in textbox at line 1, character 0
user_text.grid(column=0, row=1, columnspan=3)

start_button = tk.Button(text="Enter", bg=BUTTON_COLOR, command=start)
start_button.grid(column=2, row=2)






screen.mainloop()