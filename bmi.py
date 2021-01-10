from tkinter import *

master = Tk()

# configuring the main window
# master.configure(bg="#5d5d81")
bg = PhotoImage(file = "D:\Python Projects\\assets\\bmifitness4.png")
label1 = Label(master, image=bg)
label1.place(x=-2.5, y=-2.5)
# canvas = Canvas(master, width=550, height=900)
# canvas.pack(fill="both", expand=True)
# canvas.create_image(0, 0, image=bg, anchor="nw")
master.geometry("900x550")  # syntax:- width x height // this will set default width and height
master.minsize(900, 550)
master.maxsize(900, 550)
master.title("Body Mass Index Calculator")

# main frame inside the main window
f1 = Frame(master, bg="#191919", borderwidth=10, relief=FLAT)  # FLAT, GROOVE, RAISED, RIDGE, SOLID, SUNKEN
f1.pack(side=TOP, fill=X, pady=70, padx=70)

# heading
heading = Label(f1, text="Body Mass Index", fg="#fefcfd", font="montserrat 30 bold", bg="#191919")  # 3b3355
heading.pack(side=TOP, fill=X, padx=40, pady=40)

# frame 2 inside frame 1 (main frame)
f2 = Frame(f1, bg="#191919") #3b3355
f2.pack(side=TOP, fill=X, padx=40)

# frame 3 inside frame 2
f3 = Frame(f2, bg="#191919") #3b3355
f3.pack(side=LEFT, fill=Y, padx=20)

# frame 4 inside frame 2
f4 = Frame(f2, bg="#191919") #3b3355
f4.pack(side=RIGHT, fill=Y, padx=20)
# frame 3 and frame 4 are parallel inside frame 2

# input label of entering height
height = Label(f3, text="Enter the height (in cm): -", fg="#feffff", font="montserrat 15", bg="#191919") #3b3355
height.pack(side=TOP, padx=40, pady=13, anchor=NW)

# input label of entering weight
weight = Label(f3, text="Enter the weight (in kg): -", fg="#feffff", font="montserrat 15", bg="#191919")
weight.pack(side=TOP, padx=40, pady=19, anchor=NW)

# input area of entering height
height_entry = Entry(f4, bg="#feffff", textvariable=StringVar(), fg="black", font="montserrat 13 bold", width=40)
height_entry.pack(side=TOP, anchor=NE, ipady=7, pady=10)

# input area of entering weight
weight_entry = Entry(f4, bg="#feffff", textvariable=StringVar(), fg="black", font="montserrat 13 bold", width=40) #bfcde0
weight_entry.pack(side=TOP, anchor=SE, ipady=7, pady=10)

# declaring a variable that will be needed.
bmi = StringVar()


def getvals():  # defining a function to calculate bmi
    bmicalc = round(float(weight_entry.get())/(float(height_entry.get())*float(height_entry.get()))*10000, 2)
    if bmicalc < 18.5:
        bmiresult = f"Your BMI is {bmicalc} and \nYou are UNDERWEIGHT."
    elif bmicalc >= 18.5 and bmicalc < 24.9:
        bmiresult = f"Your BMI is {bmicalc} and \nYou are NORMAL."
    elif bmicalc > 24.9:
        bmiresult = f"Your BMI is {bmicalc} and \nYou are OVERWEIGHT."
    bmi.set(bmiresult)


# frame 5 inside frame 3
f5 = Frame(f3, bg="#191919") #3b3355
f5.pack(side=BOTTOM, anchor=S, pady=20, fill=X)

# button to calculate body mass index
btn = Button(f5, text="Calculate BMI", command=getvals, font="montserrat 12 bold", bg="#333333", fg="white", borderwidth=2, relief=FLAT)
btn.pack(side=TOP, anchor=S, pady=20, ipadx=30, ipady=20)

# label for displaying result
anslabel = Label(f4, bg="#191919", fg="white", textvariable=bmi, font="montserrat 13 bold")
anslabel.pack(side=TOP, anchor=S, ipadx=30, ipady=35)

master.mainloop()

