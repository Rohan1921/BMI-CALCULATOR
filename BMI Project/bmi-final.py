from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from time import strftime
import webbrowser
import os

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()


def hyperlink_of_bmi():
    webbrowser.open_new_tab("https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html")

def after_login():
  screen2.destroy()
  screen6 = Toplevel(screen)

  menubar = Menu(screen6) 
  file = Menu(menubar, tearoff = 0) 
  menubar.add_cascade(label ='File', menu = file) 
  file.add_command(label ='New Entry', command = None) 
  file.add_command(label ='Personal Statistics', command = None) 
  file.add_command(label ='Saved Data', command = None) 
  file.add_separator() 
  file.add_command(label ='Exit', command = screen6.destroy) 
  
  # Adding Edit Menu and commands 
  edit = Menu(menubar, tearoff = 0) 
  menubar.add_cascade(label ='Info', menu = edit) 
  edit.add_command(label ='Thin Body', command = None) 
  edit.add_command(label ='Fat Body', command = None) 
  edit.add_command(label ='Maintenance', command = None) 
  edit.add_command(label ='Food & Supplements', command = None) 
  edit.add_separator() 
  edit.add_command(label ='Find!', command = None) 
  edit.add_command(label ='Search Online', command = hyperlink_of_bmi) 
  
  # Adding Help Menu 
  help_ = Menu(menubar, tearoff = 0) 
  menubar.add_cascade(label ='Help Desk', menu = help_) 
  help_.add_command(label ='Diet', command = None) 
  help_.add_command(label ='Demonstration', command = None) 
  help_.add_separator() 
  help_.add_command(label ='About BMI', command = hyperlink_of_bmi) 
  
  # display Menu 
  screen6.config(menu = menubar) 
  screen6.geometry("900x550")  # syntax:- width x height // this will set default width and height
  screen6.minsize(900, 550)
  screen6.maxsize(900, 550)
  screen6.configure(bg="#a8a8a8")
  screen6.title("Body Mass Index Calculator")

  # main frame inside the main window
  f1 = Frame(screen6, bg="#191919", borderwidth=10, relief=FLAT)  # FLAT, GROOVE, RAISED, RIDGE, SOLID, SUNKEN
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

  
  btn = Button(f5, text="Calculate BMI", command=getvals, font="montserrat 12 bold", bg="#333333", fg="white", borderwidth=2, relief=FLAT)
  btn.pack(side=TOP, anchor=S, pady=20, ipadx=30, ipady=20)

  
  anslabel = Label(f4, bg="#191919", fg="white", textvariable=bmi, font="montserrat 13 bold")
  anslabel.pack(side=TOP, anchor=S, ipadx=30, ipady=35)

def password_not_recognised():
  message = messagebox.showerror("Error", "Incorrect Password!")
  screen2.destroy()
  login()

def user_not_found():
  message = messagebox.showerror("Error", "Incorrect Username!")
  screen2.destroy()
  login()

  
