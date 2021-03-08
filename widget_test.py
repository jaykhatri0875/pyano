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
root.geometry('750x350')
#bg_img = PhotoImage(file='F:\Z_SOMETHING\imgs\bg.png')
root.configure(background='white')
os.chdir(r'F:\pyano\tunes')

bt_img=PhotoImage(file='F:\pyano\imgs\key_black.png')
wt_img=PhotoImage(file='F:\pyano\imgs\key_white.png')
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
b12 = Button(root,image=bt_img,width=30,height=150,command=play_c_3).place(x=60,y=0)

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

#first 
ba3 = Button(root,image=wt_img,width=27,height=170,command=play_a3).place(x=5,y=160)
bb3 = Button(root,image=wt_img,width=27,height=170,command=play_b3).place(x=40,y=160)
bc3 = Button(root,image=wt_img,width=27,height=170,command=play_c3).place(x=75,y=160)
bd3 = Button(root,image=wt_img,width=27,height=170,command=play_d3).place(x=110,y=160)
be3 = Button(root,image=wt_img,width=27,height=170,command=play_e3).place(x=145,y=160)
bf3 = Button(root,image=wt_img,width=27,height=170,command=play_f3).place(x=180,y=160)
bg3 = Button(root,image=wt_img,width=27,height=170,command=play_g3).place(x=215,y=160)

#second
ba4 = Button(root,image=wt_img,width=27,height=170,command=play_a4).place(x=260,y=160)
bb4 = Button(root,image=wt_img,width=27,height=170,command=play_b4).place(x=295,y=160)
bc4 = Button(root,image=wt_img,width=27,height=170,command=play_c4).place(x=320,y=160)
bd4 = Button(root,image=wt_img,width=27,height=170,command=play_d4).place(x=355,y=160)
be4 = Button(root,image=wt_img,width=27,height=170,command=play_e4).place(x=390,y=160)
bf4 = Button(root,image=wt_img,width=27,height=170,command=play_f4).place(x=425,y=160)
bg4 = Button(root,image=wt_img,width=27,height=170,command=play_g4).place(x=460,y=160)

#third
ba5 = Button(root,image=wt_img,width=27,height=170,command=play_a5).place(x=505,y=160)
bb5 = Button(root,image=wt_img,width=27,height=170,command=play_b5).place(x=530,y=160)
bc5 = Button(root,image=wt_img,width=27,height=170,command=play_c5).place(x=565,y=160)
bd5 = Button(root,image=wt_img,width=27,height=170,command=play_d5).place(x=600,y=160)
be5 = Button(root,image=wt_img,width=27,height=170,command=play_e5).place(x=625,y=160)
bf5 = Button(root,image=wt_img,width=27,height=170,command=play_f5).place(x=670,y=160)
bg5 = Button(root,image=wt_img,width=27,height=170,command=play_g5).place(x=705,y=160)


mainloop()

