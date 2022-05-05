#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x500")
e_text=""
def get_value():
   fitness=float(entry.get())
   sleep=float(entry1.get())
   social=float(entry2.get())
   tv=float(entry3.get())
   
   if (fitness>=0 and fitness<=1) and (sleep>=7 and sleep<=9) and (social<=2.36) and (tv>=0 and tv<=2):
       e_text="Mental Health Condition is Good" 

   else:
      e_text="Mental Health Condition is Bad" 
      
      
      
   Label(win, text=e_text, font= ('Century 15 bold')).place(x=350,y=450)


def Reset():
    Label(win, text="", font= ('Century 15 bold')).place(x=350,y=450)    

def Reload():
    entry.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    Reset()
#Create an Entry Widget




Label(win,text="Check Your Mental Health", font="arial 25").pack(pady=50)

Label(text="Time Spent on Fitness(in hour)",font=23).place(x=220,y=150)

entry= ttk.Entry(win,font=('Century 12'),width=40)
entry.pack(pady= 30)
entry.place(x=220,y=180)


Label(text="Time Spent on Sleep(in hour)",font=23).place(x=220,y=220)

entry1= ttk.Entry(win,font=('Century 12'),width=40)
entry1.pack(pady= 30)
entry1.place(x=220,y=250)

Label(text="Time Spent on Social Media(in hour)",font=23).place(x=220,y=290)

entry2= ttk.Entry(win,font=('Century 12'),width=40)
entry2.pack(pady= 30)
entry2.place(x=220,y=320)


Label(text="Time Spent on TV(in hour)",font=23).place(x=220,y=360)

entry3= ttk.Entry(win,font=('Century 12'),width=40)
entry3.pack(pady= 30)
entry3.place(x=220,y=390)


#Create a button to display the text of entry widget
button= ttk.Button(win, text="Check", command= get_value)
button.pack()
button.place(x=220,y=420);

button2= ttk.Button(win, text="Check Again", command= Reload)
button2.pack()
button2.place(x=300,y=420);
win.mainloop()