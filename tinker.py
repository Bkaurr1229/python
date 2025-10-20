from tkinter import *


def button_clicked():
    n = entry.get()
    kilometer = round(float(n) * 1.609)
    my_label2.config(text=kilometer)


window = Tk()
window.title("Converter Miles to Km")
window.minsize(width=500, height=300)

entry = Entry(width=10)
entry.grid(column=2, row=0)

my_label = Label(text=" Miles")
my_label.grid(column=3, row=0)

my_label1 = Label(text=" is equal to")
my_label1.grid(column=1, row=1)

my_label2 = Label(text=" 0 ")
my_label2.grid(column=2, row=1)

my_label4 = Label(text=" Km")
my_label4.grid(column=3, row=1)

# button
button = Button(text="calculate", command=button_clicked)
button.grid(column=2, row=2)
window.mainloop()
