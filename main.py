from tkinter import *
import calendar
from time import strftime

def write():
    textarea.config(state=NORMAL)

def delete():
    textarea.delete("1.0", "end")

def save():
    text = textarea.get("1.0", "end")
    with open("not_defteri.txt", "w") as file:
        file.write(text)

def month_calendar():
    month = int(monthspinBox.get())
    year = int(yearspinBox.get())
    data = calendar.month(year, month)
    textfield.insert(INSERT, data)

root = Tk()
root.geometry('1279x939+200+10')
root.title('Not Defteri')
#root.resizable(False, False)
root.config(bg='red4')

my_label_frame = LabelFrame(root, text="Not Defteri", font=('arial', 20, 'bold'), bg='brown3', fg='white')
my_label_frame.pack(pady=10, padx=10)

my_frame = Frame(my_label_frame)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

textarea = Text(my_frame, yscrollcommand=text_scroll.set, wrap='word', font=("Helvetica", 20), height=17.2,
                bg='red4', fg='white', state=DISABLED)
textarea.pack()

buttonFrame = Frame(my_label_frame, bg='brown3')
buttonFrame.pack()

write_button = Button(buttonFrame, text="Yaz", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',
                      command=write)
write_button.grid(row=0, column=0, padx=20)

delete_button = Button(buttonFrame, text="Sil", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',
                       command=delete)
delete_button.grid(row=0, column=1, padx=20)

save_button = Button(buttonFrame, text="Kaydet", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',
                     command=save)
save_button.grid(row=0, column=2, padx=20)

clock_frame = Frame(my_label_frame, bg='brown3')
clock_frame.pack(pady=5)

clock_label = Label(clock_frame, font=('ds-digital', 20), bg='brown3', fg='white')
clock_label.pack(pady=10, padx=10)

def timer():
    string = strftime('%H:%M:%S %p')
    clock_label.config(text=string)
    clock_label.after(1000, timer)

timer()

# Calendar Section
#calendar_label = Label(root, text='', font=('arial', 12, 'bold'), bg='yellow')
#calendar_label.pack()

#month_label = Label(root, text='', font=('arial', 12, 'bold'), bg='yellow')
#month_label.pack()

#year_label = Label(root, text='', font=('arial', 12, 'bold'), bg='yellow')
#year_label.pack()
calendar_frame = Frame(my_label_frame, bg='brown3')
calendar_frame.pack(pady=10, padx=10)

monthspinBox = Spinbox(calendar_frame, from_=1, to=12, width=8, font=('arial', 10, 'bold'), bg='brown3', fg='white')
monthspinBox.pack(side=LEFT, fill=X,)

yearspinBox = Spinbox(calendar_frame, from_=1996, to=2500, width=8, font=('arial', 10, 'bold'),bg='brown3', fg='white')
yearspinBox.pack(side=LEFT, fill=X,)

goButton = Button(calendar_frame, text='Go', font=('arial', 12, 'bold'), bg='brown3', fg='white', command=month_calendar)
goButton.pack(side=LEFT, fill=X,)

textfield = Text(calendar_frame, width=24, height=8, fg='red')
textfield.pack(side=LEFT, fill=X,)

root.mainloop()

