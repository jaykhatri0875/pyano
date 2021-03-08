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

bt_img=PhotoImage(file='F:\pyano\imgs\key_black.png')

    ##for binding activity of keyboard with buttons but not working properly - need to search on it , to add it first edit notes functions and pass event param
##b11 = Button(root,image=bt_img,width=30,height=150)
##b11.bind('<A>',play_a_3)
##b11.place(x=20,y=0)
##b21 = Button(root,image=bt_img,width=30,height=150)
##b21.bind('<S>',play_c_3)
##b21.place(x=60,y=0)

## black ones 

#first note
b11 = Button(root,image=bt_img,width=30,height=150,command=play_a_3).place(x=20,y=0)
b12 = Button(root,image=bt_img,width=30,height=150,command=play_a_3).place(x=60,y=0)

b31 = Button(root,image=bt_img,width=30,height=150,command=play_d_3).place(x=120,y=0)
b41 = Button(root,image=bt_img,width=30,height=150,command=play_f_3).place(x=160,y=0)
b51 = Button(root,image=bt_img,width=30,height=150,command=play_g_3).place(x=200,y=0)

#second note
b12 = Button(root,image=bt_img,width=30,height=150,command=play_a_4).place(x=270,y=0)
b22 = Button(root,image=bt_img,width=30,height=150,command=play_c_4).place(x=310,y=0)

b32 = Button(root,image=bt_img,width=30,height=150,command=play_d_4).place(x=370,y=0)
b42 = Button(root,image=bt_img,width=30,height=150,command=play_f_4).place(x=410,y=0)
b52 = Button(root,image=bt_img,width=30,height=150,command=play_g_4).place(x=450,y=0)

#third note
b13 = Button(root,image=bt_img,width=30,height=150,command=play_a_5).place(x=520,y=0)
b23 = Button(root,image=bt_img,width=30,height=150,command=play_c_5).place(x=560,y=0)

b33 = Button(root,image=bt_img,width=30,height=150,command=play_d_5).place(x=620,y=0)
b43 = Button(root,image=bt_img,width=30,height=150,command=play_f_5).place(x=660,y=0)
b53 = Button(root,image=bt_img,width=30,height=150,command=play_g_5).place(x=700,y=0)

##white ones


mainloop()

