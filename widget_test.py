##from tkinter import *
##from tkinter.ttk import *
##
##master = Tk()
##master.geometry("200x200")
##
##btn = Button(master,text="sample")
##btn.pack(fill=X,expand=True,ipady=10)


from tkinter import *
import os
from notes import *
from pygame import mixer
mixer.init()

root = Tk()
root.title('Pyano')
root.geometry('1200x350')
#bg_img = PhotoImage(file='F:\Z_SOMETHING\imgs\bg.png')
root.configure(background='white')
os.chdir(r'F:\pyano\tunes')
def play_a_3(event):
    mixer.music.load("a-3.mp3")
    mixer.music.play()
    
def play_c_3(event):
    mixer.music.load("c-3.mp3")
    mixer.music.play()
    
bt_img=PhotoImage(file='F:\pyano\imgs\key_black.png')
#first note

##b11 = Button(root,image=bt_img,width=30,height=150)
##b11.bind('<A>',play_a_3)
##b11.place(x=20,y=0)
##b21 = Button(root,image=bt_img,width=30,height=150)
##b21.bind('<S>',play_c_3)
##b21.place(x=60,y=0)

##
b31 = Button(root,image=bt_img,width=30,height=150,command=play_d_3).place(x=120,y=0)
b41 = Button(root,image=bt_img,width=30,height=150,command=play_f_3).place(x=160,y=0)
b51 = Button(root,image=bt_img,width=30,height=150,command=play_g_3).place(x=200,y=0)

#second note
b12 = Button(root,image=bt_img,width=30,height=150,command=play_a_4).place(x=270,y=0)
b22 = Button(root,image=bt_img,width=30,height=150,command=play_c_4).place(x=310,y=0)

b32 = Button(root,image=bt_img,width=30,height=150,command=play_d_4).place(x=370,y=0)
b42 = Button(root,image=bt_img,width=30,height=150,command=play_f_4).place(x=410,y=0)
b52 = Button(root,image=bt_img,width=30,height=150,command=play_g_4).place(x=450,y=0)



mainloop()

