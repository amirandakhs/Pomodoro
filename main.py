from tkinter import *

#Constants
BACKGROUNDCOLOR = "#F7F5F2"
TIMERCOLOR = "#FF6B6B"
TITLECOLOR = "#FD5D5D"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPEATITION = 0
ROUND_NUM = 4
CYCLE = 0
Timer = None

# RESET THE TIMER 
def reset():
    window.after_cancel(Timer)
    canvas.itemconfig(timer_text, text = "00:00")
    Label.config(timer, text="Timer")
    Check.config(text= "")
    global REPEATITION 
    global CYCLE
    REPEATITION = 0
    CYCLE = 0

# START TIMER  
def start():
    global REPEATITION
    global ROUND_NUM
    global CYCLE
    if(REPEATITION == ROUND_NUM):
        Label.config(timer, text="Have fun", fg="#8479E1" )
        count(LONG_BREAK_MIN * 60)
        REPEATITION =0
    else:
        if(REPEATITION %2 == 0):
            Label.config(timer, text="Work")
            count(WORK_MIN * 60)
        else:
            Label.config(timer, text="Break",fg="#8479E1")
            count(SHORT_BREAK_MIN *60)
            CYCLE +=1
            Check.config(text= "☑"*CYCLE)
            

        REPEATITION += 1
    
    

#COUNTDOWN 
def count(timer):
    canvas.itemconfig(timer_text, text="{:02d}:{:02d}".format(timer//60,timer%60))
    if(timer>0):
        global Timer
        Timer = window.after(5, count, timer-1)
    else:
        start()
#UI SETUP
window = Tk()

window.title("Goal")
window.config(padx=20, pady=20, bg=BACKGROUNDCOLOR)


timer = Label(text="Timer", fg=TITLECOLOR, font=(FONT_NAME, 30), bg=BACKGROUNDCOLOR)
timer.grid(row=0, column=1)

canvas = Canvas(width=250, height=250, bg=BACKGROUNDCOLOR, highlightthickness=0)
img = PhotoImage(file='./images/Goal.png')
canvas.create_image(125, 125, image=img)
timer_text = canvas.create_text(125, 125, text="00:00", fill=TIMERCOLOR, font=(FONT_NAME, 27,'bold'))
canvas.grid(row=1, column=1)


start_btn = Button(text="start", highlightthickness=0, command=start)
start_btn.grid(row=2, column=0)

start_btn = Button(text="reset", highlightthickness=0, command = reset)
start_btn.grid(row=2, column=2)

Check = Label(fg=TITLECOLOR)
Check.grid(row=3, column=1)






window.mainloop()
