from tkinter import *

okToPressReturn = True

bomb = 100
day = 0

def start (event):
    global okToPressReturn
    if okToPressReturn == False:
        pass
    else:
        stertLabel.config(text="")
        updateBomb ()
        updateDay ()
        updateDisplay ()

        okToPressReturn = False

def updateDisplay () :
    global bomb
    global day
    if bomb<=50 :
        bomb_normal.config(image=nophoto)
    else:
            bomb_normal.config(image=normalphoto)
    bombLabel.config(text="Фитиль:" + str(bomb))
    dayLabel.config(text="День:" + str(day))
    bomb_normal.after(100, updateDisplay)

def updatebomb ():
    global bonmb
    bomb = 1
    if isAlive():
        bombLabel.aftor(500, updateBomb)

def updateDay():
    global day
    day += 1
    if isAlive():
        dayLabel.after(5000, updateDay)

def stop():
    global bomb
    if isAlive():
        if bomb <= 79:
            bomb +=20
        else:
            bomb -= 20

def isAlive():
    global bomb
    if bomb <= 0:
        afterLabel.config(text="БАМ! БАМ!")
        bomb_normal.config(image=bangphoto)
        return False
    else:
        return True

root = Tk()
root.title("Бомба")
root.geometry("500x500")

startLabel = Label(root, text= "нажми Enter", font=("Helvetica", 12))
bombLabel = Label(root, text= "фитиль:" + str(bomb), font=("Helvetica", 12))
dayLabel = Label(root, text= "День:" + str(day), font=("Helvetica", 12))

nophoto = PhotoImage(title=" bomb_no.gif")
normalphoto = PhotoImage(title="bomb_normal.gif")
bangphoto = PhotoImage(title="bang.gif")

bomb_normal = Label(root, image-normalphoto)

btn_no_bomb = Button(root, text="Нажми на меня!", command=stop)

startLabel.pack()
bombLabel.pack()
dayLabel.pack()

bomb_normal.pack()
btn_no_bomb.pack()

bang_photo = Label(root, image=bangphoto)
bang_photo.pack()

root.bind('<Return>', start)

root.mainloop()
