from tkinter import *

master = Tk()

master.configure(bg="#5d5d81")
master.geometry("900x550")  # syntax:- width x height // this will set default width and height
master.minsize(900, 550)
master.maxsize(900, 550)
master.title("Body Mass Index Calculator")

# main frame
f1 = Frame(master, bg="#3b3355", borderwidth=10, relief=FLAT)  # FLAT, GROOVE, RAISED, RIDGE, SOLID, SUNKEN
f1.pack(side=TOP, fill=X, pady=70, padx=70)

heading = Label(f1, text="BMI Calculator", fg="#fefcfd", font="montserrat 30 bold", bg="#3b3355")  # 3b3355
heading.pack(side=TOP, fill=X, padx=40, pady=40)

f2 = Frame(f1, bg="#3b3355")
f2.pack(side=TOP, fill=X, padx=40)

f3 = Frame(f2, bg="#3b3355")
f3.pack(side=LEFT, fill=Y, padx=20)

f4 = Frame(f2, bg="#3b3355")
f4.pack(side=RIGHT, fill=Y, padx=20)

height = Label(f3, text="Enter the height (in cm): -", fg="#bfcde0", font="montserrat 15", bg="#3b3355")
height.pack(side=TOP, padx=40, pady=10, anchor=NW)

weight = Label(f3, text="Enter the weight (in kg): -", fg="#bfcde0", font="montserrat 15", bg="#3b3355")
weight.pack(side=TOP, padx=40, pady=10, anchor=NW)

height_entry = Entry(f4, bg="#bfcde0", textvariable=StringVar(), fg="black", width=40)
height_entry.pack(side=TOP, anchor=NE, ipady=7, pady=10)

weight_entry = Entry(f4, bg="#bfcde0", textvariable=StringVar(), fg="black", width=40)
weight_entry.pack(side=TOP, anchor=SE, ipady=7, pady=10)

bmi = StringVar()


def getvals():
    bmicalc = round(float(weight_entry.get())/(float(height_entry.get())*float(height_entry.get()))*10000, 2)
    if bmicalc < 18.5:
        bmiresult = f"Your BMI is {bmicalc} and \nYou are UNDERWEIGHT."
    elif bmicalc >= 18.5 and bmicalc < 24.9:
        bmiresult = f"Your BMI is {bmicalc} and \nYou are NORMAL."
    elif bmicalc > 24.9:
        bmiresult = f"Your BMI is {bmicalc} and \nYou are OVERWEIGHT."
    bmi.set(bmiresult)


f5 = Frame(f3, bg="#3b3355")
f5.pack(side=BOTTOM, anchor=S, pady=20, fill=X)
btn = Button(f5, text="Calculate BMI", command=getvals, font="montserrat 12 bold", bg="#202030", fg="white", borderwidth=2, relief=FLAT)
btn.pack(side=TOP, anchor=S, pady=20, ipadx=30, ipady=10)

anslabel = Label(f4, bg="#3b3355", fg="white", textvariable=bmi, font="montserrat 13 bold")
anslabel.pack(side=TOP, anchor=S, ipadx=30, ipady=34)


master.mainloop()

