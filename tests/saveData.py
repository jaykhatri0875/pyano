import tkinter as tk

def storeData(state):
    if(state=='1'):
        print("pressed")
    elif(state=='0'):
        print('Not pressed')

cav = tk.Tk()
pbutton = tk.Button(cav,text='Pressed',command = lambda:storeData('1'))
npbutton = tk.Button(cav,text='NotPressed',command = lambda:storeData('0'))
pbutton.pack()
npbutton.pack()
cav.mainloop()
