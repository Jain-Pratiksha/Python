from tkinter import *
from pygame import mixer

root=Tk()
mixer.init() #initializing the mixer
root.geometry("300x300")
root.title("Melody")

text=Label(root,text="Let's make some noise")
text.pack()

def play_music():
    mixer.music.load("filename.mp3")
    mixer.music.play()
plyBtn=Button(root,text="Play",command=play_music)
plyBtn.pack()

root.mainloop()
