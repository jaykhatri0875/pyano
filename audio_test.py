'''
Mixer module- for playing tunes on action
'''
'''
from pygame import mixer
mixer.init()
mixer.music.load(<path>)
mixer.music.play()
mixer.music.stop()
'''


'''
    playing tunes on button press
'''

#to do:- make class for piano
# make piano view and piano looking properties
#
import os
from tkinter import *
from pygame import mixer
import notes
mixer.init()
root = Tk()

os.chdir(r'F:\Z_SOMETHING\tunes')
#for A notes 
def play_a3():
    mixer.music.load("a3.mp3")
    mixer.music.play()
def play_a_3():
    mixer.music.load("a-3.mp3")
    mixer.music.play()
    
def play_a4():
    mixer.music.load("a4.mp3")
    mixer.music.play()
def play_a_4():
    mixer.music.load("a-4.mp3")
    mixer.music.play()
    
def play_a5():
    mixer.music.load("a5.mp3")
    mixer.music.play()
def play_a_5():
    mixer.music.load("a-5.mp3")
    mixer.music.play()

#for all B notes 
def play_b3():
    mixer.music.load("b3.mp3")
    mixer.music.play()
def play_b_3():
    mixer.music.load("b-3.mp3")
    mixer.music.play()

def play_b4():
    mixer.music.load("b4.mp3")
    mixer.music.play()
def play_b_4():
    mixer.music.load("b-4.mp3")
    mixer.music.play()

def play_b5():
    mixer.music.load("b5.mp3")
    mixer.music.play()
def play_b_5():
    mixer.music.load("b-5.mp3")
    mixer.music.play()

#for all C notes 
def play_c3():
    mixer.music.load("c3.mp3")
    mixer.music.play()
def play_c_3():
    mixer.music.load("c-3.mp3")
    mixer.music.play()

def play_c4():
    mixer.music.load("c4.mp3")
    mixer.music.play()
def play_c_4():
    mixer.music.load("c-4.mp3")
    mixer.music.play()

def play_c5():
    mixer.music.load("c5.mp3")
    mixer.music.play()
def playc5():
    mixer.music.load("c-5.mp3")
    mixer.music.play()
    
#for all D notes
def play_d3():
    mixer.music.load("d3.mp3")
    mixer.music.play()
def play_d_3():
    mixer.music.load("d-3.mp3")
    mixer.music.play()

def play_d4():
    mixer.music.load("d4.mp3")
    mixer.music.play()
def play_d_4():
    mixer.music.load("d-4.mp3")
    mixer.music.play()

def play_d5():
    mixer.music.load("d5.mp3")
    mixer.music.play()
def play_d_5():
    mixer.music.load("d-5.mp3")
    mixer.music.play()

#for all E notes
def play_e3():
    mixer.music.load("e3.mp3")
    mixer.music.play()
def play_e_3():
    mixer.music.load("e-3.mp3")
    mixer.music.play()

def play_e4():
    mixer.music.load("e4.mp3")
    mixer.music.play()
def play_e_4():
    mixer.music.load("e-4.mp3")
    mixer.music.play()

def play_e5():
    mixer.music.load("e5.mp3")
    mixer.music.play()
def play_e_5():
    mixer.music.load("e-5.mp3")
    mixer.music.play()

#for all F notes
def play_f3():
    mixer.music.load("f3.mp3")
    mixer.music.play()
def play_f_3():
    mixer.music.load("f-3.mp3")
    mixer.music.play()

def play_f4():
    mixer.music.load("f4.mp3")
    mixer.music.play()
def play_f_4():
    mixer.music.load("f-4.mp3")
    mixer.music.play()

def play_f5():
    mixer.music.load("f5.mp3")
    mixer.music.play()
def play_f_5():
    mixer.music.load("f-5.mp3")
    mixer.music.play()


#for all G notes
def play_g3():
    mixer.music.load("g3.mp3")
    mixer.music.play()
def play_g_3():
    mixer.music.load("g-3.mp3")
    mixer.music.play()
    
def play_g4():
    mixer.music.load("g4.mp3")
    mixer.music.play()
def play_g_4():
    mixer.music.load("g-4.mp3")
    mixer.music.play()

def play_g5():
    mixer.music.load("g5.mp3")
    mixer.music.play()
def play_g_5():
    mixer.music.load("g-5.mp3")
    mixer.music.play()


    



# buttons in (to be imported from GUI)

b1=Button(root,text="a3",command=play_a3)
b2=Button(root,text="b3",command=play_b3)
b3=Button(root,text="c3",command=play_c3)
b4=Button(root,text="d3",command=play_d4)
b5=Button(root,text="g3",command=play_g3)
b6=Button(root,text="e3",command=play_e3)
b7=Button(root,text="f3",command=play_f3)

b8=Button(root,text="a4",command=play_a4)
b9=Button(root,text="b4",command=play_b4)
b10=Button(root,text="c4",command=play_c4)
b11=Button(root,text="d4",command=play_d4)
b12=Button(root,text="g4",command=play_e4)
b13=Button(root,text="e4",command=play_f4)
b14=Button(root,text="f4",command=play_g4)

b15=Button(root,text="a5",command=play_a5)
b16=Button(root,text="b5",command=play_b5)
b17=Button(root,text="c5",command=play_c5)
b18=Button(root,text="d5",command=play_d5)
b19=Button(root,text="g5",command=play_e5)
b20=Button(root,text="e5",command=play_f5)
b21=Button(root,text="f5",command=play_g5)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()

b8.pack()
b9.pack()
b10.pack()
b11.pack()
b12.pack()
b13.pack()
b14.pack()

b15.pack()
b16.pack()
b17.pack()
b18.pack()
b19.pack()
b20.pack()
b21.pack()

root.mainloop()
