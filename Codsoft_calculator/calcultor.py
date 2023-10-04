from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget('text')
    print(text)
    
    if text == '=': #when click "=" (equal to) button
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except:
                value = 'Error'
        scvalue.set(value)
        screen.update()

    elif text == 'C': #When click C (Clear) button
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk() #creating GUI main window
root.geometry('415x575')
root.minsize(415, 575)
root.maxsize(415, 575)
root.title('Calculator')
root.wm_iconbitmap('calculator.ico')


scvalue = StringVar() #varialbe whose value will be show in calculator screen (screen value)
scvalue.set('')
screen = Entry(root, textvariable=scvalue, font='lucida 40 bold')
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


f = Frame(root, bg='light grey')

b = Button(f, text='*',bg='grey' ,padx=10, pady=1, font='lucida 30 bold')#Creating "*" (Multiplication) button
b.pack(side=RIGHT, padx=15, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='/',bg='grey', padx=16, pady=5, font='lucida 27 bold') #Creating "/" division button
b.pack(side=RIGHT, padx=16, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text='%',bg='grey', padx=5, pady=6, font='lucida 26 bold') #Creating "%" (remainder) button
b.pack(side=RIGHT, padx=17, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='C',bg='grey', padx=5, pady=1, font='lucida 30 bold')#Creating "C" (clear) button
b.pack(side=RIGHT, padx=17.5, pady=4)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='light grey')

b = Button(f, text='-',bg='grey', padx=8, pady=1, font='lucida 34 bold')#Creating "-" (subtract) button
b.pack(side=RIGHT, padx=13.5, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='9',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "9" button
b.pack(side=RIGHT, padx=17, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text='8',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "8" button
b.pack(side=RIGHT, padx=17, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='7',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "7" button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='light grey')

b = Button(f, text='+',bg='grey', padx=1, pady=1, font='lucida 35 bold')#Creating "+" (Addition) button
b.pack(side=RIGHT, padx=12, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='6',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "6" button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text='5',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "5" button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='4',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "4" button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='light grey')

b = Button(f, text='=',bg='orange', padx=1, pady=1, font='lucida 35 bold')#Creating "=" (Equal) button
b.pack(side=RIGHT, padx=11, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='3',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "3" button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind("<Button-1>", click)

b = Button(f, text='2',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "2" button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='1',bg='white', padx=2, pady=1, font='lucida 35 bold')#Creating "1" button
b.pack(side=RIGHT, padx=19, pady=4)
b.bind('<Button-1>', click)

f.pack()


f = Frame(root, bg='light grey')

b = Button(f, text='00',bg='white', padx=46, pady=1, font='lucida 30 bold')# creatin "0" (double zero ) button
b.pack(side=RIGHT, padx=17, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='.',bg='white', padx=13, pady=1, font='lucida 30 bold')#Creating "." (point) button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text='0',bg='white', padx=8, pady=1, font='lucida 30 bold')#Creating "0" button
b.pack(side=RIGHT, padx=18, pady=4)
b.bind("<Button-1>", click)

f.pack()


root.mainloop()
