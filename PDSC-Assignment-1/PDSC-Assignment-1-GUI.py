#This is the same program of day 1 assignment, just added with tkinter GUI.
from tkinter import *
root = Tk()
root.title("PDSC Assignment One")
root.geometry("550x450")
root.iconbitmap('Brand-Logo-Icon.ico')
root.resizable(False, False)
root.configure(bg='lemon chiffon')
input_label = Label(root, text="Enter your Mark:", font=("Times", "20", "underline"), background="lemon chiffon")
input_label.pack()
input_label.place(x=0, y=10)
input_entry = Entry(root, font=("Times", "20", "italic"))
input_entry.pack()
input_entry.place(x=250, y=10)
result = Label(root, text="", font=("Times", "20", "italic"), background="lemon chiffon")
result.pack()
result.place(x=5, y=50)
def checkResult():
    a = input_entry.get()
    x = int(a)
    if x <= 100:
        if x < 32 and x > 0:
            result.configure(text="Oops!! We're sorry to say that you failed.")
        elif x == 32:
            result.configure(text="You're just pass !")
        elif x > 32 and x <= 60:
            result.configure(text="Congrats, You're pass!!")
        elif x > 60 and x <=100:
            result.configure(text="Wow, You're excellent !!!")
        else:
            result.configure(text="The mark is not valid !")
    else:
        result.configure(text="Your mark cannot be more than 100.")
submit_button = Button(root, text="Submit Mark", fg='white', bg='red', font=("Helvetica", "11", "italic"), bd='3', command=checkResult)
submit_button.pack()
submit_button.place(x=50, y=100)
root.mainloop()
