from time import *
from tkinter import *


def update():
    time_string = strftime("%I:%M:%S %p")
    timeLabel.config(text=time_string)

    day_string = strftime("%A")
    dayLabel.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    dateLabel.config(text=date_string)

    timeLabel.after(1000, update)


window = Tk()

window.title("Clock")

timeLabel = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
timeLabel.pack()

dayLabel = Label(window, font=("Ink Free", 30, "bold"))
dayLabel.pack()

dateLabel = Label(window, font=("Arial", 30))
dateLabel.pack()

update()

window.mainloop()
