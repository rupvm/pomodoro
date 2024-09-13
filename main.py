from tkinter import*
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_clock=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    root.after_cancel(timer_clock)
    l1.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer,text="00:00")
    check_marks.config(text="")
    global reps
    reps=0




# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    reps+=1
    if reps%8==0:
        countdown(LONG_BREAK_MIN*60)
        l1.config(text="Break",fg=RED)
    elif reps%2==0:
        countdown(SHORT_BREAK_MIN*60)
        l1.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN*60)
        l1.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min=count//60
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    #print(val,val2)
    canvas.itemconfig(timer,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer_clock
        timer_clock= root.after(1000,countdown,count-1)
    else:
        start()
        marks=""
        for _ in range(reps//2):
            marks+="✓"
        check_marks.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #


root=Tk()
root.config(padx=100,pady=50)
root.title("pomodoro")
root.config(bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
pic=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=pic)
timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

canvas.grid(column=2,row=2)


l1=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40))
l1.grid(column=2,row=1)


b1=Button(text="Start",highlightthickness=0,command=start)
b1.grid(column=1,row=3)


b2=Button(text="Reset",highlightthickness=0,command=reset)
b2.grid(column=3,row=3)


check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=2,row=4)





root.mainloop()