def register_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()
  file = askopenfile(mode='a', filetypes=[('Text Files', '*.txt')])
  file.write("\n"+username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

  messagebox.showinfo('Registered', message="Your registration was successful.")
  screen1.destroy()

def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  
  file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
  verifypwd = file.read().splitlines()
  if username1 in verifypwd:
    if password1 in verifypwd:
      after_login()
      file.close()
    else:
      password_not_recognised()
      file.close()
  else:
    user_not_found()
    file.close()

  
  


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("900x550")
  screen1.minsize(900, 550)
  screen1.maxsize(900, 550)
  screen1.configure(bg="#191919")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter your details", font="montserrat 20 bold", bg="#191919", fg="#fefcfd").pack(pady=30)
  
  Label(screen1, text = "Username * ", font="montserrat 15", fg="#fefcfd", bg="#191919").pack(pady=10)
  
 
  username_entry = Entry(screen1, textvariable = username, width=30, font="montserrat 13")
  username_entry.pack(pady=5, ipadx=10, ipady=5)
  Label(screen1, text = "Password * ", font="montserrat 15", fg="#fefcfd", bg="#191919").pack(pady=10)
  password_entry =  Entry(screen1, textvariable = password, width=30, font="montserrat 13", show="*")
  password_entry.pack(pady=5, ipadx=10, ipady=5)
  Label(screen1, text="Show password", font="montserrat 11", fg="#fefcfd", bg="#191919").pack(padx=40)
  var = IntVar()

  def showhidepwd():
    if var.get() == 1:
      password_entry.configure(show="")
    elif var.get() == 0:
      password_entry.configure(show="*")

  

  checkbtn = Checkbutton(screen1, command=showhidepwd, offvalue=0, onvalue=1, variable=var, bg="#191919")
  checkbtn.place(x=515, y=306)
  
  Button(screen1, text = "Register", width = "25", height = "2", bg="#333333", font="montserrat 14", fg="#fefcfd", borderwidth=2, relief=FLAT, command = register_user).pack(pady=30)

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("900x550")
  screen2.minsize(900, 550)
  screen2.maxsize(900, 550)
  screen2.configure(bg="#191919")
  
  Label(screen2, text = "Please enter your details", font="montserrat 20 bold", bg="#191919", fg="#fefcfd").pack(pady=30)
  

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1

  
  
  Label(screen2, text = "Username * ", font="montserrat 15", fg="#fefcfd", bg="#191919").pack(pady=10)
  username_entry1 = Entry(screen2, textvariable = username_verify, width=30, font="montserrat 13")
  username_entry1.pack(pady=5, ipadx=10, ipady=5)
  
  
  Label(screen2, text = "Password * ", font="montserrat 15", fg="#fefcfd", bg="#191919").pack(pady=10)
  password_entry1 = Entry(screen2, textvariable = password_verify, width=30, font="montserrat 13", show="*")
  password_entry1.pack(pady=5, ipadx=10, ipady=5)
  Label(screen2, text="Show password", font="montserrat 11", fg="#fefcfd", bg="#191919").pack(padx=40)
  var = IntVar()

  def showhidepwd():
    if var.get() == 1:
      password_entry1.configure(show="")
    elif var.get() == 0:
      password_entry1.configure(show="*")
  

  checkbtn = Checkbutton(screen2, command=showhidepwd, offvalue=0, onvalue=1, variable=var, bg="#191919")
  checkbtn.place(x=515, y=306)
  
  Button(screen2, text = "Login", width = "25", height = "2", bg="#333333", font="montserrat 14", fg="#fefcfd", borderwidth=2, relief=FLAT, command = login_verify).pack(pady=30)
  
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("900x550")
  screen.minsize(900, 550)
  screen.maxsize(900, 550)
  screen.configure(bg="#191919")
  screen.title("BMI Calculator | Login/Sign-up")
  heading = Label(screen, text="Body Mass Index Calculator", fg="#fefcfd", font="montserrat 30 bold", bg="#191919")  # 3b3355
  heading.pack(side=TOP, fill=X, pady=30)
  login_label = Label(screen, text = "Login / Register to continue..", font = "montserrat 20", fg="#fefcfd", bg="#191919")
  login_label.pack(side=TOP, fill=X, pady=40)
  # Label(text = "").pack()
  login_btn = Button(text = "Login", height = "2", width = "25", font="montserrat 13", fg="#fefcfd", bg="#333333", borderwidth=2, relief=FLAT, command = login)
  login_btn.pack(pady=10)
  # Label(text = "").pack()
  reg_btn = Button(text = "Register",height = "2", width = "25", font="montserrat 13", fg="#fefcfd", bg="#333333", borderwidth=2, relief=FLAT, command = register)
  reg_btn.pack(pady=15)

  screen.mainloop()

main_screen()
  
