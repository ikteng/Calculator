# pip install tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
 
window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="#C6DEF1", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=5, ipady=2, pady=2)
 
 
def myclick(number):
    entry.insert(tk.END, number) # when click on button, insert number to entry
 
 
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error") # if entry is empty, error message
 
 
def clear():
    entry.delete(0, tk.END) # clear the entry

# buttons functions
# number 1 button
button_1 = tk.Button(master=frame, text='1', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(1))
button_1.grid(row=3, column=0, pady=2)

# number 2 button
button_2 = tk.Button(master=frame, text='2', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(2))
button_2.grid(row=3, column=1, pady=2)

# number 3 button
button_3 = tk.Button(master=frame, text='3', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(3))
button_3.grid(row=3, column=2, pady=2)

# number 4 button
button_4 = tk.Button(master=frame, text='4', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)

# number 5 button
button_5 = tk.Button(master=frame, text='5', 
                     padx=15, pady=5, width=2, 
                     command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)

# number 6 button
button_6 = tk.Button(master=frame, text='6', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)

# number 7 button
button_7 = tk.Button(master=frame, text='7', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(7))
button_7.grid(row=1, column=0, pady=2)

# number 8 button
button_8 = tk.Button(master=frame, text='8', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(8))
button_8.grid(row=1, column=1, pady=2)

# number 9 button
button_9 = tk.Button(master=frame, text='9', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(9))
button_9.grid(row=1, column=2, pady=2)

# number 0 button
button_0 = tk.Button(master=frame, text='0', 
                     padx=15,pady=5, width=2, 
                     command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

# clear button
button_clear = tk.Button(master=frame, text="clear",
                        padx=15, pady=5, width=2, 
                        command=clear)
button_clear.grid(row=4, column=0, pady=2)
 
# equal button
button_equal = tk.Button(master=frame, text="=", 
                        padx=15,pady=5, width=2, 
                        command=equal)
button_equal.grid(row=4, column=2, pady=2)

# arithmetic operation
# add button 
button_add = tk.Button(master=frame, text="+", 
                       padx=15,pady=5, width=2, 
                       command=lambda: myclick('+'))
button_add.grid(row=1, column=3, pady=2)
 
# subtract button
button_subtract = tk.Button(master=frame, text="-", 
                            padx=15, pady=5, width=2, 
                            command=lambda: myclick('-'))
button_subtract.grid(row=2, column=3, pady=2)
 
# multiply button
button_multiply = tk.Button(master=frame, text="*", 
                            padx=15, pady=5, width=2, 
                            command=lambda: myclick('*'))
button_multiply.grid(row=3, column=3, pady=2)

# division button
button_div = tk.Button(master=frame, text="/", 
                       padx=15,pady=5, width=2, 
                       command=lambda: myclick('/'))
button_div.grid(row=4, column=3, pady=2)
 
window.mainloop()