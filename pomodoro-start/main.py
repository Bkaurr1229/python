from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = 1 * 60
    short_break_sec = 2 * 60
    long_break_sec = 3 * 60
    reps += 1

    if reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Short Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)
    else:
        count_down(work_sec)
        label_timer.config(text="working hours", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # code to show min:00 or 01,02......
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=PINK)
# to have a window
# if i have a windo then a thin line will appear creating seperation between window and canvas so to remove that -->
# highlightthickness=0

canvas = Canvas(width=200, height=250, bg=YELLOW)

label_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

# to open the pic
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)

# inner timer
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons
button = Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
button.grid(column=0, row=2)

button = Button(text="Reset", )
button.grid(column=3, row=2)

check_mark = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
check_mark.grid(column=1, row=2)

window.mainloop()
