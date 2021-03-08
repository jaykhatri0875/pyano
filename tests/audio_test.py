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
os.chdir(r'F:\Z_SOMETHING\tunes')
mixer.init()
root = Tk()
def play1():
    mixer.music.load("a3.mp3")
    mixer.music.play()
def play2():
    mixer.music.load("b3.mp3")
    mixer.music.play()
def play3():
    mixer.music.load("c3.mp3")
    mixer.music.play()
def play4():
    mixer.music.load("d3.mp3")
    mixer.music.play()
def play5():
    mixer.music.load("e3.mp3")
    mixer.music.play()
def play6():
    mixer.music.load("f3.mp3")
    mixer.music.play()
def play7():
    mixer.music.load("g3.mp3")
    mixer.music.play()
    
def playa4():
    mixer.music.load("a4.mp3")
    mixer.music.play()
def playb4():
    mixer.music.load("b4.mp3")
    mixer.music.play()
def playc4():
    mixer.music.load("c4.mp3")
    mixer.music.play()
def playd4():
    mixer.music.load("d4.mp3")
    mixer.music.play()
def playe4():
    mixer.music.load("e4.mp3")
    mixer.music.play()
def playf4():
    mixer.music.load("f4.mp3")
    mixer.music.play()
def playg4():
    mixer.music.load("g4.mp3")
    mixer.music.play()

def playa5():
    mixer.music.load("a5.mp3")
    mixer.music.play()
def playb5():
    mixer.music.load("b5.mp3")
    mixer.music.play()
def playc5():
    mixer.music.load("c5.mp3")
    mixer.music.play()
def playd5():
    mixer.music.load("d5.mp3")
    mixer.music.play()
def playe5():
    mixer.music.load("e5.mp3")
    mixer.music.play()
def playf5():
    mixer.music.load("f5.mp3")
    mixer.music.play()
def playg5():
    mixer.music.load("g5.mp3")
    mixer.music.play()


b1=Button(root,text="a3",command=play1)
b2=Button(root,text="b3",command=play2)
b3=Button(root,text="c3",command=play3)
b4=Button(root,text="d3",command=play4)
b5=Button(root,text="g3",command=play5)
b6=Button(root,text="e3",command=play6)
b7=Button(root,text="f3",command=play7)

b8=Button(root,text="a4",command=playa4)
b9=Button(root,text="b4",command=playb4)
b10=Button(root,text="c4",command=playc4)
b11=Button(root,text="d4",command=playd4)
b12=Button(root,text="g4",command=playe4)
b13=Button(root,text="e4",command=playf4)
b14=Button(root,text="f4",command=playg4)

b15=Button(root,text="a5",command=playa5)
b16=Button(root,text="b5",command=playb5)
b17=Button(root,text="c5",command=playc5)
b18=Button(root,text="d5",command=playd5)
b19=Button(root,text="g5",command=playe5)
b20=Button(root,text="e5",command=playf5)
b21=Button(root,text="f5",command=playg5)

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
