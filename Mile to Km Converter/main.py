from tkinter import *

solution = 0


def calculator():
    global solution
    km_1 = 1.609
    mile = float(text_field.get())
    solution = round(km_1*mile, 2)
    answer.config(text=f"{solution}")
    

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=500, width=600)

text_field = Entry(width=15)
text_field.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)


answer = Label(text=f"{solution}")
answer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)

window.mainloop()
