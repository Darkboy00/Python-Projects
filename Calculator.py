import tkinter as tk

def addition():
    if(num1.get().isdigit() and num2.get().isdigit):
        n1 = float(num1.get())
        n2 = float(num1.get())
        result.configure(text = str(n1+n2))

def extraction():
    if(num1.get().isdigit() and num2.get().isdigit):
        n1 = float(num1.get())
        n2 = float(num1.get())
        result.configure(text = str(n1-n2))

def multiplication():
    if(num1.get().isdigit() and num2.get().isdigit):
        n1 = float(num1.get())
        n2 = float(num1.get())
        result.configure(text = str(n1*n2))

def divison():
    if(num1.get().isdigit() and num2.get().isdigit):
        n1 = float(num1.get())
        n2 = float(num1.get())
        result.configure(text = str(n1/n2))

window = tk.Tk()
window.title("Calculator")
screenwidth = window.winfo_screenwidth() // 2-160
screenheight = window.winfo_screenheight() // 2-150
window.geometry("320x300+{}+{}".format(screenwidth,screenheight))

result = tk.Label(window, text = "Result", font = "Courier 16 bold", width = 30, justify = "center")
result.place(x = -50, y = 20)

num1 = tk.Entry(window, font = "Courier 14 bold", width = 15, justify = "right")
num1.place(x = 70, y = 50)

num2 = tk.Entry(window, font = "Courier 14 bold", width = 15, justify = "right")
num2.place(x = 70, y = 80)

key1 = tk.Button(window, text = "+", font = "Courier 14 bold", width = 10, command = addition)
key1.place(x = 90, y = 110)

key2 = tk.Button(window, text = "-", font = "Courier 14 bold", width = 10, command = extraction)
key2.place(x = 90, y = 150)

key3 = tk.Button(window, text = "*", font = "Courier 14 bold", width = 10, command = multiplication)
key3.place(x = 90, y = 190)

key4 = tk.Button(window, text = "/", font = "Courier 14 bold", width = 10, command = divison)
key4.place(x = 90, y = 230)

num1.focus()

window.mainloop()